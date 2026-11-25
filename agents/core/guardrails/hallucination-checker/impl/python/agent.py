"""Grounding / Hallucination Checker implementation."""

from __future__ import annotations

import re
from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

_STOPWORDS = {"the", "and", "for", "with", "that", "this", "from", "are", "was", "were", "has", "have"}


class HallucinationCheckerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        answer = str(input_data["answer"]).strip()
        sources_text = " ".join(str(s) for s in input_data.get("sources", [])).lower()
        source_tokens = {t for t in re.findall(r"[a-z0-9]+", sources_text) if len(t) > 2 and t not in _STOPWORDS}

        claims = [c.strip() for c in re.split(r"[.!?]+", answer) if len(c.strip()) > 4]
        verdicts: list[dict[str, Any]] = []
        unsupported = 0
        for claim in claims:
            c_tokens = {t for t in re.findall(r"[a-z0-9]+", claim.lower()) if len(t) > 2 and t not in _STOPWORDS}
            overlap = len(c_tokens & source_tokens) / max(1, len(c_tokens))
            supported = overlap >= 0.45 and bool(c_tokens)
            if not supported:
                unsupported += 1
            verdicts.append({"claim": claim, "supported": supported, "overlap": round(overlap, 2)})

        return {
            "grounded": unsupported == 0 and len(claims) > 0,
            "unsupported_claims": unsupported,
            "claim_verdicts": verdicts,
        }
