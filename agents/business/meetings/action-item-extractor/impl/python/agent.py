from __future__ import annotations
import re
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class ActionItemExtractorAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        lines = [s.strip() for s in re.split(r"[\n.]+", str(input_data["text"])) if s.strip()]
        tasks = []
        for idx, line in enumerate(lines, start=1):
            if any(k in line.lower() for k in ("will ", "todo", "action:", "by ", "assign", "need to")):
                owner_m = re.match(r"^([A-Z][a-z]+)\s+will\b", line)
                tasks.append({"id": f"task-{idx}", "title": line, "owner": owner_m.group(1) if owner_m else "unassigned", "priority": "medium", "status": "todo"})
        return {"tasks": tasks}
