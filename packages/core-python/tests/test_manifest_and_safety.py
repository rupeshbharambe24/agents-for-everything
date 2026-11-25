"""Tests for SafetyPolicy, PII redaction, and schema compatibility."""

import json
import tempfile
import unittest
from pathlib import Path

from agents_for_everything.manifest import check_schema_compatibility
from agents_for_everything.models import AgentManifest
from agents_for_everything.safety import (
    ApprovalRequiredError,
    BudgetExceededError,
    SafetyPolicy,
    SafetyViolation,
    redact_pii,
)


def _dummy_manifest(safety_level: str = "S2") -> AgentManifest:
    return AgentManifest(
        id="test/agent",
        name="Test Agent",
        version="0.1.0",
        family="core",
        category="orchestration",
        tier="atomic",
        maturity="spec",
        priority="P0",
        license="Apache-2.0",
        summary="Test summary",
        purpose="Test purpose",
        pattern="augmented-llm",
        autonomy="L2",
        input_schema_path="schemas/input.schema.json",
        output_schema_path="schemas/output.schema.json",
        safety_level=safety_level,
        approval_required_for=["submit"] if safety_level in {"S2", "S3", "S4"} else [],
        max_steps=3,
        timeout_seconds=10.0,
        max_cost_usd=0.05,
    )


class SafetyAndCompatTests(unittest.TestCase):
    def test_pii_redaction_masks_sensitive_tokens(self) -> None:
        raw = "Email rupesh@example.com phone +91-9876543210 key sk-1234567890abcdef"
        masked = redact_pii(raw)
        self.assertNotIn("rupesh@example.com", masked)
        self.assertNotIn("9876543210", masked)
        self.assertNotIn("sk-1234567890abcdef", masked)

    def test_s0_forbids_tools(self) -> None:
        policy = SafetyPolicy(_dummy_manifest("S0"))
        with self.assertRaises(SafetyViolation):
            policy.check_tool_permission("afe/web-search", {"afe/web-search"})

    def test_s4_requires_approval(self) -> None:
        policy = SafetyPolicy(_dummy_manifest("S4"), auto_approve=False)
        with self.assertRaises(ApprovalRequiredError):
            policy.require_approval("submit", "Submit wire transfer")

        approved_policy = SafetyPolicy(
            _dummy_manifest("S4"),
            approval_handler=lambda req: req.action == "submit",
        )
        self.assertTrue(approved_policy.require_approval("submit", "Approved action"))

    def test_budget_limits_enforced(self) -> None:
        policy = SafetyPolicy(_dummy_manifest("S1"))
        with self.assertRaises(BudgetExceededError):
            policy.enforce_limits(steps=4, elapsed_seconds=1.0, cost_usd=0.0)
        with self.assertRaises(BudgetExceededError):
            policy.enforce_limits(steps=1, elapsed_seconds=1.0, cost_usd=0.10)

    def test_schema_compatibility_check(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            types_dir = Path(tmp)
            out_s = {"type": "object", "properties": {"text": {"type": "string"}}}
            in_s = {
                "type": "object",
                "required": ["text"],
                "properties": {"text": {"type": "string"}},
            }
            ok, reasons = check_schema_compatibility(out_s, in_s, types_dir)
            self.assertTrue(ok, reasons)

            bad_in = {
                "type": "object",
                "required": ["missing_field"],
                "properties": {"missing_field": {"type": "string"}},
            }
            ok2, _ = check_schema_compatibility(out_s, bad_in, types_dir)
            self.assertFalse(ok2)


if __name__ == "__main__":
    unittest.main()
