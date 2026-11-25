"""End-to-end Deep Research application."""

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


def run_research(topic: str, provider_name: str = "auto") -> dict[str, Any]:
    runner = AgentRunner(repo_root=REPO_ROOT)
    ctx = RunContext(provider_name=provider_name)

    quick = runner.run("search/answer-engine", {"question": topic}, context=ctx).output
    deep = runner.run("research/deep-researcher", {"topic": topic, "depth": "standard"}, context=ctx).output
    hal = runner.run(
        "guardrails/hallucination-checker",
        {
            "answer": quick["answer"],
            "sources": [c.get("quote", "") for c in deep.get("citations", [])] or [topic],
        },
        context=ctx,
    ).output
    return {
        "topic": topic,
        "quick_answer": quick["answer"],
        "report_markdown": deep["report_markdown"],
        "citations": deep["citations"],
        "verified_claims": deep["verified_claims"],
        "grounded": hal["grounded"],
    }


if __name__ == "__main__":
    print(json.dumps(run_research("Open-source AI agent standards MCP and A2A"), indent=2))
