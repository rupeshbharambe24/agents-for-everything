from __future__ import annotations
import re
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class SummarizerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)
        text = str(input_data["text"]).strip()
        sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
        limit = int(input_data.get("max_sentences", 3))
        top = sents[:limit] if sents else [text]
        return {"summary": " ".join(top), "key_points": top}
