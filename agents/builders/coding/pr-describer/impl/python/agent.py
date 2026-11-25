from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        diff = str(input_data["diff"])
        added = sum(1 for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++"))
        removed = sum(1 for l in diff.splitlines() if l.startswith("-") and not l.startswith("---"))
        kind = "fix" if "fix" in diff.lower() else "feat"
        return {"title": f"{kind}: update module (+{added}/-{removed} lines)", "summary": f"Modified {added + removed} diff lines.", "changelog": [f"Updated implementation (+{added}/-{removed})"]}
