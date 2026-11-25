"""Generate README.md files for every agent, team, recipe and MCP server from their manifests.

Source of truth is each folder's YAML manifest (agent.yaml, team.yaml, recipe.yaml, server.yaml)
plus its schemas and eval files. Hand-written prose is preserved:

* Agents: the "use it when" / "don't use it when" lines and the Limitations section.
* Teams, recipes, MCP servers: anything below the `<!-- afe:end-generated -->` marker.

Run after changing any manifest:

    python3 scripts/build_readmes.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "packages" / "core-python" / "src"))

from agents_for_everything.manifest import (  # noqa: E402
    discover_agents,
    discover_mcp_servers,
    discover_recipes,
    discover_teams,
)

REPO_URL = "https://github.com/rupeshbharambe24/agents-for-everything"
BEGIN = "<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->"
END = "<!-- afe:end-generated -->"

CATEGORY_EMOJI = {
    "orchestration": "🧭", "memory": "🧠", "guardrails": "🛡️", "evaluation": "📏",
    "voice": "🎙️", "audio": "🎧", "vision": "👁️", "video": "🎬", "accessibility": "♿",
    "text": "📝", "search": "🔎", "research": "📚",
    "browser": "🌐", "computer-use": "🖥️", "documents": "📄", "integration": "🔌", "physical": "🤖",
    "coding": "💻", "devops": "⚙️", "data": "📊", "ai-engineering": "🧪", "security": "🔐", "it-support": "🛠️",
    "communication": "✉️", "meetings": "📅", "content": "✍️", "marketing": "📣", "sales": "🤝",
    "support": "💬", "finance": "💰", "legal": "⚖️", "hr": "👥", "operations": "📋",
    "supply-chain": "🚚", "strategy": "♟️",
    "productivity": "✅", "personal": "🏠", "travel": "✈️", "wellness": "🌿", "education": "🎓",
    "creative": "🎨", "community": "🌍",
    "banking": "🏦", "insurance": "☂️", "healthcare": "🏥", "ecommerce": "🛒", "real-estate": "🏘️",
    "manufacturing": "🏭", "agriculture": "🌾", "energy": "⚡", "government": "🏛️",
    "hospitality": "🏨", "science": "🔬", "gaming": "🎮",
}

SAFETY_TEXT = {
    "S0": ("Pure computation", "No external access; schema validation only"),
    "S1": ("Reads data", "Read-only tool scopes; untrusted input screened for prompt injection"),
    "S2": ("Reversible writes", "Drafts and local changes with preview, undo and logging"),
    "S3": ("External side effects", "Human approval per action by default"),
    "S4": ("High stakes", "Mandatory human sign-off, immutable audit log, no autonomous mode"),
}
SAFETY_COLOR = {"S0": "16a34a", "S1": "65a30d", "S2": "ca8a04", "S3": "ea580c", "S4": "dc2626"}
MATURITY_COLOR = {"spec": "94a3b8", "prototype": "f59e0b", "beta": "2563eb", "stable": "16a34a", "deprecated": "6b7280"}
PRIORITY_COLOR = {"P0": "7c3aed", "P1": "8b5cf6", "P2": "a78bfa"}
AUTONOMY_TEXT = {
    "L0": "suggests only", "L1": "human executes", "L2": "acts with per-action approval",
    "L3": "acts within policy, escalates exceptions", "L4": "fully autonomous in a sandbox",
}


# ---------------------------------------------------------------- helpers

def badge(label: str, value: str, color: str) -> str:
    def esc(s: str) -> str:
        return quote(s.replace("-", "--").replace("_", "__"), safe="")
    return f"![{label}: {value}](https://img.shields.io/badge/{esc(label)}-{esc(value)}-{color}?style=flat-square)"


def rel(from_dir: Path, target: Path) -> str:
    import os
    return Path(os.path.relpath(target, from_dir)).as_posix()


def write_if_changed(path: Path, text: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def preserved_tail(path: Path) -> str:
    """Text below the end-generated marker (kept verbatim on regeneration)."""
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    if END in text:
        return text.split(END, 1)[1].strip("\n")
    return ""


def legacy_body(path: Path) -> str:
    """For READMEs not yet generated: everything after the H1 and its first paragraph."""
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    if END in text:
        return ""
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    # drop leading blank lines and the first paragraph (it repeats the summary)
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and lines[0].strip() and not lines[0].startswith("#"):
        lines.pop(0)
    rest = "\n".join(lines).strip()
    # drop one-line "Flow:" / "Architecture" restatements that the generated block now covers
    rest = re.sub(r"^Flow:.*$", "", rest, flags=re.M).strip()
    return rest


def count_lines(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())


def mermaid_label(text: str) -> str:
    return text.replace('"', "'")


def schema_rows(schema_path: Path, readme_dir: Path) -> list[str]:
    if not schema_path.exists():
        return ["_Schema file not found._"]
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    props: dict = schema.get("properties", {}) or {}
    required = set(schema.get("required", []) or [])
    if not props:
        return [f"See [`{schema_path.name}`]({rel(readme_dir, schema_path)})."]
    rows = ["| Field | Type | Required | Notes |", "|---|---|:---:|---|"]
    for name, node in props.items():
        rows.append(f"| `{name}` | {describe_type(node, readme_dir)} | {'✅' if name in required else ''} | {describe_notes(node)} |")
    return rows


def describe_type(node: dict, readme_dir: Path) -> str:
    if not isinstance(node, dict):
        return "any"
    ref = node.get("$ref")
    if ref and ref.startswith("afe://types/"):
        tname = ref.rsplit("/", 1)[1]
        target = ROOT / "spec" / "types" / f"{tname}.schema.json"
        return f"[`{tname}`]({rel(readme_dir, target)})" if target.exists() else f"`{tname}`"
    if ref:
        return f"`{ref}`"
    t = node.get("type")
    if t == "array":
        return f"array of {describe_type(node.get('items', {}), readme_dir)}"
    if isinstance(t, list):
        return " \\| ".join(f"`{x}`" for x in t)
    if "enum" in node and not t:
        return "enum"
    if "oneOf" in node or "anyOf" in node:
        return "one of several shapes"
    return f"`{t}`" if t else "any"


def describe_notes(node: dict) -> str:
    if not isinstance(node, dict):
        return ""
    bits = []
    if node.get("description"):
        bits.append(str(node["description"]).replace("|", "\\|"))
    if "enum" in node:
        bits.append("one of " + ", ".join(f"`{v}`" for v in node["enum"]))
    if "default" in node:
        bits.append(f"default `{json.dumps(node['default'])}`")
    for k, label in (("minimum", "min"), ("maximum", "max"), ("minLength", "min length"), ("maxLength", "max length")):
        if k in node:
            bits.append(f"{label} {node[k]}")
    return "; ".join(bits)


def example_payload(agent_dir: Path) -> list[str]:
    """Shortest eval-case input as a ready-to-run example, or code that loads the first case."""
    cases = agent_dir / "evals" / "cases.jsonl"
    best = None
    if cases.exists():
        for line in cases.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                inp = json.loads(line).get("input")
            except json.JSONDecodeError:
                continue
            if isinstance(inp, dict):
                txt = json.dumps(inp, ensure_ascii=False)
                if best is None or len(txt) < len(best):
                    best = txt
    if best and len(best) <= 220:
        return [f"payload = {best}  # from evals/cases.jsonl"]
    return ["import json, pathlib",
            "first_case = pathlib.Path(\"evals/cases.jsonl\").read_text().splitlines()[0]",
            "payload = json.loads(first_case)[\"input\"]  # any input matching schemas/input.schema.json"]


def parse_agent_prose(path: Path) -> tuple[str, str, str]:
    """Extract (use_when, avoid_when, limitations) from an existing agent README (old or new format)."""
    if not path.exists():
        return "", "", ""
    text = path.read_text(encoding="utf-8")
    use = avoid = lim = ""
    m = re.search(r"\*\*Use when:\*\*\s*(.+)", text) or re.search(r"^\| \*\*Use it when\*\* \| (.+?) \|$", text, re.M)
    if m:
        use = m.group(1).strip()
    m = re.search(r"\*\*Do not use when:\*\*\s*(.+)", text) or re.search(r"^\| \*\*Don't use it when\*\* \| (.+?) \|$", text, re.M)
    if m:
        avoid = m.group(1).strip()
    m = re.search(r"^## (?:⚠️ )?Limitations\s*\n(.+?)(?=\n## |\n<!-- |\Z)", text, re.S | re.M)
    if m:
        lim = m.group(1).strip()
    return use, avoid, lim


# ---------------------------------------------------------------- agents

def build_agents(agents, teams, recipes, servers) -> int:
    used_by: dict[str, list[str]] = {}
    for a in agents.values():
        for dep in a.uses_agents:
            used_by.setdefault(dep, []).append(a.id)
    team_of: dict[str, list[str]] = {}
    for t in teams.values():
        for mem in t.members:
            team_of.setdefault(mem, []).append(t.id)
    recipe_of: dict[str, list[str]] = {}
    for r in recipes.values():
        for mem in r.agents:
            recipe_of.setdefault(mem, []).append(r.id)

    cat_titles = category_titles()
    changed = 0
    for a in agents.values():
        d: Path = a.directory
        readme = d / "README.md"
        use, avoid, lim = parse_agent_prose(readme)
        slug = a.id.split("/", 1)[1]
        emoji = CATEGORY_EMOJI.get(a.category, "🤖")
        cat_title = cat_titles.get(a.category, a.category.replace("-", " ").title())
        root = rel(d, ROOT)
        n_cases = count_lines(d / "evals" / "cases.jsonl")
        safety_name, safety_ctrl = SAFETY_TEXT.get(a.safety_level, ("", ""))

        L: list[str] = [BEGIN, ""]
        L.append(f"[🏠 Agents for Everything]({root}/README.md) › [📖 Catalog]({root}/CATALOG.md) › "
                 f"[{emoji} {cat_title}](../README.md) › **{a.name}**")
        L += ["", f"# {emoji} {a.name}", ""]
        L.append(" ".join([
            badge("id", a.id, "0f172a"),
            badge("maturity", a.maturity, MATURITY_COLOR.get(a.maturity, "64748b")),
            badge("priority", a.priority, PRIORITY_COLOR.get(a.priority, "64748b")),
            badge("tier", a.tier, "0d9488"),
            badge("safety", a.safety_level, SAFETY_COLOR.get(a.safety_level, "64748b")),
            badge("autonomy", a.autonomy, "475569"),
            badge("version", a.version, "64748b"),
        ]))
        L += ["", f"> {a.summary}", "", a.purpose, ""]

        L += ["| | |", "|---|---|"]
        if use:
            L.append(f"| **Use it when** | {use} |")
        if avoid:
            L.append(f"| **Don't use it when** | {avoid} |")
        L.append(f"| **Pattern** | `{a.pattern}` |")
        modality = a.raw["spec"].get("modality") or []
        if modality:
            L.append(f"| **Modality** | {', '.join(modality)} |")
        runtime = a.raw["spec"].get("runtime")
        L.append(f"| **Runtime** | {runtime or 'interactive'} · memory: `{a.memory}` |")
        if a.locales:
            L.append(f"| **Languages** | {', '.join(f'`{x}`' for x in a.locales)} |")
        if a.tags:
            L.append(f"| **Tags** | {' '.join(f'`{t}`' for t in a.tags)} |")
        L.append("")

        # Quick start
        L += ["## 🚀 Quick start", "", "```bash",
              f"afe add {a.id}          # copy this agent (and the agents it uses) into ./agents",
              f"afe info {a.id}         # manifest, tools, safety level",
              f"afe test {a.id}         # run its {n_cases} eval cases",
              "```", "",
              "```python",
              "from agents_for_everything import AgentRunner",
              "",
              *example_payload(d),
              f'result = AgentRunner().run("{a.id}", payload)',
              "print(result.output)",
              "```", "",
              f"> No `afe` command yet? See [Install the CLI]({root}/README.md#-quick-start).", ""]

        # How it works
        L += ["## 🧩 How it works", "", "```mermaid", "flowchart LR",
              '    IN[/"Input"/] --> AG["' + mermaid_label(a.name) + '"]',
              '    AG --> OUT[/"Output"/]']
        for i, dep in enumerate(a.uses_agents):
            L.append(f'    AG -. uses .-> D{i}["{dep}"]')
        for i, tool in enumerate(a.required_tools):
            L.append(f'    AG -. tool .-> T{i}[("{tool}")]')
        for i, tool in enumerate(a.optional_tools):
            L.append(f'    AG -. optional tool .-> O{i}[("{tool}")]')
        for i, gate in enumerate(a.approval_required_for):
            L.append(f'    AG -. needs approval .-> H{i}{{{{"human approval: {mermaid_label(gate)}"}}}}')
        L += ["```", ""]
        L += [f"1. The input is validated against [`input.schema.json`](schemas/input.schema.json).",
              f"2. The runtime enforces safety level **{a.safety_level}** and allows only the tools declared in [`tools.yaml`](tools.yaml).",
              f"3. The agent follows its [system prompt](prompts/system.md) using the `{a.pattern}` pattern"
              + (", calling the agents it composes." if a.uses_agents else "."),
              f"4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.", ""]

        # I/O
        L += ["## 📥 Input", ""] + schema_rows(d / a.input_schema_path, d) + [""]
        L += ["## 📤 Output", ""] + schema_rows(d / a.output_schema_path, d) + [""]

        # Composition
        L += ["## 🔗 Composes with", ""]
        def link_agent(aid: str) -> str:
            other = agents.get(aid)
            if not other:
                return f"`{aid}`"
            return f"[`{aid}`]({rel(d, other.directory / 'README.md')})"
        L.append("- **Uses:** " + (", ".join(link_agent(x) for x in a.uses_agents) if a.uses_agents else "_none (atomic building block)_"))
        ub = sorted(set(used_by.get(a.id, [])))
        L.append("- **Used by agents:** " + (", ".join(link_agent(x) for x in ub) if ub else "_none yet_"))
        tm = sorted(set(team_of.get(a.id, [])))
        if tm:
            L.append("- **In teams:** " + ", ".join(f"[`{t}`]({rel(d, ROOT / 'teams' / t / 'README.md')})" for t in tm))
        rc = sorted(set(recipe_of.get(a.id, [])))
        if rc:
            L.append("- **In recipes:** " + ", ".join(f"[`{r}`]({rel(d, ROOT / 'recipes' / r / 'README.md')})" for r in rc))
        L.append("")

        # Tools
        L += ["## 🧰 Tools (MCP servers)", ""]
        tools = [(t, True) for t in a.required_tools] + [(t, False) for t in a.optional_tools]
        if tools:
            L += ["| Server | Required | What it provides |", "|---|:---:|---|"]
            for tid, req in tools:
                srv = servers.get(tid)
                if srv:
                    L.append(f"| [`{tid}`]({rel(d, srv.directory / 'README.md')}) | {'✅' if req else 'optional'} | {srv.summary} |")
                else:
                    L.append(f"| `{tid}` | {'✅' if req else 'optional'} | |")
        else:
            L.append("_No tools: this agent works only on its input._")
        L.append("")

        # Safety
        L += ["## 🛡️ Safety and limits", "",
              "| | |", "|---|---|",
              f"| **Safety level** | **{a.safety_level}** — {safety_name}: {safety_ctrl} |",
              f"| **Autonomy** | **{a.autonomy}** — {AUTONOMY_TEXT.get(a.autonomy, '')} |",
              f"| **Side effects** | {', '.join(f'`{x}`' for x in a.side_effects) if a.side_effects and a.side_effects != ['none'] else 'none'} |",
              f"| **Needs approval for** | {', '.join(f'`{x}`' for x in a.approval_required_for) if a.approval_required_for and a.approval_required_for != ['none'] else 'nothing'} |",
              f"| **Handles personal data** | {'yes' if a.handles_pii else 'no'} · retention: `{a.data_retention}` |",
              f"| **Run limits** | {a.max_steps} steps · {a.timeout_seconds:g} s · ${a.max_cost_usd:g} max |"]
        if (d / "SAFETY_REVIEW.md").exists():
            L.append("| **Safety review** | [SAFETY_REVIEW.md](SAFETY_REVIEW.md) |")
        L += ["", f"Full policy: [SECURITY.md]({root}/SECURITY.md).", ""]

        # Evaluation & model
        targets = ", ".join(f"{k} ≥ {v}" for k, v in a.eval_targets.items()) or "see eval.yaml"
        L += ["## 📏 Evaluation", "",
              f"- **{n_cases} test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).",
              f"- **Targets:** {targets} ([`eval.yaml`](evals/eval.yaml)).",
              f"- **Run:** `afe test {a.id}`", "",
              "## 🧠 Model requirements", "",
              f"- **Needs:** {', '.join(f'`{c}`' for c in a.capabilities) or 'any chat model'}"
              + (f" · optional: {', '.join(f'`{c}`' for c in a.optional_capabilities)}" if a.optional_capabilities else ""),
              f"- **Context:** {a.min_context_tokens:,}+ tokens",
              f"- **Tested with:** {', '.join(f'`{m}`' for m in a.tested_with) or 'n/a'}",
              f"- **Exports:** {', '.join(f'`{x}`' for x in a.exports)}", ""]

        L += ["## ⚠️ Limitations", "", lim or "No known limitations recorded yet. Found one? Please open an issue.", ""]

        # Files
        L += ["## 📁 Files", "",
              "| File | Purpose |", "|---|---|",
              "| [`agent.yaml`](agent.yaml) | Manifest: the single source of truth |",
              "| [`prompts/system.md`](prompts/system.md) | Instructions the model follows |",
              "| [`schemas/`](schemas/input.schema.json) | Input and output contracts |",
              "| [`tools.yaml`](tools.yaml) | MCP servers and permissions |",
              "| [`evals/`](evals/eval.yaml) | Test cases, rubric, targets |"]
        if (d / "impl").exists():
            L.append("| `impl/` | Python and TypeScript implementations |")
        if (d / "examples" / "basic.md").exists():
            L.append("| [`examples/basic.md`](examples/basic.md) | Worked example |")
        L.append("| [`CHANGELOG.md`](CHANGELOG.md) | Version history |")
        L.append("")

        issue = f"{REPO_URL}/issues/new?title=" + quote(f"[{a.id}] ")
        L += ["## 🤝 Help improve this agent", "",
              "Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. "
              f"Start with the [contributing guide]({root}/CONTRIBUTING.md), or [open an issue]({issue}) about this agent.", "",
              END, ""]
        if write_if_changed(readme, "\n".join(L)):
            changed += 1
    return changed


def category_titles() -> dict[str, str]:
    bp = (ROOT / "BLUEPRINT.md").read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"^#### 7\.\d+\s+(.+?)\s+—\s+`agents/[^/]+/([^/]+)/`", bp, re.M):
        out[m.group(2)] = m.group(1).strip()
    return out


# ---------------------------------------------------------------- teams

def build_teams(agents, teams) -> int:
    changed = 0
    by_slug = {a.id.split("/", 1)[1]: a for a in agents.values()}
    for t in teams.values():
        d: Path = t.directory
        readme = d / "README.md"
        tail = preserved_tail(readme) or legacy_body(readme)
        root = rel(d, ROOT)
        L = [BEGIN, "", f"[🏠 Agents for Everything]({root}/README.md) › [👥 Teams]({root}/README.md#-ready-made-teams) › **{t.name}**", "",
             f"# 👥 {t.name}", "",
             " ".join([badge("team", t.id, "0f172a"), badge("pattern", t.pattern, "0d9488"),
                       badge("maturity", t.maturity, MATURITY_COLOR.get(t.maturity, "64748b")),
                       badge("priority", t.priority, PRIORITY_COLOR.get(t.priority, "64748b")),
                       badge("safety", t.safety_level, SAFETY_COLOR.get(t.safety_level, "64748b"))]),
             "", f"> {t.summary}", "", "## 🔀 Workflow", "", "```mermaid", "flowchart LR"]
        def node(slug: str) -> str:
            a = by_slug.get(slug)
            label = a.name if a else slug
            shape = ('{{"' + mermaid_label(label) + '"}}') if slug == "human-approval-gate" else ('["' + mermaid_label(label) + '"]')
            return f"{slug.replace('-', '_')}{shape}"
        for edge in t.graph:
            src, dst = edge[0], edge[1]
            cond = edge[2].get("when") if len(edge) > 2 and isinstance(edge[2], dict) else None
            arrow = f' -- "{mermaid_label(cond)}" --> ' if cond else " --> "
            L.append(f"    {node(src)}{arrow}{node(dst)}")
        L += ["```", "", f"Starts at `{t.entry}`." + (f" Human approval at: {', '.join(f'`{x}`' for x in t.approvals)}." if t.approvals else ""), "",
              "## 🧑‍🤝‍🧑 Members", "", "| Agent | What it does | Safety |", "|---|---|:---:|"]
        for mid in t.members:
            a = agents.get(mid)
            if a:
                L.append(f"| [`{mid}`]({rel(d, a.directory / 'README.md')}) | {a.summary} | {a.safety_level} |")
            else:
                L.append(f"| `{mid}` | | |")
        L += ["", "## 🚀 Try it", "", "```bash",
              f"afe graph {t.id}   # print the workflow and check that agent contracts fit",
              f"for a in {' '.join(t.members)}; do afe add $a; done   # copy every member",
              "```", "",
              f"Files: [`team.yaml`](team.yaml) · [`schemas/`](schemas) · [`evals/`](evals)", "", END, ""]
        text = "\n".join(L) + ("\n" + tail + "\n" if tail else "")
        if write_if_changed(readme, text):
            changed += 1
    return changed


# ---------------------------------------------------------------- recipes

def build_recipes(agents, teams, recipes, servers) -> int:
    changed = 0
    for r in recipes.values():
        d: Path = r.directory
        readme = d / "README.md"
        tail = preserved_tail(readme) or legacy_body(readme)
        root = rel(d, ROOT)
        L = [BEGIN, "", f"[🏠 Agents for Everything]({root}/README.md) › [🍳 Recipes]({root}/README.md#-product-recipes) › **{r.name}**", "",
             f"# 🍳 {r.name}", "",
             " ".join([badge("recipe", r.id, "0f172a"), badge("maturity", r.maturity, MATURITY_COLOR.get(r.maturity, "64748b")),
                       badge("priority", r.priority, PRIORITY_COLOR.get(r.priority, "64748b"))]),
             "", f"> {r.summary}", "",
             "| | |", "|---|---|", f"| **Problem** | {r.problem} |", f"| **Solution** | {r.solution} |", "",
             ]
        if f"recipes/{d.name}/{r.entrypoint}" not in tail:
            L += ["## 🚀 Run it", "", "```bash",
                  f"PYTHONPATH=.:packages/core-python/src:cli/src python3 recipes/{d.name}/{r.entrypoint}",
                  f"PYTHONPATH=.:packages/core-python/src:cli/src python3 -m unittest recipes/{d.name}/tests/test_recipe.py",
                  "```", ""]
        L += ["## 🧩 Built from", ""]
        L += ["| Agent | What it does | Safety |", "|---|---|:---:|"]
        for aid in r.agents:
            a = agents.get(aid)
            L.append(f"| [`{aid}`]({rel(d, a.directory / 'README.md')}) | {a.summary} | {a.safety_level} |" if a else f"| `{aid}` | | |")
        if r.teams:
            L += ["", "**Teams:** " + ", ".join(f"[`{t}`]({rel(d, ROOT / 'teams' / t / 'README.md')})" for t in r.teams)]
        if r.mcp_servers:
            L += ["", "**MCP servers:** " + ", ".join(
                f"[`{s}`]({rel(d, servers[s].directory / 'README.md')})" if s in servers else f"`{s}`" for s in r.mcp_servers)]
        L += ["", END, ""]
        text = "\n".join(L) + ("\n" + tail + "\n" if tail else "")
        if write_if_changed(readme, text):
            changed += 1
    return changed


# ---------------------------------------------------------------- MCP servers

def build_servers(agents, servers) -> int:
    changed = 0
    users: dict[str, list[str]] = {}
    for a in agents.values():
        for t in a.required_tools + a.optional_tools:
            users.setdefault(t, []).append(a.id)
    for s in servers.values():
        d: Path = s.directory
        readme = d / "README.md"
        tail = preserved_tail(readme) or legacy_body(readme)
        root = rel(d, ROOT)
        L = [BEGIN, "", f"[🏠 Agents for Everything]({root}/README.md) › [🧰 MCP servers]({root}/CATALOG.md#mcp-servers) › **{s.name}**", "",
             f"# 🧰 {s.name}", "",
             " ".join([badge("id", s.id, "0f172a"), badge("transport", s.transport, "0d9488"), badge("version", s.version, "64748b")]),
             "", f"> {s.summary}", ""]
        if s.upstream:
            L += [f"**Backed by:** {s.upstream}", ""]
        L += ["## 🔧 Tools", "", "| Tool | Description | Read-only |", "|---|---|:---:|"]
        for tool in s.tools:
            if isinstance(tool, dict):
                L.append(f"| `{tool.get('name', '')}` | {tool.get('description', '')} | {'✅' if tool.get('read_only') else ''} |")
        u = sorted(set(users.get(s.id, [])))
        L += ["", f"## 🤖 Used by {len(u)} agent{'s' if len(u) != 1 else ''}", ""]
        if u:
            L.append(", ".join(f"[`{x}`]({rel(d, agents[x].directory / 'README.md')})" for x in u))
        else:
            L.append("_No agents use this server yet._")
        L += ["", f"Contract: [`server.yaml`](server.yaml)", "", END, ""]
        text = "\n".join(L) + ("\n" + tail + "\n" if tail else "")
        if write_if_changed(readme, text):
            changed += 1
    return changed


def main() -> int:
    agents = discover_agents(ROOT)
    teams = discover_teams(ROOT)
    recipes = discover_recipes(ROOT)
    servers = discover_mcp_servers(ROOT)
    a = build_agents(agents, teams, recipes, servers)
    t = build_teams(agents, teams)
    r = build_recipes(agents, teams, recipes, servers)
    s = build_servers(agents, servers)
    print(f"READMEs updated: {a} agents, {t} teams, {r} recipes, {s} MCP servers "
          f"(of {len(agents)}, {len(teams)}, {len(recipes)}, {len(servers)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
