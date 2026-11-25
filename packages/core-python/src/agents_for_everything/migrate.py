"""Automated afe/v1 -> afe/v2 manifest migration and validation."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from typing import Any

from ._compat import SchemaValidationError, load_yaml_file, validate_json_schema

_SAFE_UNQUOTED_KEY = re.compile(r"^[A-Za-z0-9_-]+$")
_SAFE_UNQUOTED_VAL = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]*$")
_NUMERIC_STR = re.compile(r"^[0-9]+(\.[0-9]+)?$")
_RESERVED_WORDS = {"true", "True", "TRUE", "false", "False", "FALSE", "null", "Null", "NULL", "yes", "no", "on", "off"}


def _format_scalar(val: Any) -> str:
    if val is None:
        return "null"
    if isinstance(val, bool):
        return "true" if val else "false"
    if isinstance(val, (int, float)):
        return str(val)
    text = str(val)
    if text not in _RESERVED_WORDS and not _NUMERIC_STR.match(text) and _SAFE_UNQUOTED_VAL.match(text):
        return text
    return json.dumps(text, ensure_ascii=False)


def dump_yaml(data: Any, indent: int = 0) -> str:
    """Serialize Python dicts/lists/scalars into clean YAML compatible with `_compat.load_yaml_file`."""
    prefix = " " * indent
    if isinstance(data, dict):
        if not data:
            return "{}"
        lines: list[str] = []
        for k, v in data.items():
            key_str = k if isinstance(k, str) and _SAFE_UNQUOTED_KEY.match(k) else json.dumps(str(k))
            if isinstance(v, dict) and v:
                lines.append(f"{prefix}{key_str}:")
                lines.append(dump_yaml(v, indent + 2))
            elif isinstance(v, list) and v and any(isinstance(i, (dict, list)) for i in v):
                lines.append(f"{prefix}{key_str}:")
                lines.append(dump_yaml(v, indent + 2))
            elif isinstance(v, list):
                items_str = ", ".join(_format_scalar(i) for i in v)
                lines.append(f"{prefix}{key_str}: [{items_str}]")
            elif isinstance(v, dict):
                lines.append(f"{prefix}{key_str}: {{}}")
            else:
                lines.append(f"{prefix}{key_str}: {_format_scalar(v)}")
        return "\n".join(lines)
    if isinstance(data, list):
        if not data:
            return "[]"
        lines = []
        for item in data:
            if isinstance(item, dict):
                dumped = dump_yaml(item, indent + 2).splitlines()
                first = dumped[0].lstrip() if dumped else "{}"
                lines.append(f"{prefix}- {first}")
                lines.extend(dumped[1:])
            else:
                lines.append(f"{prefix}- {_format_scalar(item)}")
        return "\n".join(lines)
    return f"{prefix}{_format_scalar(data)}"


def _infer_deployments(tested_with: list[str], category: str) -> list[str]:
    profiles: list[str] = []
    if category in {"banking", "insurance", "healthcare", "government", "legal", "finance"}:
        profiles.append("profiles/regulated-airgapped.yaml")
    elif category in {"agriculture", "voice", "accessibility"}:
        profiles.append("profiles/low-bandwidth-edge.yaml")
    if "open-weights-8b" in tested_with or "local-onprem" in tested_with:
        if "profiles/local-onprem.yaml" not in profiles:
            profiles.append("profiles/local-onprem.yaml")
    return profiles


def upgrade_manifest_v1_to_v2(
    raw: dict[str, Any],
    agent_dir: Path,
    repo_root: Path,
) -> dict[str, Any]:
    """Upgrade an `afe/v1` manifest mapping to `afe/v2` and validate against `spec/v2/agent.schema.json`."""
    upgraded = json.loads(json.dumps(raw))
    meta = upgraded.get("metadata", {})
    spec = upgraded.get("spec", {})
    safety = spec.get("safety", {})
    model = spec.get("model", {})
    evals = spec.get("evals", {})
    category = str(meta.get("category", ""))

    upgraded["apiVersion"] = "afe/v2"
    safety_lvl = str(safety.get("level", "S0"))
    safety_ok = True if safety_lvl not in {"S3", "S4"} else (agent_dir / "SAFETY_REVIEW.md").exists()
    tested_with = list(model.get("tested_with", []))
    on_prem = any(t in tested_with for t in ("open-weights-8b", "open-weights-70b", "local-onprem"))

    spec.setdefault(
        "a2a",
        {
            "protocol_version": "0.2.2",
            "streaming": spec.get("pattern") in {"react", "plan-and-execute", "orchestrator-workers"},
            "state_transition_history": spec.get("memory", "none") != "none",
            "transports": ["http+json", "stdio", "in-process"],
        },
    )
    spec.setdefault(
        "verification",
        {
            "badge": "verified" if safety_ok else "unverified",
            "safety_reviewed": safety_ok,
            "on_prem_ready": on_prem,
            "min_eval_pass_rate": float((evals.get("targets") or {}).get("pass_rate", 0.9)),
        },
    )
    profiles = _infer_deployments(tested_with, category)
    if profiles:
        spec.setdefault("deployments", {"profiles": profiles})

    v2_schema = json.loads((repo_root / "spec" / "v2" / "agent.schema.json").read_text(encoding="utf-8"))
    errors = validate_json_schema(upgraded, v2_schema)
    if errors:
        raise SchemaValidationError(f"v2 migration schema error: {'; '.join(errors)}")
    return upgraded


def migrate_agent_dir(
    agent_dir: Path,
    repo_root: Path,
    *,
    out_dir: Path | None = None,
    in_place: bool = False,
) -> tuple[Path | None, dict[str, Any]]:
    """Migrate an agent folder from `afe/v1` to `afe/v2`.

    Returns `(written_manifest_path, upgraded_manifest_dict)`.
    """
    raw = load_yaml_file(agent_dir / "agent.yaml")
    upgraded = upgrade_manifest_v1_to_v2(raw, agent_dir, repo_root)
    yaml_text = dump_yaml(upgraded) + "\n"

    if out_dir is not None:
        dest = out_dir.resolve()
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(agent_dir, dest)
        manifest_path = dest / "agent.yaml"
        manifest_path.write_text(yaml_text, encoding="utf-8")
        return manifest_path, upgraded
    if in_place:
        manifest_path = agent_dir / "agent.yaml"
        manifest_path.write_text(yaml_text, encoding="utf-8")
        return manifest_path, upgraded
    return None, upgraded
