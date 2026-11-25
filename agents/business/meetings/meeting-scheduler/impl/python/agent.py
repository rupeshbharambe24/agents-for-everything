from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class MeetingSchedulerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        slots = input_data.get("candidate_slots", [])
        chosen = str(slots[0]) if slots else "TBD"
        runner.call_tool("afe/calendar", {"slots": slots})
        if input_data.get("confirm"):
            runner.require_approval("send_invite", f"Send invite '{input_data['title']}' at {chosen}")
            runner.call_agent("communication/email-drafter", {"recipient": ", ".join(input_data["attendees"]), "subject": input_data["title"], "intent": f"Calendar invite for {chosen}"})
            return {"selected_slot": chosen, "status": "invite_sent"}
        return {"selected_slot": chosen, "status": "slots_proposed"}
