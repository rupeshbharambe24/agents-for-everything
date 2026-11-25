from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class CodeGeneratorAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        code = f'def implement_feature(payload: dict) -> dict:\n    """{input_data["spec"]}"""\n    return {{"status": "ok", "payload": payload}}\n'
        tests = runner.call_agent("coding/test-writer", {"code": code})
        return {"code": code, "tests": tests["test_code"]}
