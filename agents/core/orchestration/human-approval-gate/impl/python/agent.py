"""Human-in-the-loop approval gate implementation."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation


class HumanApprovalGateAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        action = str(input_data["action"])
        summary = str(input_data["summary"])
        user_resp = input_data.get("user_response")

        if user_resp in {"no", "reject"}:
            decision = "rejected"
        elif user_resp == "edit":
            decision = "needs_edit"
        elif user_resp in {"yes", "approve"}:
            decision = "approved"
        else:
            runner.require_approval("approve_action", f"{action}: {summary}")
            decision = "approved"

        return {
            "decision": decision,
            "audit_entry": {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "agent_id": runner.manifest.id,
                "action": action,
                "safety_level": input_data.get("safety_level", "S2"),
                "approved_by": "human" if decision == "approved" else "human_declined",
                "details": {"summary": summary},
            },
            "notes": f"Gate recorded decision={decision} for {action}",
        }
