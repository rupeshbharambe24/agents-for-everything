"""Tests covering all 6 Python framework adapters against real catalog agents."""

import unittest
from pathlib import Path

from agents_for_everything import AgentRunner, RunContext
from packages.adapters import (
    as_claude_subagent,
    as_crewai_agent_spec,
    as_google_adk_agent_spec,
    as_langgraph_node,
    as_ms_agent_config,
    as_openai_agent_spec,
)


class FrameworkAdaptersTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(__file__).resolve().parents[3]
        self.ctx = RunContext(provider_name="mock")
        self.payload = {"text": "Agents for Everything builds composable AI agents."}

    def test_langgraph_adapter(self) -> None:
        node = as_langgraph_node("text/summarizer", runner=AgentRunner(repo_root=self.root), context=self.ctx)
        out = node(self.payload)
        self.assertIn("summary", out)
        self.assertIn("key_points", out)

    def test_openai_agents_adapter(self) -> None:
        spec = as_openai_agent_spec("text/summarizer", repo_root=self.root, context=self.ctx)
        self.assertEqual(spec["metadata"]["id"], "text/summarizer")
        out = spec["afe_tool"](self.payload)
        self.assertIn("summary", out)

    def test_claude_agent_sdk_adapter(self) -> None:
        sub = as_claude_subagent("text/summarizer", repo_root=self.root, context=self.ctx)
        self.assertEqual(sub["name"], "summarizer")
        out = sub["run"](self.payload)
        self.assertIn("summary", out)

    def test_google_adk_adapter(self) -> None:
        spec = as_google_adk_agent_spec("text/summarizer", repo_root=self.root, context=self.ctx)
        self.assertEqual(spec["a2a_id"], "text/summarizer")
        out = spec["tools"][0](self.payload)
        self.assertIn("summary", out)

    def test_ms_agent_framework_adapter(self) -> None:
        cfg = as_ms_agent_config("text/summarizer", repo_root=self.root, context=self.ctx)
        out = cfg["handler"](self.payload)
        self.assertIn("summary", out)

    def test_crewai_adapter(self) -> None:
        spec = as_crewai_agent_spec("text/summarizer", repo_root=self.root, context=self.ctx)
        out = spec["tools"][0](self.payload)
        self.assertIn("summary", out)


if __name__ == "__main__":
    unittest.main()
