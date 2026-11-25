"""Agent execution engine for afe/v1 agents."""

from __future__ import annotations

import importlib.util
import json
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from ._compat import SchemaValidationError, validate_json_schema
from .manifest import discover_agents, find_repo_root, load_agent_manifest
from .mcp import LocalMCPRegistry
from .models import AgentManifest, RunContext, RunResult
from .providers.base import BaseModelProvider, CompletionRequest
from .providers.factory import resolve_provider
from .safety import ApprovalHandler, SafetyPolicy
from .tracing import TraceCollector


class BaseAgentImplementation(ABC):
    """Optional custom implementation class in `impl/python/agent.py`."""

    @abstractmethod
    def run(
        self,
        input_data: dict[str, Any],
        runner: "AgentExecutionHelper",
    ) -> dict[str, Any]:
        """Execute agent logic and return output conforming to output.schema.json."""


class AgentExecutionHelper:
    """Runtime services exposed to custom Python agent implementations."""

    def __init__(
        self,
        manifest: AgentManifest,
        system_prompt: str,
        input_schema: dict[str, Any],
        output_schema: dict[str, Any],
        provider: BaseModelProvider,
        mcp: LocalMCPRegistry,
        safety: SafetyPolicy,
        tracer: TraceCollector,
        context: RunContext,
        parent_runner: "AgentRunner",
        start_time: float,
    ) -> None:
        self.manifest = manifest
        self.system_prompt = system_prompt
        self.input_schema = input_schema
        self.output_schema = output_schema
        self.provider = provider
        self.mcp = mcp
        self.safety = safety
        self.tracer = tracer
        self.context = context
        self._parent_runner = parent_runner
        self._start_time = start_time
        self.steps = 0
        self.cost_usd = 0.0
        self._declared_tools = set(manifest.required_tools) | set(manifest.optional_tools)

    def complete(
        self,
        payload: dict[str, Any],
        system_override: str | None = None,
    ) -> dict[str, Any]:
        """Invoke the configured LLM provider with schema enforcement."""
        self.steps += 1
        self.safety.enforce_limits(
            self.steps, time.monotonic() - self._start_time, self.cost_usd
        )
        span = self.tracer.start_span(
            f"gen_ai.chat.{self.manifest.id}",
            {
                "gen_ai.system": self.provider.config.name,
                "gen_ai.operation.name": "chat",
                "gen_ai.request.model": self.provider.config.model,
                "afe.agent.id": self.manifest.id,
            },
        )
        resp = self.provider.complete(
            CompletionRequest(
                system_prompt=system_override or self.system_prompt,
                user_payload=payload,
                output_schema=self.output_schema,
            )
        )
        self.cost_usd += resp.cost_usd
        self.tracer.finish_span(
            span,
            extra={
                "gen_ai.usage.input_tokens": resp.input_tokens,
                "gen_ai.usage.output_tokens": resp.output_tokens,
            },
        )
        if resp.parsed_json is not None:
            return resp.parsed_json
        return {"text": resp.content}

    def call_tool(self, server_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        """Call a declared MCP server tool after checking safety permissions."""
        self.steps += 1
        self.safety.enforce_limits(
            self.steps, time.monotonic() - self._start_time, self.cost_usd
        )
        self.safety.check_tool_permission(server_id, self._declared_tools)
        span = self.tracer.start_span(
            f"mcp.tool.{server_id}",
            {"afe.agent.id": self.manifest.id, "afe.mcp.server": server_id},
        )
        result = self.mcp.call(server_id, payload)
        self.tracer.finish_span(span)
        return result

    def require_approval(self, action: str, summary: str) -> bool:
        """Request human approval for gated side effects."""
        return self.safety.require_approval(action, summary)

    def call_agent(self, agent_id: str, input_data: dict[str, Any]) -> dict[str, Any]:
        """Invoke a composed subagent declared in `uses_agents`."""
        if agent_id not in self.manifest.uses_agents:
            raise PermissionError(
                f"Agent {self.manifest.id} attempted undeclared subagent call to {agent_id!r}"
            )
        sub_res = self._parent_runner.run(
            agent_id,
            input_data,
            context=self.context,
            tracer=self.tracer,
        )
        self.cost_usd += sub_res.cost_usd
        return sub_res.output


def _load_custom_impl(agent_dir: Path, agent_id: str) -> Any | None:
    impl_path = agent_dir / "impl" / "python" / "agent.py"
    if not impl_path.exists():
        return None
    mod_name = f"afe_agent_impl_{agent_id.replace('/', '_').replace('-', '_')}"
    spec = importlib.util.spec_from_file_location(mod_name, impl_path)
    if spec is None or spec.loader is None:
        return None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for attr in dir(module):
        obj = getattr(module, attr)
        if (
            isinstance(obj, type)
            and issubclass(obj, BaseAgentImplementation)
            and obj is not BaseAgentImplementation
        ):
            return obj()
    if hasattr(module, "run") and callable(module.run):
        return module
    return None


class AgentRunner:
    """Loads, validates, and executes `afe/v1` agents."""

    def __init__(
        self,
        repo_root: Path | None = None,
        mcp: LocalMCPRegistry | None = None,
        approval_handler: ApprovalHandler | None = None,
    ) -> None:
        self.repo_root = (repo_root or find_repo_root()).resolve()
        self.types_dir = self.repo_root / "spec" / "types"
        self.mcp = mcp or LocalMCPRegistry(workspace_root=self.repo_root)
        self.approval_handler = approval_handler
        self._catalog_cache: dict[str, AgentManifest] | None = None

    def _resolve_agent_dir(self, agent_ref: str | Path) -> tuple[Path, AgentManifest]:
        if isinstance(agent_ref, Path) or (
            isinstance(agent_ref, str) and (Path(agent_ref) / "agent.yaml").exists()
        ):
            path = Path(agent_ref).resolve()
            return path, load_agent_manifest(path)
        if self._catalog_cache is None:
            self._catalog_cache = discover_agents(self.repo_root)
        if agent_ref not in self._catalog_cache:
            raise KeyError(f"Agent not found in catalog: {agent_ref!r}")
        manifest = self._catalog_cache[agent_ref]
        assert manifest.directory is not None
        return manifest.directory, manifest

    def run(
        self,
        agent_ref: str | Path,
        input_data: dict[str, Any],
        context: RunContext | None = None,
        provider: BaseModelProvider | None = None,
        tracer: TraceCollector | None = None,
    ) -> RunResult:
        """Execute an agent with full I/O schema validation, safety, and tracing."""
        ctx = context or RunContext()
        agent_dir, manifest = self._resolve_agent_dir(agent_ref)
        input_schema = json.loads((agent_dir / manifest.input_schema_path).read_text(encoding="utf-8"))
        output_schema = json.loads((agent_dir / manifest.output_schema_path).read_text(encoding="utf-8"))
        system_prompt = (agent_dir / "prompts" / "system.md").read_text(encoding="utf-8")

        in_errors = validate_json_schema(input_data, input_schema, self.types_dir)
        if in_errors:
            raise SchemaValidationError(
                f"Invalid input for {manifest.id}: {'; '.join(in_errors)}"
            )

        active_provider = provider or resolve_provider(ctx.provider_name, ctx.model)
        active_tracer = tracer or TraceCollector(
            trace_id=ctx.trace_id, mask_pii=manifest.handles_pii or True
        )
        safety = SafetyPolicy(
            manifest,
            auto_approve=ctx.auto_approve,
            approval_handler=self.approval_handler,
        )

        start = time.monotonic()
        root_span = active_tracer.start_span(
            f"afe.agent.run.{manifest.id}",
            {
                "afe.agent.id": manifest.id,
                "afe.agent.tier": manifest.tier,
                "afe.safety.level": manifest.safety_level,
                "afe.autonomy": manifest.autonomy,
            },
        )
        helper = AgentExecutionHelper(
            manifest=manifest,
            system_prompt=system_prompt,
            input_schema=input_schema,
            output_schema=output_schema,
            provider=active_provider,
            mcp=self.mcp,
            safety=safety,
            tracer=active_tracer,
            context=ctx,
            parent_runner=self,
            start_time=start,
        )

        custom = _load_custom_impl(agent_dir, manifest.id)
        if custom is not None:
            output = custom.run(input_data, helper)
        else:
            output = helper.complete(input_data)

        out_errors = validate_json_schema(output, output_schema, self.types_dir)
        if out_errors:
            active_tracer.finish_span(root_span, status="ERROR")
            raise SchemaValidationError(
                f"Invalid output from {manifest.id}: {'; '.join(out_errors)}"
            )

        elapsed_ms = round((time.monotonic() - start) * 1000, 2)
        active_tracer.finish_span(root_span, status="OK")
        return RunResult(
            agent_id=manifest.id,
            output=output,
            status="ok",
            trace=active_tracer.export(),
            steps=max(1, helper.steps),
            latency_ms=elapsed_ms,
            cost_usd=helper.cost_usd,
        )
