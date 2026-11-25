from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

_RULES = [("pickle.loads", "Insecure pickle deserialization"), ("shell=True", "Command injection risk via shell=True"), ("yaml.load(", "Use yaml.safe_load instead of yaml.load"), ("md5(", "Weak MD5 hash for security context")]

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        code = str(input_data["code"])
        issues = [msg for pat, msg in _RULES if pat in code]
        return {"vulnerable": bool(issues), "issues": issues}
