from __future__ import annotations
import json
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class DataCleanerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        seen: set[str] = set()
        cleaned = []
        dupes = 0
        for row in input_data.get("rows", []):
            norm = {k: (v.strip() if isinstance(v, str) else v) for k, v in row.items()}
            sig = json.dumps(norm, sort_keys=True)
            if sig in seen:
                dupes += 1
            else:
                seen.add(sig)
                cleaned.append(norm)
        return {"cleaned_rows": cleaned, "removed_duplicates": dupes}
