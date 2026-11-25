"""Tests for AgentRunner, TeamRunner, and exporters."""

import json
import tempfile
import unittest
from pathlib import Path

from agents_for_everything.exporters import export_agent
from agents_for_everything.models import RunContext
from agents_for_everything.runner import AgentRunner
from agents_for_everything.team_runner import evaluate_condition


def _write_sample_agent(root: Path, slug: str = "echo-agent") -> Path:
    agent_dir = root / "agents" / "core" / "orchestration" / slug
    (agent_dir / "prompts").mkdir(parents=True)
    (agent_dir / "schemas").mkdir(parents=True)
    (agent_dir / "evals").mkdir(parents=True)
    (agent_dir / "agent.yaml").write_text(
        f"""apiVersion: afe/v1
kind: Agent
metadata:
  id: orchestration/{slug}
  name: Echo Agent
  version: 0.1.0
  family: core
  category: orchestration
  tier: atomic
  maturity: spec
  priority: P0
  license: Apache-2.0
spec:
  summary: Echoes normalized text.
  purpose: Simple test agent for runner validation.
  pattern: augmented-llm
  autonomy: L1
  io:
    input: schemas/input.schema.json
    output: schemas/output.schema.json
  model:
    capabilities: [structured_output]
  safety:
    level: S0
  limits:
    max_steps: 5
    timeout_seconds: 10
    max_cost_usd: 0.01
  evals:
    suite: evals/eval.yaml
""",
        encoding="utf-8",
    )
    (agent_dir / "README.md").write_text("# Echo Agent\n", encoding="utf-8")
    (agent_dir / "prompts" / "system.md").write_text("Return JSON matching schema.", encoding="utf-8")
    (agent_dir / "schemas" / "input.schema.json").write_text(
        json.dumps(
            {
                "type": "object",
                "required": ["text"],
                "properties": {"text": {"type": "string"}},
            }
        ),
        encoding="utf-8",
    )
    (agent_dir / "schemas" / "output.schema.json").write_text(
        json.dumps(
            {
                "type": "object",
                "required": ["text"],
                "properties": {"text": {"type": "string"}},
            }
        ),
        encoding="utf-8",
    )
    (agent_dir / "tools.yaml").write_text("apiVersion: afe/v1\nkind: Tools\nservers: []\n", encoding="utf-8")
    (agent_dir / "evals" / "eval.yaml").write_text("metrics: [exact_match]\n", encoding="utf-8")
    (agent_dir / "evals" / "cases.jsonl").write_text("", encoding="utf-8")
    (agent_dir / "evals" / "rubric.md").write_text("# Rubric\n", encoding="utf-8")
    (agent_dir / "CHANGELOG.md").write_text("# Changelog\n", encoding="utf-8")
    return agent_dir


class RunnerAndExporterTests(unittest.TestCase):
    def test_runner_executes_generic_manifest_and_exports(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "spec").mkdir()
            (root / "spec" / "agent.schema.json").write_text("{}", encoding="utf-8")
            (root / "spec" / "types").mkdir()
            agent_dir = _write_sample_agent(root)

            runner = AgentRunner(repo_root=root)
            res = runner.run(
                "orchestration/echo-agent",
                {"text": "hello agents"},
                context=RunContext(provider_name="mock"),
            )
            self.assertEqual(res.status, "ok")
            self.assertEqual(res.output["text"], "hello agents")
            self.assertGreaterEqual(len(res.trace), 2)

            out_dir = root / "exports"
            for target in ("a2a", "skill", "mcp-server", "subagent", "langgraph"):
                files = export_agent(agent_dir, target, out_dir)
                self.assertTrue(all(f.exists() for f in files), f"Missing export for {target}")

    def test_team_condition_evaluator_safe(self) -> None:
        self.assertTrue(evaluate_condition("unsupported_claims > 0", {"unsupported_claims": 2}))
        self.assertFalse(evaluate_condition("unsupported_claims > 0", {"unsupported_claims": 0}))
        self.assertTrue(evaluate_condition("approved == true", {"approved": True}))
        self.assertFalse(evaluate_condition("__import__('os').system('ls')", {}))


if __name__ == "__main__":
    unittest.main()
