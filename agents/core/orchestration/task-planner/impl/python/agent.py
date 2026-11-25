"""Task Planner implementation."""

from __future__ import annotations

from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation


class TaskPlannerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)

        goal = str(input_data["goal"]).lower()
        steps: list[dict[str, Any]] = []
        if "research" in goal or "report" in goal:
            steps = [
                {"id": "s1", "action": "Search authoritative sources", "agent_id": "search/web-search", "depends_on": [], "success_criteria": "Relevant URLs retrieved"},
                {"id": "s2", "action": "Read and extract evidence", "agent_id": "research/source-reader", "depends_on": ["s1"], "success_criteria": "Key facts with citations"},
                {"id": "s3", "action": "Verify claims and draft report", "agent_id": "research/report-writer", "depends_on": ["s2"], "success_criteria": "Cited report generated"},
            ]
        elif "voice" in goal and "form" in goal:
            steps = [
                {"id": "s1", "action": "Transcribe spoken utterance", "agent_id": "voice/speech-to-text", "depends_on": [], "success_criteria": "Clean transcript produced"},
                {"id": "s2", "action": "Map text into form schema", "agent_id": "text/structured-extractor", "depends_on": ["s1"], "success_criteria": "Fields normalized"},
                {"id": "s3", "action": "Verify fields and confirm", "agent_id": "orchestration/verifier", "depends_on": ["s2"], "success_criteria": "All required fields valid"},
            ]
        else:
            steps = [
                {"id": "s1", "action": "Route request to specialist", "agent_id": "orchestration/router", "depends_on": [], "success_criteria": "Target agent identified"},
                {"id": "s2", "action": "Execute primary task", "agent_id": "text/summarizer", "depends_on": ["s1"], "success_criteria": "Task output generated"},
                {"id": "s3", "action": "Verify output contract", "agent_id": "orchestration/verifier", "depends_on": ["s2"], "success_criteria": "Schema valid"},
            ]
        return {"steps": steps, "estimated_cost_usd": round(0.01 * len(steps), 3)}
