"""End-to-end Vernacular Banking Helpline recipe."""

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


def handle_banking_call(
    utterance: str,
    locale: str = "hi-IN",
    suspicious_message: str | None = None,
    file_grievance: bool = False,
    auto_approve: bool = False,
    provider_name: str = "auto",
) -> dict[str, Any]:
    runner = AgentRunner(repo_root=REPO_ROOT)
    ctx = RunContext(provider_name=provider_name, auto_approve=auto_approve, locale=locale)

    voice_turn = runner.run(
        "voice/realtime-voice-assistant",
        {
            "audio": {"format": "text-simulated", "locale_hint": locale, "transcript_hint": utterance},
            "locale": locale,
        },
        context=ctx,
    ).output

    banking_reply = runner.run(
        "banking/banking-voice-assistant",
        {"input": utterance, "locale": locale, "execute": False},
        context=ctx,
    ).output

    scam_check = None
    if suspicious_message:
        scam_check = runner.run(
            "banking/scam-message-checker",
            {"input": suspicious_message, "locale": locale},
            context=ctx,
        ).output

    grievance = None
    if file_grievance:
        grievance = runner.run(
            "banking/grievance-redressal",
            {"input": utterance, "locale": locale, "execute": True},
            context=ctx,
        ).output

    return {
        "ai_disclosed": True,
        "locale": locale,
        "voice_turn": voice_turn,
        "banking_reply": banking_reply,
        "scam_check": scam_check,
        "grievance": grievance,
    }


if __name__ == "__main__":
    print(
        json.dumps(
            handle_banking_call(
                "Mere khate se anjan UPI katoti hui hai",
                locale="hi-IN",
                suspicious_message="Click http://bit.ly/fake-kyc to unblock account",
                file_grievance=False,
            ),
            indent=2,
            ensure_ascii=False,
        )
    )
