"""End-to-end AI Receptionist recipe."""

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


def handle_inbound_inquiry(
    question: str,
    faq_docs: list[dict[str, str]],
    caller_email: str,
    slots: list[str],
    confirm_booking: bool = False,
    provider_name: str = "auto",
) -> dict[str, Any]:
    runner = AgentRunner(repo_root=REPO_ROOT)
    ctx = RunContext(provider_name=provider_name, auto_approve=confirm_booking)

    faq = runner.run("search/rag-qa", {"question": question, "documents": faq_docs}, context=ctx).output
    booking = runner.run(
        "meetings/meeting-scheduler",
        {
            "title": "Clinic Appointment",
            "attendees": [caller_email],
            "candidate_slots": slots,
            "confirm": confirm_booking,
        },
        context=ctx,
    ).output
    return {
        "ai_disclosed": True,
        "faq_answer": faq["answer"],
        "booking": booking,
    }


if __name__ == "__main__":
    print(json.dumps(handle_inbound_inquiry("What are your clinic hours?", [{"title": "Hours", "content": "Open 9 AM to 6 PM Monday through Saturday."}], "guest@example.org", ["2026-11-26T10:00Z"]), indent=2))
