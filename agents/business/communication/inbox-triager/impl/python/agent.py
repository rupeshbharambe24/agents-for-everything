from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class InboxTriagerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        triaged = []
        urgent = 0
        for mail in input_data.get("emails", []):
            subj = str(mail.get("subject", ""))
            body = str(mail.get("body", ""))
            txt = f"{subj} {body}".lower()
            if any(k in txt for k in ("urgent", "asap", "outage", "deadline today")):
                label, prio = "urgent", 1
                urgent += 1
            elif "?" in txt or "please" in txt:
                label, prio = "action_required", 2
            else:
                label, prio = "fyi", 3
            triaged.append({"id": mail.get("id", ""), "subject": subj, "label": label, "priority": prio})
        triaged.sort(key=lambda x: x["priority"])
        return {"triaged": triaged, "urgent_count": urgent}
