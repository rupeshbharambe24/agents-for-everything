from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        cost = float(input_data["cost_usd"])
        cap = float(input_data["max_cost_usd"])
        if cost >= cap:
            dec = "stop"
        elif cost >= cap * 0.8:
            dec = "throttle"
        else:
            dec = "allow"
        return {"decision": dec, "remaining_usd": round(max(0.0, cap - cost), 4)}
