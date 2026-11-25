from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if not input_data.get("user_consent"):
            raise PermissionError("Consented KYC verification required before reading ID documents")
        runner.require_approval("verified_user_consent", "Read consented KYC ID document")
        ocr = runner.call_tool("afe/ocr", {"image": input_data["image"]})
        return {"fields": {"raw_text": ocr.get("text", "")}, "status": "extracted_consented"}
