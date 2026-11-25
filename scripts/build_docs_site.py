"""Bundle registry/catalog.json, compatibility-graph.json, and eval leaderboard for docs/site/."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    reg_dir = ROOT / "registry"
    site_dir = ROOT / "docs" / "site"
    site_dir.mkdir(parents=True, exist_ok=True)

    catalog = json.loads((reg_dir / "catalog.json").read_text(encoding="utf-8"))
    graph = json.loads((reg_dir / "compatibility-graph.json").read_text(encoding="utf-8"))
    lb_path = ROOT / "evals" / "reports" / "leaderboard.json"
    leaderboard = json.loads(lb_path.read_text(encoding="utf-8")) if lb_path.exists() else []

    payload = {
        "catalog": catalog,
        "graph": graph,
        "leaderboard": leaderboard,
    }
    js = "window.AFE_SITE_DATA = " + json.dumps(payload, separators=(",", ":")) + ";\n"
    (site_dir / "data.js").write_text(js, encoding="utf-8")
    print(f"Built docs/site/data.js ({len(catalog.get('agents', []))} agents, {len(graph.get('edges', []))} graph edges).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
