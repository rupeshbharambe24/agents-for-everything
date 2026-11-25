"""Critic / Reflector implementation."""

from __future__ import annotations

from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation


class CriticAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)

        out = input_data["output"]
        text = str(out).strip()
        rubric = str(input_data["rubric"]).lower()
        fixes: list[str] = []
        if len(text) < 12:
            fixes.append("Output is too brief; expand with clear detail.")
        if "citation" in rubric and "http" not in text.lower() and "[" not in text:
            fixes.append("Rubric requires citations; include source references.")
        if "json" in rubric and not text.startswith("{"):
            fixes.append("Format response as valid JSON.")
        score = max(0.2, 1.0 - 0.35 * len(fixes))
        return {
            "score": round(score, 2),
            "critique": "Meets rubric criteria." if not fixes else "; ".join(fixes),
            "fixes": fixes,
            "passed": len(fixes) == 0,
        }
