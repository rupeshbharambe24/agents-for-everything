from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class DeepResearcherAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        topic = input_data["topic"]
        search_res = runner.call_agent("search/web-search", {"query": topic})
        findings = []
        citations = []
        for idx, item in enumerate(search_res.get("results", [])[:3], start=1):
            notes = runner.call_agent("research/source-reader", {"url": item["url"], "content": item.get("snippet", "")})
            findings.extend(notes.get("key_points", []))
            citations.append({"source_id": str(idx), "title": item["title"], "url": item["url"], "quote": notes["summary"]})
        fc = runner.call_agent("research/fact-checker", {"claims": findings[:2] or [topic]})
        rep = runner.call_agent("research/report-writer", {"topic": topic, "findings": findings, "citations": citations})
        return {"report_markdown": rep["report_markdown"], "citations": citations, "verified_claims": len(fc.get("verdicts", []))}
