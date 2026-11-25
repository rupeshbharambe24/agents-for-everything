"""Safety tier enforcement (S0-S4), PII masking, and budget guardrails."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable

from .models import AgentManifest

_PII_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"), "[REDACTED_EMAIL]"),
    (re.compile(r"\b(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{3,5}\)?[-.\s]?)?\d{3,5}[-.\s]?\d{4}\b"), "[REDACTED_PHONE]"),
    (re.compile(r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b"), "[REDACTED_ID_12]"),
    (re.compile(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"), "[REDACTED_PAN]"),
    (re.compile(r"\bsk-[A-Za-z0-9_-]{12,}\b"), "[REDACTED_API_KEY]"),
]


class SafetyViolation(RuntimeError):
    """Raised when an operation violates safety policy."""


class ApprovalRequiredError(SafetyViolation):
    """Raised when an S3/S4 or gated action requires human confirmation."""


class BudgetExceededError(SafetyViolation):
    """Raised when step, cost, or timeout limits are reached."""


@dataclass(slots=True)
class ApprovalRequest:
    """Payload describing an action awaiting human approval."""

    agent_id: str
    safety_level: str
    action: str
    summary: str


ApprovalHandler = Callable[[ApprovalRequest], bool]


def redact_pii(text: str) -> str:
    """Mask common emails, phone numbers, IDs, and API keys from log strings."""
    masked = text
    for pattern, replacement in _PII_PATTERNS:
        masked = pattern.sub(replacement, masked)
    return masked


class SafetyPolicy:
    """Runtime safety guard enforcing manifest safety tiers and resource limits."""

    def __init__(
        self,
        manifest: AgentManifest,
        auto_approve: bool = False,
        approval_handler: ApprovalHandler | None = None,
    ) -> None:
        self.manifest = manifest
        self.auto_approve = auto_approve
        self.approval_handler = approval_handler

    def check_tool_permission(self, tool_id: str, declared_tools: set[str]) -> None:
        """Ensure tools used at runtime were declared by the manifest."""
        if self.manifest.safety_level == "S0" and tool_id:
            raise SafetyViolation(
                f"Agent {self.manifest.id} is S0 (pure computation) and cannot call tool {tool_id!r}"
            )
        if declared_tools and tool_id not in declared_tools:
            raise SafetyViolation(
                f"Agent {self.manifest.id} attempted undeclared tool {tool_id!r}"
            )

    def require_approval(self, action: str, summary: str) -> bool:
        """Gate side effects declared in `approval_required_for` or S3/S4 policies."""
        needs_gate = (
            action in self.manifest.approval_required_for
            or self.manifest.safety_level in {"S3", "S4"}
        )
        if not needs_gate:
            return True
        if self.manifest.safety_level == "S4" and self.approval_handler is None and not self.auto_approve:
            raise ApprovalRequiredError(
                f"S4 agent {self.manifest.id} requires human approval for {action!r}: {summary}"
            )
        if self.auto_approve:
            return True
        if self.approval_handler is not None:
            approved = self.approval_handler(
                ApprovalRequest(
                    agent_id=self.manifest.id,
                    safety_level=self.manifest.safety_level,
                    action=action,
                    summary=summary,
                )
            )
            if not approved:
                raise ApprovalRequiredError(
                    f"Human rejected action {action!r} for agent {self.manifest.id}"
                )
            return True
        raise ApprovalRequiredError(
            f"Approval required for {self.manifest.id} action {action!r}: {summary}"
        )

    def enforce_limits(self, steps: int, elapsed_seconds: float, cost_usd: float) -> None:
        """Stop execution if step, timeout, or spend budgets are exceeded."""
        if steps > self.manifest.max_steps:
            raise BudgetExceededError(
                f"{self.manifest.id}: exceeded max_steps ({steps} > {self.manifest.max_steps})"
            )
        if elapsed_seconds > self.manifest.timeout_seconds:
            raise BudgetExceededError(
                f"{self.manifest.id}: exceeded timeout_seconds ({elapsed_seconds:.2f} > {self.manifest.timeout_seconds})"
            )
        if cost_usd > self.manifest.max_cost_usd and self.manifest.max_cost_usd > 0:
            raise BudgetExceededError(
                f"{self.manifest.id}: exceeded max_cost_usd ({cost_usd:.4f} > {self.manifest.max_cost_usd})"
            )
