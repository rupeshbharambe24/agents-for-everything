from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class SpreadsheetAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        col = str(input_data["column"])
        op = str(input_data.get("operation", "sum"))
        nums = [float(r[col]) for r in input_data.get("rows", []) if col in r and isinstance(r[col], (int, float))]
        if op == "count":
            val = float(len(nums))
        elif op == "avg":
            val = round(sum(nums) / len(nums), 2) if nums else 0.0
        elif op == "max":
            val = max(nums) if nums else 0.0
        else:
            val = round(sum(nums), 2)
        return {"operation": op, "column": col, "value": val}
