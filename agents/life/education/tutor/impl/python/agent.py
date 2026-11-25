from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        topic = str(input_data["topic"])
        attempt = str(input_data.get("learner_attempt", "")).strip()
        q = f"What key principle in {topic} connects to '{attempt or 'the problem'}'?"
        return {"guiding_question": q, "hint": f"Break {topic} into smaller base cases first."}
