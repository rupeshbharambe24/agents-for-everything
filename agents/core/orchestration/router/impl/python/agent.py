"""Intent Router implementation."""

from __future__ import annotations

import re
from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

_DEFAULT_RULES: list[tuple[str, tuple[str, ...]]] = [
    ("voice/voice-form-filler", ("fill form", "voice form", "speak form", "loan form", "dictate form")),
    ("voice/speech-to-text", ("transcribe", "speech to text", "audio to text", "voice note")),
    ("text/summarizer", ("summarize", "summary", "tl;dr", "tldr", "condense")),
    ("text/translator", ("translate", "hindi", "spanish", "french", "marathi", "tamil")),
    ("text/structured-extractor", ("extract json", "parse fields", "structured", "schema")),
    ("search/web-search", ("search web", "google", "look up", "find online")),
    ("research/deep-researcher", ("deep research", "investigate", "comprehensive report")),
    ("documents/invoice-receipt-parser", ("invoice", "receipt", "gst", "bill")),
    ("coding/code-reviewer", ("review code", "review pr", "diff", "code review")),
    ("coding/bug-fixer", ("fix bug", "traceback", "stack trace", "error in code")),
    ("data/text-to-sql", ("sql", "query database", "select rows", "postgres")),
    ("guardrails/pii-redactor", ("redact", "mask pii", "aadhaar", "pan", "ssn", "privacy")),
    ("communication/inbox-triager", ("inbox", "triage email", "urgent emails")),
]


class RouterAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)

        req = str(input_data["request"]).lower()
        top_k = int(input_data.get("top_k", 3))
        candidates = input_data.get("candidates")
        scored: list[tuple[float, str]] = []

        if isinstance(candidates, list) and candidates:
            req_tokens = set(re.findall(r"[a-z0-9]+", req))
            for cand in candidates:
                cid = str(cand.get("id", ""))
                desc = f"{cid} {cand.get('summary', '')} {' '.join(cand.get('tags', []))}".lower()
                desc_tokens = set(re.findall(r"[a-z0-9]+", desc))
                overlap = len(req_tokens & desc_tokens)
                score = min(0.99, 0.35 + 0.15 * overlap) if overlap else 0.1
                scored.append((score, cid))
        else:
            for aid, keywords in _DEFAULT_RULES:
                hits = sum(1 for kw in keywords if kw in req)
                if hits:
                    scored.append((min(0.98, 0.65 + 0.12 * hits), aid))

        scored.sort(reverse=True)
        if not scored:
            scored = [(0.45, "search/answer-engine")]

        best_score, best_id = scored[0]
        return {
            "agent_id": best_id,
            "arguments": {"request": input_data["request"]},
            "confidence": round(best_score, 2),
            "alternatives": [{"agent_id": aid, "confidence": round(s, 2)} for s, aid in scored[1:top_k]],
        }
