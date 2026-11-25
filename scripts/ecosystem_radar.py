"""Generate monthly ecosystem radar digest scaffolds under radar/."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

WATCHLIST = [
    ("MCP (Model Context Protocol)", "https://github.com/modelcontextprotocol"),
    ("A2A (Agent2Agent Protocol)", "https://github.com/a2aproject/A2A"),
    ("Agent Skills Standard", "https://agentskills.io"),
    ("AGENTS.md Standard", "https://agents.md"),
    ("AG-UI Protocol", "https://github.com/ag-ui-protocol/ag-ui"),
    ("OpenTelemetry GenAI", "https://opentelemetry.io/docs/specs/semconv/gen-ai/"),
]


def main() -> int:
    now = datetime.now(timezone.utc)
    month_slug = now.strftime("%Y-%m")
    target = ROOT / "radar" / f"{month_slug}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        print(f"Radar digest already exists: {target}")
        return 0
    lines = [
        f"# Ecosystem Radar — {month_slug}",
        "",
        "Tracked standards, protocols, and framework updates for `agents-for-everything`.",
        "",
        "## Protocol & Spec Watchlist",
        "",
    ]
    for name, url in WATCHLIST:
        lines.append(f"- **{name}**: {url}")
    lines.extend(["", "## Action Items", "", "- Review quarterly taxonomy deltas against `BLUEPRINT.md`.", ""])
    target.write_text("\n".join(lines), encoding="utf-8")
    print(f"Created {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
