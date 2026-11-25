from __future__ import annotations
from collections import Counter
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class LogAnalyzerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        err_lines = [l.strip() for l in str(input_data["logs"]).splitlines() if any(lvl in l.upper() for lvl in ("ERROR", "CRITICAL", "EXCEPTION"))]
        counts = Counter(err_lines)
        clusters = [{"message": msg, "count": cnt} for msg, cnt in counts.most_common(10)]
        return {"error_count": len(err_lines), "clusters": clusters}
