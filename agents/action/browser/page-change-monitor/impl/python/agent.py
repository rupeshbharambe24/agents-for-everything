from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        prev = str(input_data["previous_text"]).strip()
        curr = str(input_data["current_text"]).strip()
        changed = prev != curr
        return {"changed": changed, "summary": "Page content changed." if changed else "No change detected."}
