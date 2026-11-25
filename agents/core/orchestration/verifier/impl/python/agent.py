"""Deterministic Output Verifier supporting field rules and Indian/global formats."""

from __future__ import annotations

import re
from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

_FORMAT_PATTERNS: dict[str, tuple[re.Pattern[str], str]] = {
    "email": (re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"), "Invalid email format"),
    "pincode": (re.compile(r"^[1-9][0-9]{5}$"), "PIN code must be 6 digits"),
    "ifsc": (re.compile(r"^[A-Z]{4}0[A-Z0-9]{6}$"), "Invalid IFSC code"),
    "dob": (re.compile(r"^\d{4}-\d{2}-\d{2}$"), "Date must be YYYY-MM-DD"),
    "phone": (re.compile(r"^(\+?\d{1,3}[-\s]?)?\d{10}$"), "Phone must have 10 digits"),
}


class VerifierAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        data: dict[str, Any] = input_data.get("data", {})
        required = list(input_data.get("required_fields", []))
        rules: dict[str, Any] = input_data.get("rules", {})

        missing: list[str] = []
        invalid: list[dict[str, Any]] = []
        reasons: list[str] = []

        for req in required:
            val = data.get(req)
            if val is None or val == "" or val == []:
                missing.append(req)
                reasons.append(f"Missing required field '{req}'")

        for key, val in data.items():
            if val in (None, ""):
                continue
            rule = rules.get(key, {})
            fmt = rule.get("format") or (key if key in _FORMAT_PATTERNS else None)
            if fmt and fmt in _FORMAT_PATTERNS:
                pat, msg = _FORMAT_PATTERNS[fmt]
                if not pat.match(str(val).strip()):
                    invalid.append({"field": key, "code": f"invalid_{fmt}", "message": msg, "value": val})
                    reasons.append(f"{key}: {msg}")
            if "pattern" in rule:
                if not re.match(str(rule["pattern"]), str(val)):
                    msg = f"Does not match pattern {rule['pattern']}"
                    invalid.append({"field": key, "code": "pattern_mismatch", "message": msg, "value": val})
                    reasons.append(f"{key}: {msg}")
            if "min" in rule and isinstance(val, (int, float)) and val < rule["min"]:
                msg = f"Value {val} below minimum {rule['min']}"
                invalid.append({"field": key, "code": "min_value", "message": msg, "value": val})
                reasons.append(f"{key}: {msg}")

        return {
            "valid": len(missing) == 0 and len(invalid) == 0,
            "missing": missing,
            "invalid": invalid,
            "reasons": reasons,
        }
