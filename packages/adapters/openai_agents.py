"""OpenAI Agents SDK adapter returning declarative Agent kwargs + tool callable."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from agents_for_everything import AgentRunner, RunContext, discover_agents, find_repo_root


def as_openai_agent_spec(
    agent_id: str,
    repo_root: Path | None = None,
    context: RunContext | None = None,
) -> dict[str, Any]:
    """Build configuration suitable for `agents.Agent(**spec)` in OpenAI Agents SDK."""
    root = repo_root or find_repo_root()
    manifest = discover_agents(root)[agent_id]
    assert manifest.directory is not None
    instructions = (manifest.directory / "prompts" / "system.md").read_text(encoding="utf-8")
    runner = AgentRunner(repo_root=root)

    def run_tool(payload: dict[str, Any]) -> dict[str, Any]:
        return runner.run(agent_id, payload, context=context).output

    return {
        "name": manifest.name,
        "instructions": instructions,
        "handoff_description": manifest.summary,
        "afe_tool": run_tool,
        "metadata": {"id": manifest.id, "safety_level": manifest.safety_level},
    }
