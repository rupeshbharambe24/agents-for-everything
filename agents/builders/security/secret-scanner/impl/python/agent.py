from __future__ import annotations
import re
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

_SECRETS = [("github_pat", re.compile(r"ghp_[A-Za-z0-9]{16,}")), ("private_key", re.compile(r"-----BEGIN .*PRIVATE KEY-----")), ("api_key", re.compile(r"sk-[A-Za-z0-9_-]{12,}"))]

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        txt = str(input_data["content"])
        matches = [name for name, pat in _SECRETS if pat.search(txt)]
        return {"leaked": bool(matches), "matches": matches}
