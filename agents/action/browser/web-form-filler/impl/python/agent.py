from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class WebFormFillerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        res = runner.call_tool("afe/browser", {"action": "fill", "url": input_data["url"], "fields": input_data["fields"]})
        if input_data.get("submit"):
            runner.require_approval("submit", f"Submit web form at {input_data['url']}")
            return {"filled_fields": res.get("filled_fields", {}), "submitted": True, "status": "submitted"}
        return {"filled_fields": res.get("filled_fields", {}), "submitted": False, "status": "awaiting_confirmation"}
