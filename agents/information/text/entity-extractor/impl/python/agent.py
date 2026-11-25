from __future__ import annotations
import re
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class EntityExtractorAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        txt = str(input_data["text"])
        ents: list[dict[str, str]] = []
        for m in re.finditer(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", txt):
            ents.append({"type": "EMAIL", "text": m.group(0)})
        for m in re.finditer(r"(?:INR|USD|\$|₹)\s?\d[\d,]*(?:\.\d+)?", txt):
            ents.append({"type": "MONEY", "text": m.group(0)})
        for m in re.finditer(r"\b[A-Z][a-z]+\s+[A-Z][a-z]+\b", txt):
            ents.append({"type": "PERSON_OR_ORG", "text": m.group(0)})
        return {"entities": ents}
