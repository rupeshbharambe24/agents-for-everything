from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class TextToSQLAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        q = str(input_data["question"]).lower()
        if any(bad in q for bad in ("drop table", "delete from", "truncate", "insert into")):
            raise ValueError("Refused non-read-only SQL intent")
        tables = list((input_data.get("tables") or {"events": ["id"]}).keys())
        table = tables[0] if tables else "events"
        if "count" in q or "how many" in q:
            sql = f"SELECT COUNT(*) AS total FROM {table};"
        else:
            cols = ", ".join((input_data.get("tables") or {}).get(table, ["id"])[:5])
            sql = f"SELECT {cols} FROM {table} LIMIT 50;"
        return {"sql": sql, "read_only": True}
