"""Agent verification engine and deterministic badge issuance for afe/v1 & afe/v2."""

from __future__ import annotations

import hashlib
import importlib.util
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .manifest import discover_agents, load_agent_manifest, validate_agent_dir

_SECRET_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bAIza[0-9A-Za-z_-]{20,}\b"),
    re.compile(r"\bghp_[0-9A-Za-z]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
)


@dataclass(slots=True)
class VerificationRecord:
    """Verification outcome and reproducible badge digest for an agent."""

    agent_id: str
    verified: bool
    badge: str
    safety_level: str
    maturity: str
    eval_passed: int
    eval_total: int
    eval_pass_rate: float
    safety_reviewed: bool
    digest: str
    issues: list[str] = field(default_factory=list)


def compute_contract_digest(agent_dir: Path) -> str:
    """Compute a deterministic SHA-256 digest over an agent's manifest, schemas, and prompt."""
    h = hashlib.sha256()
    for rel in (
        "agent.yaml",
        "schemas/input.schema.json",
        "schemas/output.schema.json",
        "prompts/system.md",
        "tools.yaml",
    ):
        target = agent_dir / rel
        h.update(rel.encode("utf-8"))
        if target.exists():
            h.update(target.read_bytes())
    return f"sha256:{h.hexdigest()}"


def _scan_for_secrets(agent_dir: Path) -> list[str]:
    hits: list[str] = []
    for path in (
        agent_dir / "agent.yaml",
        agent_dir / "prompts" / "system.md",
        agent_dir / "impl" / "python" / "agent.py",
        agent_dir / "impl" / "typescript" / "agent.ts",
    ):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pat in _SECRET_PATTERNS:
            if pat.search(text):
                hits.append(f"{path.name}: potential hardcoded secret pattern matched")
    return hits


def _load_evaluate_agent(repo_root: Path):
    harness_path = repo_root / "evals" / "harness" / "runner.py"
    if not harness_path.exists():
        return None
    try:
        from evals.harness.runner import evaluate_agent  # type: ignore

        return evaluate_agent
    except ImportError:
        spec = importlib.util.spec_from_file_location("afe_eval_harness_runner", harness_path)
        if spec is None or spec.loader is None:
            return None
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return getattr(mod, "evaluate_agent", None)


def verify_agent_dir(
    agent_dir: Path,
    repo_root: Path,
    *,
    run_evals: bool = True,
) -> VerificationRecord:
    """Verify an agent directory against schema, safety, secret-scan, and eval standards."""
    issues = list(validate_agent_dir(agent_dir, repo_root))
    manifest = load_agent_manifest(agent_dir)

    if manifest.safety_level == "S0" and (manifest.required_tools or manifest.optional_tools):
        issues.append(f"{manifest.id}: S0 agent must not declare external tools")

    safety_review_exists = (agent_dir / "SAFETY_REVIEW.md").exists()
    if manifest.safety_level in {"S3", "S4"}:
        if not manifest.approval_required_for:
            issues.append(f"{manifest.id}: {manifest.safety_level} agent requires approval_required_for")
        if not safety_review_exists:
            issues.append(f"{manifest.id}: {manifest.safety_level} agent requires SAFETY_REVIEW.md")

    issues.extend(_scan_for_secrets(agent_dir))

    eval_passed = 0
    eval_total = 0
    eval_rate = 1.0
    if run_evals:
        eval_fn = _load_evaluate_agent(repo_root)
        if eval_fn is not None:
            summary = eval_fn(agent_dir, repo_root=repo_root, provider_name="mock")
            eval_passed = summary.passed
            eval_total = summary.total
            eval_rate = summary.pass_rate
            target = float(manifest.eval_targets.get("pass_rate", 0.9))
            if summary.failed > 0 or summary.pass_rate < target:
                issues.append(
                    f"{manifest.id}: eval pass rate {summary.passed}/{summary.total} ({summary.pass_rate:.0%}) below target {target:.0%}"
                )

    digest = compute_contract_digest(agent_dir)
    verified = len(issues) == 0
    return VerificationRecord(
        agent_id=manifest.id,
        verified=verified,
        badge="verified" if verified else "unverified",
        safety_level=manifest.safety_level,
        maturity=manifest.maturity,
        eval_passed=eval_passed,
        eval_total=eval_total,
        eval_pass_rate=eval_rate,
        safety_reviewed=safety_review_exists if manifest.safety_level in {"S3", "S4"} else True,
        digest=digest,
        issues=issues,
    )


def verify_repository_agents(
    repo_root: Path,
    *,
    run_evals: bool = True,
) -> list[VerificationRecord]:
    """Run verification across every discovered agent in a repository."""
    agents = discover_agents(repo_root)
    records: list[VerificationRecord] = []
    for aid in sorted(agents):
        manifest = agents[aid]
        assert manifest.directory is not None
        records.append(verify_agent_dir(manifest.directory, repo_root, run_evals=run_evals))
    return records
