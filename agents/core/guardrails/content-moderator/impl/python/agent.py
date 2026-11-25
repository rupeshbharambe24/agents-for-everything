"""Content Moderator implementation."""

from __future__ import annotations

from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

_BLOCK_TERMS = {
    "malware": ("ransomware", "credential harvester", "keylogger", "exploit payload"),
    "self_harm": ("how to hurt myself", "commit suicide"),
    "bypass": ("bypass captcha", "crack password"),
}


class ContentModeratorAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        low = str(input_data["content"]).lower()
        labels = [lbl for lbl, terms in _BLOCK_TERMS.items() if any(t in low for t in terms)]
        allowed = len(labels) == 0
        return {"allowed": allowed, "labels": labels, "action": "allow" if allowed else "block"}
