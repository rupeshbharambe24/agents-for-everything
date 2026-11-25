"""Generate CATALOG.md, registry/catalog.json, and registry/compatibility-graph.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "packages" / "core-python" / "src"))

from agents_for_everything.manifest import (  # noqa: E402
    check_schema_compatibility,
    discover_agents,
    discover_mcp_servers,
    discover_recipes,
    discover_teams,
)


def main() -> int:
    agents = discover_agents(ROOT)
    teams = discover_teams(ROOT)
    recipes = discover_recipes(ROOT)
    servers = discover_mcp_servers(ROOT)
    types_dir = ROOT / "spec" / "types"

    registry_dir = ROOT / "registry"
    registry_dir.mkdir(parents=True, exist_ok=True)

    # 1. Build registry/catalog.json
    catalog_data = {
        "apiVersion": "afe/v1",
        "counts": {
            "agents": len(agents),
            "teams": len(teams),
            "recipes": len(recipes),
            "mcp_servers": len(servers),
        },
        "agents": [
            {
                "id": m.id,
                "name": m.name,
                "version": m.version,
                "family": m.family,
                "category": m.category,
                "tier": m.tier,
                "maturity": m.maturity,
                "priority": m.priority,
                "pattern": m.pattern,
                "autonomy": m.autonomy,
                "safety_level": m.safety_level,
                "summary": m.summary,
                "tools": {"required": m.required_tools, "optional": m.optional_tools},
                "uses_agents": m.uses_agents,
                "locales": m.locales,
                "tags": m.tags,
                "path": str(m.directory.relative_to(ROOT)) if m.directory else "",
            }
            for m in agents.values()
        ],
        "teams": [
            {
                "id": t.id,
                "name": t.name,
                "maturity": t.maturity,
                "priority": t.priority,
                "pattern": t.pattern,
                "members": t.members,
                "summary": t.summary,
            }
            for t in teams.values()
        ],
        "recipes": [
            {
                "id": r.id,
                "name": r.name,
                "maturity": r.maturity,
                "priority": r.priority,
                "agents": r.agents,
                "teams": r.teams,
                "summary": r.summary,
            }
            for r in recipes.values()
        ],
        "mcp_servers": [
            {
                "id": s.id,
                "name": s.name,
                "transport": s.transport,
                "summary": s.summary,
            }
            for s in servers.values()
        ],
    }
    (registry_dir / "catalog.json").write_text(json.dumps(catalog_data, indent=2), encoding="utf-8")

    # 2. Build registry/compatibility-graph.json
    schemas: dict[str, tuple[dict, dict]] = {}
    for aid, m in agents.items():
        if m.directory is None:
            continue
        in_s = json.loads((m.directory / m.input_schema_path).read_text(encoding="utf-8"))
        out_s = json.loads((m.directory / m.output_schema_path).read_text(encoding="utf-8"))
        schemas[aid] = (in_s, out_s)

    edges: list[dict[str, str]] = []
    for src_id, (_, src_out) in schemas.items():
        for dst_id, (dst_in, _) in schemas.items():
            if src_id == dst_id:
                continue
            dst_req = dst_in.get("required", [])
            if not dst_req:
                continue
            ok, reasons = check_schema_compatibility(src_out, dst_in, types_dir)
            if ok:
                edges.append({"from": src_id, "to": dst_id, "reason": reasons[0]})

    (registry_dir / "compatibility-graph.json").write_text(
        json.dumps({"apiVersion": "afe/v1", "edges": edges}, indent=2),
        encoding="utf-8",
    )

    # 3. Build CATALOG.md
    lines = [
        "# Agents for Everything — Catalog",
        "",
        "> Auto-generated from `agent.yaml`, `team.yaml`, `recipe.yaml`, and `server.yaml` manifests via `scripts/build_catalog.py`.",
        "",
        f"- **Agents:** {len(agents)}",
        f"- **Teams:** {len(teams)}",
        f"- **Recipes:** {len(recipes)}",
        f"- **MCP Servers:** {len(servers)}",
        f"- **Direct Compatible Edges:** {len(edges)}",
        "",
        "## Agents",
        "",
        "| ID | Name | Family / Category | Tier | Maturity | Priority | Safety | Summary |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for m in agents.values():
        rel = m.directory.relative_to(ROOT) if m.directory else ""
        lines.append(
            f"| [`{m.id}`]({rel}/README.md) | {m.name} | `{m.family}/{m.category}` | {m.tier} | `{m.maturity}` | {m.priority} | {m.safety_level} | {m.summary} |"
        )

    lines.extend([
        "",
        "## Teams",
        "",
        "| ID | Name | Pattern | Maturity | Priority | Members | Summary |",
        "|---|---|---|---|---|---|---|",
    ])
    for t in teams.values():
        lines.append(
            f"| [`{t.id}`](teams/{t.id}/README.md) | {t.name} | {t.pattern} | `{t.maturity}` | {t.priority} | {len(t.members)} | {t.summary} |"
        )

    lines.extend([
        "",
        "## Recipes",
        "",
        "| ID | Name | Maturity | Priority | Entrypoint | Summary |",
        "|---|---|---|---|---|---|",
    ])
    for r in recipes.values():
        lines.append(
            f"| [`{r.id}`](recipes/{r.id}/README.md) | {r.name} | `{r.maturity}` | {r.priority} | `{r.entrypoint}` | {r.summary} |"
        )

    lines.extend([
        "",
        "## MCP Servers",
        "",
        "| ID | Name | Transport | Summary |",
        "|---|---|---|---|",
    ])
    for s in servers.values():
        slug = s.id.split("/", 1)[-1]
        lines.append(f"| [`{s.id}`](mcp-servers/{slug}/README.md) | {s.name} | `{s.transport}` | {s.summary} |")

    (ROOT / "CATALOG.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Built catalog: {len(agents)} agents, {len(teams)} teams, {len(recipes)} recipes, {len(servers)} MCP servers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
