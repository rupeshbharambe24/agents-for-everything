from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class DataAnalystAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        cleaned = runner.call_agent("data/data-cleaner", {"rows": input_data["rows"]})
        metric = str(input_data["metric"])
        vals = [float(r[metric]) for r in cleaned["cleaned_rows"] if metric in r and isinstance(r[metric], (int, float))]
        if not vals:
            return {"count": 0, "mean": 0.0, "min": 0.0, "max": 0.0, "insight": f"No numeric values for {metric}."}
        mn, mx, avg = min(vals), max(vals), round(sum(vals) / len(vals), 2)
        return {"count": len(vals), "mean": avg, "min": mn, "max": mx, "insight": f"{metric}: n={len(vals)}, avg={avg}, range=[{mn}, {mx}]."}
