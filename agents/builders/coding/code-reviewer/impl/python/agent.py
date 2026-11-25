from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

_BAD_CHECKS = [
    ("eval(", "high", "Avoid eval() on untrusted input"),
    ("exec(", "high", "Avoid exec() on dynamic strings"),
    ("sk-", "critical", "Possible hardcoded API key"),
    ("except:", "medium", "Avoid bare except blocks"),
    ("SELECT * FROM", "low", "Specify explicit SQL columns"),
]

class CodeReviewerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        diff = str(input_data["diff"])
        findings = [{"severity": sev, "message": msg} for pat, sev, msg in _BAD_CHECKS if pat in diff]
        return {"approved": len(findings) == 0, "findings": findings}
