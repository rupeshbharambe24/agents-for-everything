"""End-to-end Accessible Web Companion recipe."""

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


def assist_web_session(
    page_snapshot: str,
    form_schema: dict[str, Any],
    spoken_utterance: str,
    locale: str = "en-IN",
    confirm_submit: bool = False,
    provider_name: str = "auto",
) -> dict[str, Any]:
    runner = AgentRunner(repo_root=REPO_ROOT)
    ctx = RunContext(provider_name=provider_name, auto_approve=confirm_submit, locale=locale)

    audit = runner.run(
        "accessibility/accessibility-auditor",
        {"input": page_snapshot, "locale": locale},
        context=ctx,
    ).output
    narration = runner.run(
        "accessibility/screen-narrator",
        {"input": page_snapshot, "locale": locale},
        context=ctx,
    ).output
    filled = runner.run(
        "voice/voice-form-filler",
        {
            "form": form_schema,
            "audio": {
                "format": "text-simulated",
                "locale_hint": locale,
                "transcript_hint": spoken_utterance,
            },
            "locale": locale,
            "confirm_submit": confirm_submit,
        },
        context=ctx,
    ).output

    return {
        "a11y_audit": audit,
        "narration": narration,
        "form_state": filled,
    }


if __name__ == "__main__":
    sample_form = {
        "id": "civic-portal",
        "title": "Public Service Request",
        "fields": [
            {"id": "full_name", "label": "Full Name", "type": "string", "required": True},
            {"id": "city", "label": "City", "type": "string", "required": True},
            {"id": "pincode", "label": "PIN Code", "type": "string", "required": True},
        ],
    }
    print(
        json.dumps(
            assist_web_session(
                "Heading: Public Service Request Form; Inputs: full_name, city, pincode",
                sample_form,
                "My name is Aarav Mehta, city Pune, pincode 411001",
            ),
            indent=2,
        )
    )
