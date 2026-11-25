"""Command-line interface for `agents-for-everything` (`afe`)."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any

from agents_for_everything import (
    AgentRunner,
    RunContext,
    check_schema_compatibility,
    discover_agents,
    discover_teams,
    dump_yaml,
    export_agent,
    find_repo_root,
    migrate_agent_dir,
    verify_agent_dir,
    verify_repository_agents,
)
from evals.harness.runner import evaluate_agent

from .validator import CATEGORY_TO_FAMILY, validate_repository


def _resolve_root(root_arg: str | None) -> Path:
    if root_arg:
        return Path(root_arg).resolve()
    return find_repo_root()


def _cmd_search(args: argparse.Namespace) -> int:
    root = _resolve_root(args.repo_root)
    agents = discover_agents(root)
    q = (args.query or "").lower().strip()
    matches = []
    for aid, m in sorted(agents.items()):
        if args.family and m.family != args.family:
            continue
        if args.category and m.category != args.category:
            continue
        if args.safety and m.safety_level != args.safety:
            continue
        if args.priority and m.priority != args.priority:
            continue
        if args.maturity and m.maturity != args.maturity:
            continue
        haystack = " ".join([aid, m.name, m.summary, m.purpose, *m.tags]).lower()
        if not q or all(term in haystack for term in q.split()):
            matches.append(m)

    if not matches:
        print("No matching agents found.")
        return 0
    for m in matches:
        print(f"{m.id:36s} [{m.priority} | {m.safety_level} | {m.maturity:9s}] {m.summary}")
    print(f"\nTotal: {len(matches)} agent(s)")
    return 0


def _cmd_info(args: argparse.Namespace) -> int:
    root = _resolve_root(args.repo_root)
    agents = discover_agents(root)
    if args.agent_id not in agents:
        print(f"Error: unknown agent '{args.agent_id}'", file=sys.stderr)
        return 1
    m = agents[args.agent_id]
    print(f"ID:          {m.id}")
    print(f"Name:        {m.name} (v{m.version})")
    print(f"Family/Cat:  {m.family}/{m.category}")
    print(f"Tier/Mat:    {m.tier} · {m.maturity} · {m.priority}")
    print(f"Pattern:     {m.pattern} · Autonomy: {m.autonomy} · Safety: {m.safety_level}")
    print(f"Summary:     {m.summary}")
    print(f"Tools:       required={m.required_tools} optional={m.optional_tools}")
    print(f"Composes:    {m.uses_agents}")
    print(f"Locales:     {m.locales}")
    print(f"Path:        {m.directory}")
    return 0


def _collect_agent_closure(agent_id: str, agents: dict[str, Any], seen: list[str]) -> None:
    if agent_id in seen:
        return
    if agent_id not in agents:
        raise KeyError(f"Referenced agent not found: {agent_id}")
    seen.append(agent_id)
    for dep in agents[agent_id].uses_agents:
        _collect_agent_closure(dep, agents, seen)


def _cmd_add(args: argparse.Namespace) -> int:
    root = _resolve_root(args.repo_root)
    agents = discover_agents(root)
    if args.agent_id not in agents:
        print(f"Error: unknown agent '{args.agent_id}'", file=sys.stderr)
        return 1
    closure: list[str] = []
    _collect_agent_closure(args.agent_id, agents, closure)
    dest_root = Path(args.dest).resolve()
    dest_root.mkdir(parents=True, exist_ok=True)
    for aid in closure:
        manifest = agents[aid]
        assert manifest.directory is not None
        target = dest_root / manifest.category / aid.split("/", 1)[1]
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(manifest.directory, target)
        print(f"Added {aid} -> {target}")
    types_src = root / "spec" / "types"
    if types_src.exists():
        types_dst = dest_root / "_types"
        if types_dst.exists():
            shutil.rmtree(types_dst)
        shutil.copytree(types_src, types_dst)
    return 0


def _cmd_run(args: argparse.Namespace) -> int:
    root = _resolve_root(args.repo_root)
    raw_in = args.input.strip()
    if Path(raw_in).is_file():
        payload = json.loads(Path(raw_in).read_text(encoding="utf-8"))
    else:
        payload = json.loads(raw_in)
    runner = AgentRunner(repo_root=root)
    ctx = RunContext(
        provider_name=args.provider,
        model=args.model,
        auto_approve=args.auto_approve,
    )
    res = runner.run(args.agent_id, payload, context=ctx)
    print(json.dumps(res.output, indent=2, ensure_ascii=False))
    return 0


def _cmd_test(args: argparse.Namespace) -> int:
    root = _resolve_root(args.repo_root)
    agents = discover_agents(root)
    provider = args.provider if args.live else "mock"
    if args.all or not args.agent_id:
        targets = sorted(agents.keys())
    else:
        if args.agent_id not in agents:
            print(f"Error: unknown agent '{args.agent_id}'", file=sys.stderr)
            return 1
        targets = [args.agent_id]

    all_ok = True
    for aid in targets:
        summary = evaluate_agent(aid, repo_root=root, provider_name=provider, model=args.model)
        status = "PASS" if summary.failed == 0 else "FAIL"
        print(f"[{status}] {aid:36s} {summary.passed}/{summary.total} ({summary.pass_rate:.0%})")
        for fail in summary.failures:
            print(f"   - {fail['case_id']}: {'; '.join(fail['reasons'])}")
        if summary.failed > 0:
            all_ok = False
    return 0 if all_ok else 1


def _render_template_tree(src: Path, dst: Path, tokens: dict[str, str]) -> None:
    for item in src.rglob("*"):
        rel = item.relative_to(src)
        target = dst / rel
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            content = item.read_text(encoding="utf-8")
            for k, v in tokens.items():
                content = content.replace(f"{{{{{k}}}}}", v)
            target.write_text(content, encoding="utf-8")


def _cmd_new(args: argparse.Namespace) -> int:
    root = _resolve_root(args.repo_root)
    slug = args.slug.strip().lower()
    name = args.name or slug.replace("-", " ").title()
    summary = args.summary or f"Single-purpose {name} capability."
    if args.tier in {"atomic", "composite"}:
        cat = args.category
        if not cat:
            print("Error: --category is required for agent scaffolds", file=sys.stderr)
            return 1
        family = args.family or CATEGORY_TO_FAMILY.get(cat)
        if not family:
            print(f"Error: unknown category '{cat}'; pass --family explicitly", file=sys.stderr)
            return 1
        dest = root / "agents" / family / cat / slug
        if dest.exists():
            print(f"Error: destination already exists: {dest}", file=sys.stderr)
            return 1
        _render_template_tree(
            root / "templates" / "agent-atomic",
            dest,
            {"slug": slug, "category": cat, "family": family, "name": name, "summary": summary},
        )
        if args.tier == "composite":
            comp_yaml = (root / "templates" / "agent-composite" / "agent.yaml").read_text(encoding="utf-8")
            for k, v in {"slug": slug, "category": cat, "family": family, "name": name, "summary": summary}.items():
                comp_yaml = comp_yaml.replace(f"{{{{{k}}}}}", v)
            (dest / "agent.yaml").write_text(comp_yaml, encoding="utf-8")
        print(f"Scaffolded {args.tier} agent at {dest}")
        return 0

    if args.tier == "team":
        dest = root / "teams" / slug
        if dest.exists():
            print(f"Error: destination already exists: {dest}", file=sys.stderr)
            return 1
        _render_template_tree(
            root / "templates" / "team",
            dest,
            {"slug": slug, "name": name, "summary": summary},
        )
        print(f"Scaffolded team at {dest}")
        return 0

    if args.tier == "recipe":
        dest = root / "recipes" / slug
        if dest.exists():
            print(f"Error: destination already exists: {dest}", file=sys.stderr)
            return 1
        _render_template_tree(
            root / "templates" / "recipe",
            dest,
            {"slug": slug, "name": name, "summary": summary},
        )
        print(f"Scaffolded recipe at {dest}")
        return 0

    return 1


def _cmd_export(args: argparse.Namespace) -> int:
    root = _resolve_root(args.repo_root)
    agents = discover_agents(root)
    out_base = Path(args.out).resolve()
    if args.all or not args.agent_id:
        count = 0
        for aid, manifest in sorted(agents.items()):
            assert manifest.directory is not None
            cat_out = out_base / manifest.category
            export_agent(manifest.directory, args.target_format, cat_out)
            count += 1
        print(f"Exported {count} agent(s) ({args.target_format}) -> {out_base}")
        return 0
    if args.agent_id not in agents:
        print(f"Error: unknown agent '{args.agent_id}'", file=sys.stderr)
        return 1
    manifest = agents[args.agent_id]
    assert manifest.directory is not None
    written = export_agent(manifest.directory, args.target_format, out_base)
    for p in written:
        print(f"Exported {args.agent_id} ({args.target_format}) -> {p}")
    return 0


def _cmd_validate(args: argparse.Namespace) -> int:
    root = _resolve_root(args.repo_root)
    errors = validate_repository(root)
    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        print(f"\nValidation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1
    agents = discover_agents(root)
    teams = discover_teams(root)
    print(f"Validation passed: {len(agents)} agent(s), {len(teams)} team(s).")
    return 0


def _resolve_target_agent_dir(root: Path, target: str) -> Path:
    path_candidate = Path(target)
    if (path_candidate / "agent.yaml").exists():
        return path_candidate.resolve()
    agents = discover_agents(root)
    if target not in agents:
        raise KeyError(f"Unknown agent or path: {target!r}")
    manifest = agents[target]
    assert manifest.directory is not None
    return manifest.directory


def _cmd_verify(args: argparse.Namespace) -> int:
    root = _resolve_root(args.repo_root)
    run_evals = not args.skip_evals
    if args.all or not args.target:
        records = verify_repository_agents(root, run_evals=run_evals)
    else:
        try:
            agent_dir = _resolve_target_agent_dir(root, args.target)
        except KeyError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 1
        records = [verify_agent_dir(agent_dir, root, run_evals=run_evals)]

    if args.json:
        payload = [
            {
                "agent_id": r.agent_id,
                "verified": r.verified,
                "badge": r.badge,
                "safety_level": r.safety_level,
                "maturity": r.maturity,
                "eval_passed": r.eval_passed,
                "eval_total": r.eval_total,
                "eval_pass_rate": r.eval_pass_rate,
                "safety_reviewed": r.safety_reviewed,
                "digest": r.digest,
                "issues": r.issues,
            }
            for r in records
        ]
        print(json.dumps(payload, indent=2))
    else:
        for r in records:
            tag = "VERIFIED" if r.verified else "FAILED  "
            print(f"[{tag}] {r.agent_id:38s} {r.safety_level} · {r.eval_passed}/{r.eval_total} · {r.digest[:19]}")
            for iss in r.issues:
                print(f"   - {iss}")

    verified_count = sum(1 for r in records if r.verified)
    if verified_count != len(records):
        return 1
    if not args.json and len(records) > 1:
        print(f"\nVerified badge granted to {verified_count}/{len(records)} agent(s).")
    return 0


def _cmd_migrate(args: argparse.Namespace) -> int:
    root = _resolve_root(args.repo_root)
    try:
        agent_dir = _resolve_target_agent_dir(root, args.target)
    except KeyError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    out_dir = Path(args.out).resolve() if args.out else None
    written, upgraded = migrate_agent_dir(
        agent_dir,
        root,
        out_dir=out_dir,
        in_place=bool(args.in_place),
    )
    if written is not None:
        print(f"Migrated {upgraded['metadata']['id']} -> afe/v2 ({written})")
    else:
        print(dump_yaml(upgraded))
    return 0


def _cmd_graph(args: argparse.Namespace) -> int:
    root = _resolve_root(args.repo_root)
    agents = discover_agents(root)
    teams = discover_teams(root)
    types_dir = root / "spec" / "types"
    target = args.target_id

    if target in agents:
        seen: list[str] = []
        _collect_agent_closure(target, agents, seen)
        print(f"Agent Dependency Graph for {target}:")
        for idx, aid in enumerate(seen):
            m = agents[aid]
            prefix = "└─" if idx == len(seen) - 1 else "├─"
            print(f"  {prefix} {aid} ({m.tier}, {m.safety_level}) -> uses {m.uses_agents}")
        return 0

    if target in teams:
        team = teams[target]
        print(f"Team Workflow Graph for {team.id} ({team.pattern}):")
        for edge in team.graph:
            src_node = edge[0]
            dst_node = edge[1]
            src_id = next((m for m in team.members if m == src_node or m.endswith(f"/{src_node}")), src_node)
            dst_id = next((m for m in team.members if m == dst_node or m.endswith(f"/{dst_node}")), dst_node)
            compat = "unknown"
            if src_id in agents and dst_id in agents:
                s_out = json.loads((agents[src_id].directory / agents[src_id].output_schema_path).read_text())  # type: ignore
                d_in = json.loads((agents[dst_id].directory / agents[dst_id].input_schema_path).read_text())  # type: ignore
                ok, reasons = check_schema_compatibility(s_out, d_in, types_dir)
                compat = f"{'compatible' if ok else 'adapter-needed'} ({reasons[0]})"
            print(f"  {src_id} -> {dst_id} [{compat}]")
        return 0

    print(f"Error: '{target}' not found in agents or teams", file=sys.stderr)
    return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="afe",
        description="Agents for Everything CLI (search, add, run, test, validate, export)",
    )
    parser.add_argument("--repo-root", default=None, help="Path to agents-for-everything repository root")
    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search", help="Search the agent catalog")
    p_search.add_argument("query", nargs="?", default="")
    p_search.add_argument("--family")
    p_search.add_argument("--category")
    p_search.add_argument("--safety")
    p_search.add_argument("--priority")
    p_search.add_argument("--maturity")
    p_search.set_defaults(func=_cmd_search)

    p_info = sub.add_parser("info", help="Show details for an agent")
    p_info.add_argument("agent_id")
    p_info.set_defaults(func=_cmd_info)

    p_add = sub.add_parser("add", help="Copy an agent and its dependencies into a project")
    p_add.add_argument("agent_id")
    p_add.add_argument("--dest", default="./agents")
    p_add.set_defaults(func=_cmd_add)

    p_run = sub.add_parser("run", help="Run an agent with JSON or JSON file input")
    p_run.add_argument("agent_id")
    p_run.add_argument("--input", required=True)
    p_run.add_argument("--provider", default="auto")
    p_run.add_argument("--model", default=None)
    p_run.add_argument("--auto-approve", action="store_true")
    p_run.set_defaults(func=_cmd_run)

    p_test = sub.add_parser("test", help="Run eval suites for one or all agents")
    p_test.add_argument("agent_id", nargs="?")
    p_test.add_argument("--all", action="store_true")
    p_test.add_argument("--live", action="store_true")
    p_test.add_argument("--provider", default="auto")
    p_test.add_argument("--model", default=None)
    p_test.set_defaults(func=_cmd_test)

    p_new = sub.add_parser("new", help="Scaffold a new agent, team, or recipe")
    p_new.add_argument("--tier", required=True, choices=["atomic", "composite", "team", "recipe"])
    p_new.add_argument("--category", default=None)
    p_new.add_argument("--family", default=None)
    p_new.add_argument("--slug", required=True)
    p_new.add_argument("--name", default=None)
    p_new.add_argument("--summary", default=None)
    p_new.set_defaults(func=_cmd_new)

    p_export = sub.add_parser("export", help="Export an agent to skill/a2a/mcp/subagent/langgraph")
    p_export.add_argument("agent_id", nargs="?")
    p_export.add_argument("--all", action="store_true")
    p_export.add_argument("--as", dest="target_format", required=True, choices=["skill", "mcp-server", "a2a", "subagent", "langgraph"])
    p_export.add_argument("--out", default="./exports")
    p_export.set_defaults(func=_cmd_export)

    p_val = sub.add_parser("validate", help="Validate all manifests, schemas, and references")
    p_val.set_defaults(func=_cmd_validate)

    p_verify = sub.add_parser("verify", help="Verify agents for verified badge eligibility (schema, evals, safety, secrets)")
    p_verify.add_argument("target", nargs="?")
    p_verify.add_argument("--all", action="store_true")
    p_verify.add_argument("--skip-evals", action="store_true")
    p_verify.add_argument("--json", action="store_true")
    p_verify.set_defaults(func=_cmd_verify)

    p_migrate = sub.add_parser("migrate", help="Migrate an agent manifest from afe/v1 to afe/v2")
    p_migrate.add_argument("target")
    p_migrate.add_argument("--out", default=None)
    p_migrate.add_argument("--in-place", action="store_true")
    p_migrate.set_defaults(func=_cmd_migrate)

    p_graph = sub.add_parser("graph", help="Print dependency or team workflow graph")
    p_graph.add_argument("target_id")
    p_graph.set_defaults(func=_cmd_graph)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
