from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class ReportWriterAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        topic = input_data["topic"]
        bullets = "\n".join(f"- {f}" for f in input_data.get("findings", []))
        refs = "\n".join(f"- {c.get('title', 'Source')}: {c.get('url', '')}" for c in input_data.get("citations", []))
        md = f"# {topic}\n\n## Executive Summary\nSynthesized report on {topic}.\n\n## Key Findings\n{bullets}\n\n## References\n{refs or '- Provided sources'}\n"
        return {"report_markdown": md, "section_count": 3}
