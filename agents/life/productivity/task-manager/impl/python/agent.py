from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class TaskManagerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        ext = runner.call_agent("meetings/action-item-extractor", {"text": input_data["notes"]})
        tasks = ext.get("tasks", [])
        if not tasks:
            tasks = [{"id": "task-1", "title": str(input_data["notes"]).strip(), "priority": "medium", "status": "todo"}]
        return {"tasks": tasks, "top_focus": tasks[0]["title"]}
