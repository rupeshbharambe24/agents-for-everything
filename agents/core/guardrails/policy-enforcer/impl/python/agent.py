from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        action = str(input_data["action"]).lower()
        denies = {str(d).lower() for d in input_data.get("deny_list", ["drop_db", "exfiltrate", "rm_rf"])}
        if any(d in action for d in denies):
            return {"decision": "deny", "reason": f"Matched deny rule for {action}"}
        if any(w in action for w in ("send", "submit", "pay", "delete")):
            return {"decision": "approve", "reason": "External/mutating action requires human approval"}
        return {"decision": "allow", "reason": "Permitted read-only or safe action"}
