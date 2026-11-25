"""Typed domain models for Agents for Everything (afe/v1)."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class AgentManifest:
    """Parsed `agent.yaml` manifest."""

    id: str
    name: str
    version: str
    family: str
    category: str
    tier: str
    maturity: str
    priority: str
    license: str
    summary: str
    purpose: str
    pattern: str
    autonomy: str
    input_schema_path: str
    output_schema_path: str
    capabilities: list[str] = field(default_factory=list)
    optional_capabilities: list[str] = field(default_factory=list)
    min_context_tokens: int = 8000
    tested_with: list[str] = field(default_factory=list)
    required_tools: list[str] = field(default_factory=list)
    optional_tools: list[str] = field(default_factory=list)
    uses_agents: list[str] = field(default_factory=list)
    memory: str = "none"
    safety_level: str = "S0"
    side_effects: list[str] = field(default_factory=list)
    approval_required_for: list[str] = field(default_factory=list)
    handles_pii: bool = False
    data_retention: str = "none"
    max_steps: int = 10
    timeout_seconds: float = 60.0
    max_cost_usd: float = 0.05
    eval_suite: str = "evals/eval.yaml"
    eval_targets: dict[str, float] = field(default_factory=dict)
    exports: list[str] = field(default_factory=list)
    locales: list[str] = field(default_factory=lambda: ["en"])
    tags: list[str] = field(default_factory=list)
    maintainers: list[str] = field(default_factory=list)
    raw: dict[str, Any] = field(default_factory=dict)
    directory: Path | None = None


@dataclass(slots=True)
class TeamManifest:
    """Parsed `team.yaml` manifest."""

    id: str
    name: str
    version: str
    maturity: str
    priority: str
    summary: str
    pattern: str
    entry: str
    members: list[str]
    graph: list[list[Any]]
    approvals: list[str] = field(default_factory=list)
    safety_level: str = "S1"
    raw: dict[str, Any] = field(default_factory=dict)
    directory: Path | None = None


@dataclass(slots=True)
class RecipeManifest:
    """Parsed `recipe.yaml` manifest."""

    id: str
    name: str
    version: str
    maturity: str
    priority: str
    summary: str
    problem: str
    solution: str
    agents: list[str]
    teams: list[str]
    mcp_servers: list[str]
    entrypoint: str
    raw: dict[str, Any] = field(default_factory=dict)
    directory: Path | None = None


@dataclass(slots=True)
class MCPServerManifest:
    """Parsed `mcp-servers/<slug>/server.yaml` manifest."""

    id: str
    name: str
    version: str
    summary: str
    transport: str
    tools: list[dict[str, Any]] = field(default_factory=list)
    upstream: str | None = None
    raw: dict[str, Any] = field(default_factory=dict)
    directory: Path | None = None


@dataclass(slots=True)
class RunContext:
    """Execution context passed into agent runs."""

    provider_name: str = "auto"
    model: str | None = None
    auto_approve: bool = False
    locale: str = "en"
    trace_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class RunResult:
    """Output and telemetry from a single agent or team run."""

    agent_id: str
    output: dict[str, Any]
    status: str
    trace: list[dict[str, Any]] = field(default_factory=list)
    steps: int = 1
    latency_ms: float = 0.0
    cost_usd: float = 0.0
    warnings: list[str] = field(default_factory=list)


@dataclass(slots=True)
class EvalCase:
    """Single evaluation fixture parsed from `evals/cases.jsonl`."""

    id: str
    input: dict[str, Any]
    expected: dict[str, Any]
    tags: list[str] = field(default_factory=list)
    locale: str = "en"
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class EvalSummary:
    """Summary metrics from running an agent eval suite."""

    agent_id: str
    total: int
    passed: int
    failed: int
    pass_rate: float
    failures: list[dict[str, Any]] = field(default_factory=list)
