"""Manifest discovery, loading, and validation for afe/v1."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ._compat import load_yaml_file, validate_json_schema
from .models import AgentManifest, MCPServerManifest, RecipeManifest, TeamManifest

REQUIRED_AGENT_FILES = (
    "agent.yaml",
    "README.md",
    "prompts/system.md",
    "schemas/input.schema.json",
    "schemas/output.schema.json",
    "tools.yaml",
    "evals/eval.yaml",
    "evals/cases.jsonl",
    "evals/rubric.md",
    "CHANGELOG.md",
)


def find_repo_root(start: Path | None = None) -> Path:
    """Locate the repository root containing `spec/agent.schema.json`."""
    cur = (start or Path.cwd()).resolve()
    for candidate in (cur, *cur.parents):
        if (candidate / "spec" / "agent.schema.json").exists():
            return candidate
    raise FileNotFoundError("Could not find repository root with spec/agent.schema.json")


def _load_schema(repo_root: Path, filename: str) -> dict[str, Any]:
    return json.loads((repo_root / "spec" / filename).read_text(encoding="utf-8"))


def load_agent_manifest(agent_dir: Path) -> AgentManifest:
    """Parse an `agent.yaml` file into an `AgentManifest`."""
    raw = load_yaml_file(agent_dir / "agent.yaml")
    meta = raw["metadata"]
    spec = raw["spec"]
    io = spec["io"]
    model = spec["model"]
    tools = spec.get("tools", {}) or {}
    safety = spec["safety"]
    limits = spec["limits"]
    evals = spec["evals"]

    return AgentManifest(
        id=meta["id"],
        name=meta["name"],
        version=meta["version"],
        family=meta["family"],
        category=meta["category"],
        tier=meta["tier"],
        maturity=meta["maturity"],
        priority=meta["priority"],
        license=meta["license"],
        summary=spec["summary"],
        purpose=spec["purpose"],
        pattern=spec["pattern"],
        autonomy=spec["autonomy"],
        input_schema_path=io["input"],
        output_schema_path=io["output"],
        capabilities=list(model.get("capabilities", [])),
        optional_capabilities=list(model.get("optional_capabilities", [])),
        min_context_tokens=int(model.get("min_context_tokens", 8000)),
        tested_with=list(model.get("tested_with", [])),
        required_tools=list(tools.get("required", [])),
        optional_tools=list(tools.get("optional", [])),
        uses_agents=list(spec.get("uses_agents", [])),
        memory=spec.get("memory", "none"),
        safety_level=safety["level"],
        side_effects=list(safety.get("side_effects", [])),
        approval_required_for=list(safety.get("approval_required_for", [])),
        handles_pii=bool(safety.get("handles_pii", False)),
        data_retention=safety.get("data_retention", "none"),
        max_steps=int(limits["max_steps"]),
        timeout_seconds=float(limits["timeout_seconds"]),
        max_cost_usd=float(limits["max_cost_usd"]),
        eval_suite=evals["suite"],
        eval_targets=dict(evals.get("targets", {})),
        exports=list(spec.get("exports", [])),
        locales=list(spec.get("locales", ["en"])),
        tags=list(meta.get("tags", [])),
        maintainers=list(meta.get("maintainers", [])),
        raw=raw,
        directory=agent_dir,
    )


def load_team_manifest(team_dir: Path) -> TeamManifest:
    """Parse a `team.yaml` file into a `TeamManifest`."""
    raw = load_yaml_file(team_dir / "team.yaml")
    meta = raw["metadata"]
    spec = raw["spec"]
    return TeamManifest(
        id=meta["id"],
        name=meta["name"],
        version=meta["version"],
        maturity=meta["maturity"],
        priority=meta["priority"],
        summary=spec["summary"],
        pattern=spec["pattern"],
        entry=spec["entry"],
        members=list(spec["members"]),
        graph=list(spec["graph"]),
        approvals=list(spec.get("approvals", [])),
        safety_level=(spec.get("safety") or {}).get("level", "S1"),
        raw=raw,
        directory=team_dir,
    )


def load_recipe_manifest(recipe_dir: Path) -> RecipeManifest:
    """Parse a `recipe.yaml` file into a `RecipeManifest`."""
    raw = load_yaml_file(recipe_dir / "recipe.yaml")
    meta = raw["metadata"]
    spec = raw["spec"]
    return RecipeManifest(
        id=meta["id"],
        name=meta["name"],
        version=meta["version"],
        maturity=meta["maturity"],
        priority=meta["priority"],
        summary=spec["summary"],
        problem=spec["problem"],
        solution=spec["solution"],
        agents=list(spec.get("agents", [])),
        teams=list(spec.get("teams", [])),
        mcp_servers=list(spec.get("mcp_servers", [])),
        entrypoint=spec["entrypoint"],
        raw=raw,
        directory=recipe_dir,
    )


def load_mcp_server_manifest(server_dir: Path) -> MCPServerManifest:
    """Parse `mcp-servers/<slug>/server.yaml`."""
    raw = load_yaml_file(server_dir / "server.yaml")
    meta = raw["metadata"]
    spec = raw["spec"]
    return MCPServerManifest(
        id=meta["id"],
        name=meta["name"],
        version=meta["version"],
        summary=spec["summary"],
        transport=spec["transport"],
        tools=list(spec.get("tools", [])),
        upstream=spec.get("upstream"),
        raw=raw,
        directory=server_dir,
    )


def discover_agents(repo_root: Path) -> dict[str, AgentManifest]:
    """Find all agents under `agents/` indexed by `<category>/<slug>`."""
    agents: dict[str, AgentManifest] = {}
    agents_root = repo_root / "agents"
    if not agents_root.exists():
        return agents
    for yaml_path in sorted(agents_root.glob("*/*/*/agent.yaml")):
        manifest = load_agent_manifest(yaml_path.parent)
        agents[manifest.id] = manifest
    return agents


def discover_teams(repo_root: Path) -> dict[str, TeamManifest]:
    """Find all teams under `teams/` indexed by team ID."""
    teams: dict[str, TeamManifest] = {}
    teams_root = repo_root / "teams"
    if not teams_root.exists():
        return teams
    for yaml_path in sorted(teams_root.glob("*/team.yaml")):
        manifest = load_team_manifest(yaml_path.parent)
        teams[manifest.id] = manifest
    return teams


def discover_recipes(repo_root: Path) -> dict[str, RecipeManifest]:
    """Find all recipes under `recipes/` indexed by recipe ID."""
    recipes: dict[str, RecipeManifest] = {}
    recipes_root = repo_root / "recipes"
    if not recipes_root.exists():
        return recipes
    for yaml_path in sorted(recipes_root.glob("*/recipe.yaml")):
        manifest = load_recipe_manifest(yaml_path.parent)
        recipes[manifest.id] = manifest
    return recipes


def discover_mcp_servers(repo_root: Path) -> dict[str, MCPServerManifest]:
    """Find all MCP servers under `mcp-servers/` indexed by ID."""
    servers: dict[str, MCPServerManifest] = {}
    mcp_root = repo_root / "mcp-servers"
    if not mcp_root.exists():
        return servers
    for yaml_path in sorted(mcp_root.glob("*/server.yaml")):
        manifest = load_mcp_server_manifest(yaml_path.parent)
        servers[manifest.id] = manifest
    return servers


def _resolve_schema_node(schema: dict[str, Any], types_dir: Path) -> dict[str, Any]:
    if "$ref" in schema:
        ref = schema["$ref"]
        if ref.startswith("afe://types/"):
            name = ref.removeprefix("afe://types/")
            if not name.endswith(".schema.json"):
                name = f"{name}.schema.json"
            target = types_dir / name
            if target.exists():
                return json.loads(target.read_text(encoding="utf-8"))
    return schema


def check_schema_compatibility(
    output_schema: dict[str, Any],
    input_schema: dict[str, Any],
    types_dir: Path,
) -> tuple[bool, list[str]]:
    """Determine if Agent A's output can feed Agent B's input.

    Returns (compatible, reasons). Two schemas are directly compatible when
    every required field in `input_schema` is provided by `output_schema` with
    a matching JSON type, or when `input_schema` accepts generic text/payload.
    """
    out_resolved = _resolve_schema_node(output_schema, types_dir)
    in_resolved = _resolve_schema_node(input_schema, types_dir)
    out_props = out_resolved.get("properties", {})
    in_required = in_resolved.get("required", [])
    if not in_required:
        return True, ["target has no required fields"]

    in_props = in_resolved.get("properties", {})
    matched: list[str] = []
    missing: list[str] = []
    for req in in_required:
        if req in out_props:
            out_t = _resolve_schema_node(out_props[req], types_dir).get("type")
            in_t = _resolve_schema_node(in_props.get(req, {}), types_dir).get("type")
            if out_t is None or in_t is None or out_t == in_t:
                matched.append(req)
            else:
                missing.append(f"{req} (type {out_t} != {in_t})")
        else:
            missing.append(req)
    if not missing:
        return True, [f"matched required fields: {', '.join(matched)}"]
    return False, [f"unmatched fields: {', '.join(missing)}"]


def validate_agent_dir(agent_dir: Path, repo_root: Path) -> list[str]:
    """Validate an agent folder against afe/v1 schema and structural rules."""
    errors: list[str] = []
    for rel in REQUIRED_AGENT_FILES:
        if not (agent_dir / rel).exists():
            errors.append(f"{agent_dir}: missing required file {rel}")

    yaml_path = agent_dir / "agent.yaml"
    if not yaml_path.exists():
        return errors

    try:
        raw = load_yaml_file(yaml_path)
    except Exception as exc:
        errors.append(f"{yaml_path}: YAML parse error: {exc}")
        return errors

    api_ver = raw.get("apiVersion", "afe/v1")
    v2_schema = repo_root / "spec" / "v2" / "agent.schema.json"
    schema_rel = "v2/agent.schema.json" if (api_ver == "afe/v2" and v2_schema.exists()) else "agent.schema.json"
    agent_schema = _load_schema(repo_root, schema_rel)
    for err in validate_json_schema(raw, agent_schema):
        errors.append(f"{yaml_path}: {err}")

    meta = raw.get("metadata", {})
    expected_family = agent_dir.parent.parent.name
    expected_cat = agent_dir.parent.name
    expected_slug = agent_dir.name
    if meta.get("family") != expected_family:
        errors.append(
            f"{yaml_path}: family {meta.get('family')!r} != directory {expected_family!r}"
        )
    if meta.get("category") != expected_cat:
        errors.append(
            f"{yaml_path}: category {meta.get('category')!r} != directory {expected_cat!r}"
        )
    if meta.get("id") != f"{expected_cat}/{expected_slug}":
        errors.append(
            f"{yaml_path}: id {meta.get('id')!r} != '{expected_cat}/{expected_slug}'"
        )

    for schema_rel in ("schemas/input.schema.json", "schemas/output.schema.json"):
        spath = agent_dir / schema_rel
        if spath.exists():
            try:
                json.loads(spath.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"{spath}: invalid JSON: {exc}")

    tools_path = agent_dir / "tools.yaml"
    if tools_path.exists():
        try:
            tools_raw = load_yaml_file(tools_path)
            tools_schema = _load_schema(repo_root, "tools.schema.json")
            for err in validate_json_schema(tools_raw, tools_schema):
                errors.append(f"{tools_path}: {err}")
        except Exception as exc:
            errors.append(f"{tools_path}: invalid YAML: {exc}")

    cases_path = agent_dir / "evals" / "cases.jsonl"
    if cases_path.exists():
        case_lines = [
            line for line in cases_path.read_text(encoding="utf-8").splitlines() if line.strip()
        ]
        maturity = meta.get("maturity")
        if maturity == "prototype" and len(case_lines) < 10:
            errors.append(
                f"{cases_path}: maturity {maturity!r} requires >= 10 eval cases, found {len(case_lines)}"
            )
        if maturity in {"beta", "stable"} and len(case_lines) < 50:
            errors.append(
                f"{cases_path}: maturity {maturity!r} requires >= 50 eval cases, found {len(case_lines)}"
            )
        safety_lvl = raw.get("spec", {}).get("safety", {}).get("level")
        if maturity in {"beta", "stable"} and safety_lvl in {"S3", "S4"}:
            if not (agent_dir / "SAFETY_REVIEW.md").exists():
                errors.append(
                    f"{agent_dir}: {safety_lvl} agent at maturity {maturity!r} requires SAFETY_REVIEW.md"
                )
        for line_no, line in enumerate(case_lines, start=1):
            try:
                case_obj = json.loads(line)
                if "id" not in case_obj or "input" not in case_obj:
                    errors.append(f"{cases_path}:{line_no}: eval case requires 'id' and 'input'")
            except json.JSONDecodeError as exc:
                errors.append(f"{cases_path}:{line_no}: invalid JSONL: {exc}")

    return errors
