from __future__ import annotations
import math
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class AgentImpl(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        vals = [float(x) for x in input_data["series"]]
        if len(vals) < 3:
            return {"anomaly_indices": [], "has_anomalies": False}
        mean = sum(vals) / len(vals)
        std = math.sqrt(sum((x - mean) ** 2 for x in vals) / len(vals))
        idx = [i for i, v in enumerate(vals) if std > 0 and abs(v - mean) > 1.8 * std]
        return {"anomaly_indices": idx, "has_anomalies": bool(idx)}
