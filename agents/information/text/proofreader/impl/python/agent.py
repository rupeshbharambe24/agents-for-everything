from __future__ import annotations
import re
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

_TYPOS = {"teh": "the", "recieve": "receive", "seperate": "separate", "occured": "occurred"}

class ProofreaderAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)
        raw = str(input_data["text"])
        clean = re.sub(r"\s+", " ", raw).strip()
        corrections: list[str] = []
        if clean != raw.strip():
            corrections.append("Normalized extra whitespace")
        for bad, good in _TYPOS.items():
            if re.search(rf"\b{bad}\b", clean, re.I):
                clean = re.sub(rf"\b{bad}\b", good, clean, flags=re.I)
                corrections.append(f"{bad} -> {good}")
        return {"clean_text": clean, "corrections": corrections}
