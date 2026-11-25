"""Google ADK (Agent Development Kit) adapter for afe/v1 agents."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from agents_for_everything import AgentRunner, RunContext, discover_agents, find_repo_root


def as_google_adk_agent_spec(
    agent_id: str,
    repo_root: Path | None = None,
    context: RunContext | None = None,
) -> dict[str, Any]:
    """Build configuration suitable for `google.adk.agents.Agent(**spec)`."""
    root = repo_root or find_repo_root()
    manifest = discover_agents(root)[agent_id]
    assert manifest.directory is not None
    instruction = (manifest.directory / "prompts" / "system.md").read_text(encoding="utf-8")
    runner = AgentRunner(repo_root=root)

    def invoke(payload: dict[str, Any]) -> dict[str, Any]:
        return runner.run(agent_id, payload, context=context).output

    return {
        "name": manifest.id.replace("/", "_").replace("-", "_"),
        "description": manifest.summary,
        "instruction": instruction,
        "tools": [invoke],
        "a2a_id": manifest.id,
    }
