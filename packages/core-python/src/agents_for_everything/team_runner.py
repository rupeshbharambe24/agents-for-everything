"""Team workflow graph executor for afe/v1 teams."""

from __future__ import annotations

import json
import operator
import re
from pathlib import Path
from typing import Any, Callable

from .manifest import discover_teams, find_repo_root, load_team_manifest
from .models import RunContext, RunResult, TeamManifest
from .providers.base import BaseModelProvider
from .runner import AgentRunner
from .tracing import TraceCollector

_OPS: dict[str, Callable[[Any, Any], bool]] = {
    ">": operator.gt,
    ">=": operator.ge,
    "<": operator.lt,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
}


def evaluate_condition(expr: str, state: dict[str, Any]) -> bool:
    """Safely evaluate simple graph edge conditions like `unsupported_claims > 0`."""
    match = re.fullmatch(r"\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*(>=|<=|==|!=|>|<)\s*(.+?)\s*", expr)
    if not match:
        return False
    key, op_str, rhs_raw = match.groups()
    if key not in state:
        return False
    lhs = state[key]
    rhs_clean = rhs_raw.strip().strip('"').strip("'")
    if rhs_clean.lower() == "true":
        rhs: Any = True
    elif rhs_clean.lower() == "false":
        rhs = False
    elif re.fullmatch(r"-?[0-9]+", rhs_clean):
        rhs = int(rhs_clean)
    elif re.fullmatch(r"-?[0-9]+\.[0-9]+", rhs_clean):
        rhs = float(rhs_clean)
    else:
        rhs = rhs_clean
    try:
        return _OPS[op_str](lhs, rhs)
    except TypeError:
        return False


def _bridge_missing_required(state: dict[str, Any], input_schema: dict[str, Any]) -> dict[str, Any]:
    """Adapt standard afe/v1 state fields when upstream output uses an alias key."""
    adapted = dict(state)
    for req in input_schema.get("required", []):
        if req in adapted:
            continue
        if req == "text":
            tr = adapted.get("transcript")
            if isinstance(tr, dict) and tr.get("text"):
                adapted["text"] = tr["text"]
            elif isinstance(adapted.get("markdown"), str):
                adapted["text"] = adapted["markdown"]
            elif isinstance(adapted.get("summary"), str):
                adapted["text"] = adapted["summary"]
        elif req == "notes":
            tr = adapted.get("transcript")
            if isinstance(tr, dict) and tr.get("text"):
                adapted["notes"] = tr["text"]
            elif isinstance(adapted.get("summary"), str):
                adapted["notes"] = adapted["summary"]
        elif req == "transcript" and isinstance(adapted.get("text"), str):
            adapted["transcript"] = adapted["text"]
        elif req == "claims" and isinstance(adapted.get("key_points"), list):
            adapted["claims"] = adapted["key_points"]
        elif req == "findings" and isinstance(adapted.get("key_points"), list):
            adapted["findings"] = adapted["key_points"]
        elif req == "answer" and isinstance(adapted.get("report_markdown"), str):
            adapted["answer"] = adapted["report_markdown"]
        elif req == "sources":
            if isinstance(adapted.get("findings"), list):
                adapted["sources"] = adapted["findings"]
            elif isinstance(adapted.get("key_points"), list):
                adapted["sources"] = adapted["key_points"]
        elif req == "data" and isinstance(adapted.get("extracted"), dict):
            adapted["data"] = adapted["extracted"]
        elif req == "action" and isinstance(adapted.get("decision"), str):
            adapted["action"] = adapted["decision"]
        elif req == "summary" and isinstance(adapted.get("draft_reply"), str):
            adapted["summary"] = adapted["draft_reply"]
    return adapted


class TeamRunner:
    """Executes `team.yaml` directed workflows across member agents."""

    def __init__(
        self,
        repo_root: Path | None = None,
        agent_runner: AgentRunner | None = None,
    ) -> None:
        self.repo_root = (repo_root or find_repo_root()).resolve()
        self.agent_runner = agent_runner or AgentRunner(repo_root=self.repo_root)

    def _resolve_team(self, team_ref: str | Path) -> TeamManifest:
        if isinstance(team_ref, Path) or (
            isinstance(team_ref, str) and (Path(team_ref) / "team.yaml").exists()
        ):
            return load_team_manifest(Path(team_ref).resolve())
        teams = discover_teams(self.repo_root)
        if team_ref not in teams:
            raise KeyError(f"Team not found: {team_ref!r}")
        return teams[team_ref]

    def _member_by_node(self, team: TeamManifest, node_name: str) -> str:
        if "/" in node_name:
            return node_name
        for member in team.members:
            if member.endswith(f"/{node_name}"):
                return member
        raise KeyError(f"Node {node_name!r} does not match any member in team {team.id}")

    def run(
        self,
        team_ref: str | Path,
        input_data: dict[str, Any],
        context: RunContext | None = None,
        provider: BaseModelProvider | None = None,
        max_hops: int = 12,
    ) -> RunResult:
        """Walk the team graph starting at `spec.entry` until terminal node or hop limit."""
        team = self._resolve_team(team_ref)
        ctx = context or RunContext()
        tracer = TraceCollector(trace_id=ctx.trace_id)

        state: dict[str, Any] = dict(input_data)
        current_id = team.entry
        visited_outputs: dict[str, Any] = {}
        hops = 0

        while hops < max_hops:
            hops += 1
            agent_dir, manifest = self.agent_runner._resolve_agent_dir(current_id)
            in_schema = json.loads((agent_dir / manifest.input_schema_path).read_text(encoding="utf-8"))
            payload = _bridge_missing_required(state, in_schema)
            res = self.agent_runner.run(
                current_id,
                payload,
                context=ctx,
                provider=provider,
                tracer=tracer,
            )
            visited_outputs[current_id] = res.output
            state.update(res.output)

            # Pick next matching outgoing edge from current node
            cur_slug = current_id.split("/", 1)[-1]
            next_id: str | None = None
            for edge in team.graph:
                src = edge[0]
                dst = edge[1]
                cond = edge[2] if len(edge) > 2 and isinstance(edge[2], dict) else None
                if src == current_id or src == cur_slug:
                    if cond and "when" in cond:
                        if not evaluate_condition(str(cond["when"]), state):
                            continue
                    next_id = self._member_by_node(team, dst)
                    break

            if next_id is None:
                break
            current_id = next_id

        return RunResult(
            agent_id=f"team/{team.id}",
            output={"final": state, "steps": visited_outputs},
            status="ok",
            trace=tracer.export(),
            steps=hops,
        )
