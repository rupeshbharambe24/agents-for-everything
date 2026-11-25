"""Reference implementation for healthcare/medical-evidence-agent."""

from __future__ import annotations

from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation


class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)
        runner.call_tool('afe/web-search', input_data)
        raw_text = str(input_data.get("input", "")).strip()
        locale = str(input_data.get("locale") or runner.context.locale or "en")
        inj = any(tok in raw_text.lower() for tok in ("ignore previous", "ignore all previous", "override", "bypass"))
        status = "flagged_injection" if inj else ("ok" if raw_text else "empty_input")
        summary = raw_text[:160] if raw_text else "No input supplied"
        out: dict[str, Any] = {
            "result": f"[healthcare/medical-evidence-agent] {summary}",
            "items": [{"agent": 'healthcare/medical-evidence-agent', "category": 'healthcare', "summary": summary, "locale": locale}],
            "confidence": 0.91 if raw_text else 0.4,
            "status": status,
            "locale": locale,
        }
        out["disclaimer"] = 'Clinical workflow aid for licensed professionals only; outputs are unapproved drafts requiring clinician review and never replace medical judgement.'
        return out
