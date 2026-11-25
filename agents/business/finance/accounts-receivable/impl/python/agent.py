"""Reference implementation for finance/accounts-receivable."""

from __future__ import annotations

from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation


class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)
        if input_data.get("execute"):
            runner.require_approval('approve_external_action', "Confirm finance/accounts-receivable action")
        runner.call_tool('afe/email', input_data)
        raw_text = str(input_data.get("input", "")).strip()
        locale = str(input_data.get("locale") or runner.context.locale or "en")
        inj = any(tok in raw_text.lower() for tok in ("ignore previous", "ignore all previous", "override", "bypass"))
        status = "approved" if input_data.get("execute") else ("flagged_injection" if inj else "draft_ready")
        summary = raw_text[:160] if raw_text else "No input supplied"
        out: dict[str, Any] = {
            "result": f"[finance/accounts-receivable] {summary}",
            "items": [{"agent": 'finance/accounts-receivable', "category": 'finance', "summary": summary, "locale": locale}],
            "confidence": 0.91 if raw_text else 0.4,
            "status": status,
            "locale": locale,
        }
        out["disclaimer"] = 'Accounting/tax workflow assistant; does not provide regulated investment advice and requires human finance sign-off for ledger postings.'
        return out
