"""Memory Writer implementation."""

from __future__ import annotations

from typing import Any

from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation


class MemoryWriterAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)

        text = str(input_data["interaction"]).strip()
        existing = {e.strip().lower() for e in input_data.get("existing", [])}
        sentences = [s.strip() for s in text.replace(";", ".").split(".") if len(s.strip()) > 3]
        records: list[dict[str, Any]] = []
        skipped = 0
        for s in sentences:
            low = s.lower()
            if low in existing:
                skipped += 1
                continue
            kind = "preference" if any(k in low for k in ("prefer", "always", "like", "language")) else "fact"
            records.append({"kind": kind, "content": s, "confidence": 0.9})
            existing.add(low)
        return {"records": records, "skipped_duplicates": skipped}
