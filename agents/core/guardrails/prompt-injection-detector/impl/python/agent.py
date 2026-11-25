"""Prompt Injection Detector implementation."""

from __future__ import annotations

import re
from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

_INJECTION_PATTERNS = [
    re.compile(r"ignore\s+(all\s+)?(previous|prior|above)\s+instructions?", re.I),
    re.compile(r"reveal\s+(the\s+)?system\s+prompt", re.I),
    re.compile(r"(exfiltrate|send|post)\s+(all\s+)?(secrets|tokens|api\s+keys|passwords)", re.I),
    re.compile(r"you\s+are\s+now\s+(in\s+)?developer\s+mode", re.I),
    re.compile(r"bypass\s+(safety|approval|gate)", re.I),
    re.compile(r"submit\s+immediately\s+without\s+confirmation", re.I),
]


class PromptInjectionDetectorAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        content = str(input_data["content"])
        spans: list[str] = []
        for pat in _INJECTION_PATTERNS:
            for m in pat.finditer(content):
                spans.append(m.group(0))
        risk = min(1.0, 0.45 * len(spans))
        return {"is_safe": len(spans) == 0, "risk_score": round(risk, 2), "spans": spans}
