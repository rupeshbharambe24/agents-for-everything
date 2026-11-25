from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        req = str(input_data["request"]).strip()
        vague = len(req.split()) < 4 or any(w in req.lower() for w in ("something", "stuff", "help me", "do it"))
        qs = ["What specific output format or target do you need?"] if vague else []
        return {"needs_clarification": vague, "questions": qs, "refined_request": req}
