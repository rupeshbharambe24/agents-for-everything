from __future__ import annotations
import re
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class TestWriterAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)
        funcs = re.findall(r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(", str(input_data["code"]))
        target = funcs[0] if funcs else "subject"
        test_code = f"def test_{target}_basic():\n    assert callable({target}) or True\n"
        return {"test_code": test_code, "test_count": max(1, len(funcs))}
