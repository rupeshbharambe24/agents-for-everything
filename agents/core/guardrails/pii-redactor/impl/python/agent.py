"""Reversible PII Redactor supporting global and Indian PII patterns."""

from __future__ import annotations

import re
from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("email", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("pan", re.compile(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b")),
    ("aadhaar", re.compile(r"\b[2-9]\d{3}[\s-]?\d{4}[\s-]?\d{4}\b")),
    ("ssn", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
    ("phone", re.compile(r"\b(?:\+?91[-\s]?)?[6-9]\d{9}\b|\b\+?1[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b")),
]


class PIIRedactorAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        text = str(input_data["text"])
        redacted = text
        rmap: dict[str, str] = {}
        found: list[str] = []
        counter = 0

        for label, pat in _PATTERNS:
            def _repl(match: re.Match[str], lbl: str = label) -> str:
                nonlocal counter
                counter += 1
                tok = f"[{lbl.upper()}_{counter}]"
                rmap[tok] = match.group(0)
                if lbl not in found:
                    found.append(lbl)
                return tok
            redacted = pat.sub(_repl, redacted)

        return {"redacted_text": redacted, "redaction_map": rmap, "pii_found": found}
