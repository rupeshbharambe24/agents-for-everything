"""Claude Agent SDK adapter exporting afe/v1 agents as scoped subagent definitions."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from agents_for_everything import discover_agents, find_repo_root


def as_claude_subagent(agent_id: str, repo_root: Path | None = None) -> dict[str, Any]:
    """Return a Claude Agent SDK `AgentDefinition`-compatible dictionary."""
    root = repo_root or find_repo_root()
    manifest = discover_agents(root)[agent_id]
    assert manifest.directory is not None
    prompt = (manifest.directory / "prompts" / "system.md").read_text(encoding="utf-8")
    return {
        "name": manifest.id.split("/", 1)[-1],
        "description": manifest.summary,
        "prompt": prompt,
        "tools": manifest.required_tools,
        "safety_level": manifest.safety_level,
    }
