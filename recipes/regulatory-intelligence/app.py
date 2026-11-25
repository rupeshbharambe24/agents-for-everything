"""End-to-end Regulatory Intelligence recipe."""

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


def assess_circular(
    circular_title: str,
    circular_summary: str,
    policy_scope: str = "KYC and digital lending controls",
    provider_name: str = "auto",
) -> dict[str, Any]:
    runner = AgentRunner(repo_root=REPO_ROOT)
    ctx = RunContext(provider_name=provider_name)

    tracked = runner.run(
        "banking/regulatory-circular-tracker",
        {"input": f"{circular_title}: {circular_summary}"},
        context=ctx,
    ).output
    compliance = runner.run(
        "legal/compliance-monitor",
        {"input": f"Map circular '{circular_title}' against policy scope: {policy_scope}"},
        context=ctx,
    ).output
    analysis = runner.run(
        "research/policy-analyst",
        {"input": f"Impact assessment for {circular_title} under {policy_scope}"},
        context=ctx,
    ).output
    brief = runner.run(
        "research/report-writer",
        {
            "topic": circular_title,
            "findings": [tracked["result"], compliance["result"], analysis["result"]],
        },
        context=ctx,
    ).output

    return {
        "tracked": tracked,
        "compliance": compliance,
        "analysis": analysis,
        "briefing_report": brief,
    }


if __name__ == "__main__":
    print(
        json.dumps(
            assess_circular(
                "Updated Video-KYC Re-verification Guidance",
                "Requires periodic customer due diligence refresh and explicit consent logs.",
            ),
            indent=2,
        )
    )
