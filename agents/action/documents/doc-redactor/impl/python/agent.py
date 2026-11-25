from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        res = runner.call_agent("guardrails/pii-redactor", {"text": input_data["text"]})
        return {"redacted_text": res["redacted_text"], "pii_found": res["pii_found"]}
