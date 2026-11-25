from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class BugFixerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        patch = str(input_data["code"]).replace("eval(", "ast.literal_eval(")
        runner.call_agent("coding/test-writer", {"code": patch})
        rev = runner.call_agent("coding/code-reviewer", {"diff": patch})
        return {"root_cause": f"Diagnosed: {input_data['issue']}", "patch": patch, "review_passed": bool(rev.get("approved", False))}
