"""End-to-end Content Engine recipe."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

RECIPE_DIR = Path(__file__).resolve().parent
REPO_ROOT = RECIPE_DIR.parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "packages" / "core-python" / "src"))

from agents_for_everything import AgentRunner, RunContext  # noqa: E402


def repurpose_episode(topic: str, transcript: str, provider_name: str = "auto") -> dict[str, Any]:
    runner = AgentRunner(repo_root=REPO_ROOT)
    ctx = RunContext(provider_name=provider_name)

    podcast = runner.run("audio/podcast-producer", {"input": transcript}, context=ctx).output
    blog = runner.run("content/blog-writer", {"input": f"{topic}: {transcript[:120]}"}, context=ctx).output
    edited = runner.run("content/editor", {"input": blog["result"]}, context=ctx).output
    social = runner.run("content/social-post-writer", {"input": edited["result"]}, context=ctx).output
    clips = runner.run("video/clip-generator", {"input": transcript}, context=ctx).output
    return {
        "podcast": podcast["result"],
        "blog_edited": edited["result"],
        "social_post": social["result"],
        "clips": clips["result"],
    }


if __name__ == "__main__":
    print(json.dumps(repurpose_episode("Composable AI Agents", "Today we discuss atomic agents, MCP, and A2A."), indent=2))
