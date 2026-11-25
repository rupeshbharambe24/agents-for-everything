from __future__ import annotations
import re
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

_PATTERNS = [("openai_key", re.compile(r"sk-[A-Za-z0-9_-]{12,}")), ("aws_key", re.compile(r"AKIA[0-9A-Z]{16}")), ("gh_pat", re.compile(r"ghp_[A-Za-z0-9]{20,}"))]

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        txt = str(input_data["text"])
        findings = []
        masked = txt
        for name, pat in _PATTERNS:
            if pat.search(masked):
                findings.append(name)
                masked = pat.sub(f"[MASKED_{name.upper()}]", masked)
        return {"has_secrets": bool(findings), "masked_text": masked, "findings": findings}
