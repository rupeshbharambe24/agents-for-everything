"""Supervisor composite agent orchestrating planner, router, and verifier."""

from __future__ import annotations

from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation


class SupervisorAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        plan = runner.call_agent("orchestration/task-planner", {"goal": input_data["goal"]})
        route = runner.call_agent("orchestration/router", {"request": input_data["goal"]})
        verdict = runner.call_agent(
            "orchestration/verifier",
            {"data": route, "required_fields": ["agent_id"]},
        )
        run_log = [
            f"Planned {len(plan.get('steps', []))} steps",
            f"Primary route selected: {route.get('agent_id')}",
            f"Verifier valid={verdict.get('valid')}",
        ]
        return {
            "results": [
                {"step": "plan", "output": plan},
                {"step": "route", "output": route},
                {"step": "verify", "output": verdict},
            ],
            "run_log": run_log,
            "status": "completed" if verdict.get("valid") else "partial",
        }
