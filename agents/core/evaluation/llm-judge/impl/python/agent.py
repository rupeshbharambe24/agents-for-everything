"""LLM Judge implementation."""

from __future__ import annotations

from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation


class LLMJudgeAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)

        out = str(input_data["output"]).strip()
        req_terms = [str(t).lower() for t in input_data.get("required_terms", [])]
        if not out:
            return {"passed": False, "score": 0.0, "reason": "Empty output", "breakdown": {"completeness": 0.0}}
        hits = sum(1 for t in req_terms if t in out.lower())
        term_score = hits / len(req_terms) if req_terms else 1.0
        length_score = 1.0 if len(out) >= 15 else 0.5
        score = round(0.7 * term_score + 0.3 * length_score, 2)
        passed = score >= 0.75
        return {
            "passed": passed,
            "score": score,
            "reason": "Passed rubric criteria." if passed else "Missing required rubric elements.",
            "breakdown": {"required_terms": round(term_score, 2), "completeness": length_score},
        }
