from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class ScreenParserAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)
        hint = str(input_data["image"].get("text_hint") or "Submit")
        elements = [{"type": "input", "label": part.strip(), "bbox": [10, 20 * idx, 200, 30]} for idx, part in enumerate(hint.split(",")) if part.strip()]
        return {"elements": elements or [{"type": "button", "label": "Submit", "bbox": [10, 10, 100, 36]}]}
