"""Eval runner for executing evals/cases.jsonl against afe/v1 agents."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from agents_for_everything import AgentRunner, RunContext, discover_agents, find_repo_root
from agents_for_everything.models import EvalCase, EvalSummary


def load_eval_cases(cases_path: Path) -> list[EvalCase]:
    """Load JSONL evaluation fixtures from `evals/cases.jsonl`."""
    cases: list[EvalCase] = []
    for line in cases_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        raw = json.loads(line)
        cases.append(
            EvalCase(
                id=str(raw["id"]),
                input=dict(raw["input"]),
                expected=dict(raw.get("expected", {})),
                tags=list(raw.get("tags", [])),
                locale=str(raw.get("locale", "en")),
                raw=raw,
            )
        )
    return cases


def _matches_expected(actual: Any, expected: Any, path: str = "$") -> list[str]:
    mismatches: list[str] = []
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            return [f"{path}: expected object, got {type(actual).__name__}"]
        for k, v in expected.items():
            if k not in actual:
                mismatches.append(f"{path}.{k}: missing key")
            else:
                mismatches.extend(_matches_expected(actual[k], v, f"{path}.{k}"))
        return mismatches
    if isinstance(expected, list):
        if not isinstance(actual, list):
            return [f"{path}: expected array, got {type(actual).__name__}"]
        for item in expected:
            if item not in actual:
                mismatches.append(f"{path}: missing expected item {item!r}")
        return mismatches
    if isinstance(expected, float) and isinstance(actual, (int, float)):
        if abs(float(actual) - expected) > 1e-4:
            mismatches.append(f"{path}: {actual} != {expected}")
        return mismatches
    if actual != expected:
        mismatches.append(f"{path}: {actual!r} != {expected!r}")
    return mismatches


def evaluate_agent(
    agent_ref: str | Path,
    repo_root: Path | None = None,
    provider_name: str = "mock",
    model: str | None = None,
) -> EvalSummary:
    """Run all eval cases for an agent and compute pass/fail summary."""
    root = (repo_root or find_repo_root()).resolve()
    if isinstance(agent_ref, Path) or (
        isinstance(agent_ref, str) and (Path(agent_ref) / "agent.yaml").exists()
    ):
        agent_dir = Path(agent_ref).resolve()
        agent_id = agent_dir.parent.name + "/" + agent_dir.name
    else:
        agents = discover_agents(root)
        if agent_ref not in agents:
            raise KeyError(f"Agent not found: {agent_ref!r}")
        manifest = agents[agent_ref]
        assert manifest.directory is not None
        agent_dir = manifest.directory
        agent_id = manifest.id

    cases = load_eval_cases(agent_dir / "evals" / "cases.jsonl")
    runner = AgentRunner(repo_root=root)
    passed = 0
    failures: list[dict[str, Any]] = []

    if provider_name == "mock":
        # Cases marked "live_only": true need a real model (e.g. new languages the offline mode can't parse).
        cases = [c for c in cases if not c.raw.get("live_only")]

    for case in cases:
        expect_error = case.raw.get("expect_error")
        auto_approve = bool(case.raw.get("auto_approve", False))
        ctx = RunContext(provider_name=provider_name, model=model, auto_approve=auto_approve, locale=case.locale)
        try:
            res = runner.run(agent_dir, case.input, context=ctx)
            if expect_error:
                failures.append({"case_id": case.id, "reasons": [f"expected error {expect_error!r} but succeeded"]})
                continue
            reasons = _matches_expected(res.output, case.expected)
            for field_name in case.raw.get("expect_non_empty", []):
                val = res.output.get(field_name)
                if val is None or val == "" or val == []:
                    reasons.append(f"$.{field_name}: expected non-empty value")
            for substr_key, needle in case.raw.get("expect_contains", {}).items():
                hay = str(res.output.get(substr_key, "")).lower()
                if str(needle).lower() not in hay:
                    reasons.append(f"$.{substr_key}: missing substring {needle!r}")
            expect_asked = case.raw.get("expect_asked", [])
            if expect_asked:
                missing_fields = res.output.get("missing", [])
                for mf in expect_asked:
                    if mf not in missing_fields:
                        reasons.append(f"$.missing: expected missing field {mf!r}")
            if reasons:
                failures.append({"case_id": case.id, "reasons": reasons})
            else:
                passed += 1
        except Exception as exc:
            if expect_error and expect_error in type(exc).__name__:
                passed += 1
            else:
                failures.append({"case_id": case.id, "reasons": [f"{type(exc).__name__}: {exc}"]})

    total = len(cases)
    return EvalSummary(
        agent_id=agent_id,
        total=total,
        passed=passed,
        failed=total - passed,
        pass_rate=round(passed / total, 4) if total else 1.0,
        failures=failures,
    )


def write_eval_report(summaries: list[EvalSummary], report_path: Path) -> None:
    """Persist structured JSON eval report."""
    report_path.parent.mkdir(parents=True, exist_ok=True)
    payload = [
        {
            "agent_id": s.agent_id,
            "total": s.total,
            "passed": s.passed,
            "failed": s.failed,
            "pass_rate": s.pass_rate,
            "failures": s.failures,
        }
        for s in summaries
    ]
    report_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
