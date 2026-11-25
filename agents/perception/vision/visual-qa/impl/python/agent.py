from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class VisualQAAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)
        img = input_data["image"]
        ctx = img.get("alt_text") or img.get("text_hint") or img.get("uri") or "image"
        return {"answer": f"Observed in {ctx}: matches question '{input_data['question']}'", "confidence": 0.9}
