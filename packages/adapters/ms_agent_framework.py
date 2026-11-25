"""Microsoft Agent Framework (AutoGen + Semantic Kernel successor) adapter."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from agents_for_everything import AgentRunner, RunContext, discover_agents, find_repo_root


def as_ms_agent_config(
    agent_id: str,
    repo_root: Path | None = None,
    context: RunContext | None = None,
) -> dict[str, Any]:
    """Return config + callable handler for Microsoft Agent Framework workflows."""
    root = repo_root or find_repo_root()
    manifest = discover_agents(root)[agent_id]
    assert manifest.directory is not None
    instructions = (manifest.directory / "prompts" / "system.md").read_text(encoding="utf-8")
    runner = AgentRunner(repo_root=root)

    return {
        "id": manifest.id,
        "name": manifest.name,
        "instructions": instructions,
        "handler": lambda payload: runner.run(agent_id, payload, context=context).output,
    }
