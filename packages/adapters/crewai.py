"""CrewAI adapter exposing afe/v1 agents as role/goal/backstory specs."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from agents_for_everything import discover_agents, find_repo_root


def as_crewai_agent_spec(agent_id: str, repo_root: Path | None = None) -> dict[str, Any]:
    """Return CrewAI `Agent(role=..., goal=..., backstory=...)` configuration."""
    root = repo_root or find_repo_root()
    manifest = discover_agents(root)[agent_id]
    assert manifest.directory is not None
    backstory = (manifest.directory / "prompts" / "system.md").read_text(encoding="utf-8")
    return {
        "role": manifest.name,
        "goal": manifest.summary,
        "backstory": backstory,
        "allow_delegation": manifest.tier == "composite",
        "max_iter": manifest.max_steps,
    }
