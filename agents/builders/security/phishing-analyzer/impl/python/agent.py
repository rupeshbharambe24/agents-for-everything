from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        low = str(input_data["email_text"]).lower()
        inds = []
        if "verify your password immediately" in low or "account suspended" in low:
            inds.append("urgency_credential_lure")
        if "http://" in low and "login" in low:
            inds.append("insecure_login_link")
        verdict = "phishing" if len(inds) >= 2 else ("suspicious" if inds else "safe")
        return {"verdict": verdict, "indicators": inds}
