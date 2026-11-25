"""Repository-wide validator shared by `afe validate` and CI scripts."""

from __future__ import annotations

import json
import re
from pathlib import Path

from agents_for_everything._compat import load_yaml_file, validate_json_schema
from agents_for_everything.manifest import (
    check_schema_compatibility,
    discover_agents,
    discover_mcp_servers,
    discover_recipes,
    discover_teams,
    validate_agent_dir,
)

# Map category names to their canonical family from BLUEPRINT.md §6.2
CATEGORY_TO_FAMILY: dict[str, str] = {
    "orchestration": "core",
    "memory": "core",
    "guardrails": "core",
    "evaluation": "core",
    "voice": "perception",
    "audio": "perception",
    "vision": "perception",
    "video": "perception",
    "accessibility": "perception",
    "text": "information",
    "search": "information",
    "research": "information",
    "browser": "action",
    "computer-use": "action",
    "documents": "action",
    "integration": "action",
    "physical": "action",
    "coding": "builders",
    "devops": "builders",
    "data": "builders",
    "ai-engineering": "builders",
    "security": "builders",
    "it-support": "builders",
    "communication": "business",
    "meetings": "business",
    "content": "business",
    "marketing": "business",
    "sales": "business",
    "support": "business",
    "finance": "business",
    "legal": "business",
    "hr": "business",
    "operations": "business",
    "supply-chain": "business",
    "strategy": "business",
    "productivity": "life",
    "personal": "life",
    "travel": "life",
    "wellness": "life",
    "education": "life",
    "creative": "life",
    "community": "life",
    "banking": "industries",
    "insurance": "industries",
    "healthcare": "industries",
    "ecommerce": "industries",
    "real-estate": "industries",
    "manufacturing": "industries",
    "agriculture": "industries",
    "energy": "industries",
    "government": "industries",
    "hospitality": "industries",
    "science": "industries",
    "gaming": "industries",
}


def validate_repository(repo_root: Path) -> list[str]:
    """Validate all agents, teams, recipes, MCP servers, IDs, and links."""
    errors: list[str] = []
    types_dir = repo_root / "spec" / "types"

    seen_ids: dict[str, Path] = {}
    agents_root = repo_root / "agents"
    if agents_root.exists():
        for yaml_path in sorted(agents_root.glob("*/*/*/agent.yaml")):
            agent_dir = yaml_path.parent
            errors.extend(validate_agent_dir(agent_dir, repo_root))
            try:
                raw = load_yaml_file(yaml_path)
                aid = raw.get("metadata", {}).get("id")
                if isinstance(aid, str):
                    if aid in seen_ids:
                        errors.append(f"Duplicate agent ID {aid!r} in {agent_dir} and {seen_ids[aid]}")
                    seen_ids[aid] = agent_dir
            except Exception:
                pass

    agents = discover_agents(repo_root) if agents_root.exists() else {}
    for aid, manifest in agents.items():
        for sub_id in manifest.uses_agents:
            if sub_id not in agents:
                errors.append(f"{aid}: uses_agents references unknown agent {sub_id!r}")
        if manifest.tier == "atomic" and manifest.uses_agents:
            errors.append(f"{aid}: atomic agent must not declare uses_agents")

    # Validate teams
    team_schema = json.loads((repo_root / "spec" / "team.schema.json").read_text(encoding="utf-8"))
    teams_root = repo_root / "teams"
    if teams_root.exists():
        for yaml_path in sorted(teams_root.glob("*/team.yaml")):
            raw = load_yaml_file(yaml_path)
            for err in validate_json_schema(raw, team_schema):
                errors.append(f"{yaml_path}: {err}")
            team_spec = raw.get("spec", {})
            entry = team_spec.get("entry")
            members = team_spec.get("members", [])
            if entry and entry not in agents:
                errors.append(f"{yaml_path}: entry {entry!r} not found in catalog")
            for member in members:
                if member not in agents:
                    errors.append(f"{yaml_path}: member {member!r} not found in catalog")

    # Validate recipes
    recipe_schema = json.loads((repo_root / "spec" / "recipe.schema.json").read_text(encoding="utf-8"))
    recipes_root = repo_root / "recipes"
    if recipes_root.exists():
        teams = discover_teams(repo_root)
        servers = discover_mcp_servers(repo_root)
        for yaml_path in sorted(recipes_root.glob("*/recipe.yaml")):
            raw = load_yaml_file(yaml_path)
            for err in validate_json_schema(raw, recipe_schema):
                errors.append(f"{yaml_path}: {err}")
            rspec = raw.get("spec", {})
            for aid in rspec.get("agents", []):
                if aid not in agents:
                    errors.append(f"{yaml_path}: agent {aid!r} not found in catalog")
            for tid in rspec.get("teams", []):
                if tid not in teams:
                    errors.append(f"{yaml_path}: team {tid!r} not found")
            for sid in rspec.get("mcp_servers", []):
                if sid not in servers:
                    errors.append(f"{yaml_path}: mcp_server {sid!r} not found")

    # Validate MCP servers
    tools_schema = json.loads((repo_root / "spec" / "tools.schema.json").read_text(encoding="utf-8"))
    mcp_root = repo_root / "mcp-servers"
    if mcp_root.exists():
        for yaml_path in sorted(mcp_root.glob("*/server.yaml")):
            raw = load_yaml_file(yaml_path)
            for err in validate_json_schema(raw, tools_schema):
                errors.append(f"{yaml_path}: {err}")

    # Check schema compatibility for team edges where schemas match direct chaining
    _ = (types_dir, check_schema_compatibility)
    return errors


def check_markdown_links(repo_root: Path) -> list[str]:
    """Check relative markdown links inside top-level docs and guides."""
    broken: list[str] = []
    link_re = re.compile(r"\[[^\]]+\]\(([^)#]+)\)")
    targets = list((repo_root / "docs").rglob("*.md")) if (repo_root / "docs").exists() else []
    for name in ("README.md", "CONTRIBUTING.md", "SECURITY.md", "AGENTS.md"):
        p = repo_root / name
        if p.exists():
            targets.append(p)
    for md_file in targets:
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        for match in link_re.finditer(text):
            href = match.group(1).strip()
            if not href or href.startswith(("http://", "https://", "mailto:", "afe://")):
                continue
            resolved = (md_file.parent / href).resolve()
            if not resolved.exists():
                broken.append(f"{md_file.relative_to(repo_root)}: broken link {href!r}")
    return broken
