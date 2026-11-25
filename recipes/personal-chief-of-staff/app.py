"""End-to-end Personal Chief of Staff recipe."""

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


def build_morning_brief(
    emails: list[dict[str, str]],
    notes: str,
    memories: list[str],
    provider_name: str = "auto",
) -> dict[str, Any]:
    runner = AgentRunner(repo_root=REPO_ROOT)
    ctx = RunContext(provider_name=provider_name)

    inbox = runner.run("communication/inbox-triager", {"emails": emails}, context=ctx).output
    tasks = runner.run("productivity/task-manager", {"notes": notes}, context=ctx).output
    recalled = runner.run("memory/memory-retriever", {"query": "priorities language", "memories": memories}, context=ctx).output
    brief = runner.run("productivity/daily-briefer", {"input": f"{inbox['urgent_count']} urgent mails; top task: {tasks['top_focus']}"}, context=ctx).output
    return {
        "urgent_emails": inbox["urgent_count"],
        "top_focus": tasks["top_focus"],
        "memories": recalled["matches"],
        "brief": brief["result"],
    }


if __name__ == "__main__":
    print(json.dumps(build_morning_brief([{"id": "1", "subject": "URGENT review", "body": "ASAP"}], "Priya will ship docs.", ["Prefers brief bullets"]), indent=2))
