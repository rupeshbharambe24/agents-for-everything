"""Memory Retriever implementation."""

from __future__ import annotations

import re
from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation


class MemoryRetrieverAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        query = str(input_data["query"]).lower()
        q_terms = {t for t in re.findall(r"[a-z0-9]+", query) if len(t) > 2}
        top_k = int(input_data.get("top_k", 5))
        seen: set[str] = set()
        scored: list[dict[str, Any]] = []
        for mem in input_data.get("memories", []):
            norm = str(mem).strip()
            if not norm or norm.lower() in seen:
                continue
            seen.add(norm.lower())
            m_terms = set(re.findall(r"[a-z0-9]+", norm.lower()))
            overlap = len(q_terms & m_terms)
            if overlap > 0:
                scored.append({"content": norm, "score": round(overlap / max(1, len(q_terms)), 2)})
        scored.sort(key=lambda x: x["score"], reverse=True)
        return {"matches": scored[:top_k]}
