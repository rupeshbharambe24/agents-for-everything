from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class TableExtractorAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        lines = [l.strip() for l in str(input_data["text"]).splitlines() if "|" in l]
        if len(lines) < 2:
            return {"headers": [], "rows": []}
        headers = [h.strip() for h in lines[0].strip("|").split("|")]
        rows = []
        for line in lines[1:]:
            if set(line.replace("|", "").replace("-", "").strip()) == set():
                continue
            vals = [v.strip() for v in line.strip("|").split("|")]
            rows.append(dict(zip(headers, vals)))
        return {"headers": headers, "rows": rows}
