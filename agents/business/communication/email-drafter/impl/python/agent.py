from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class EmailDrafterAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        subj = str(input_data.get("subject") or f"Re: {str(input_data['intent'])[:40]}")
        body = f"Hi {input_data['recipient']},\n\n{input_data['intent']}\n\nBest regards,"
        if input_data.get("send"):
            runner.require_approval("send", f"Send email to {input_data['recipient']}: {subj}")
            return {"subject": subj, "body": body, "status": "sent"}
        runner.call_tool("afe/email", {"subject": subj, "body": body})
        return {"subject": subj, "body": body, "status": "draft_saved"}
