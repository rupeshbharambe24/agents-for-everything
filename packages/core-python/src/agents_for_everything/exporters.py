"""Portable exporters for A2A Agent Cards, Agent Skills, MCP servers, subagents, and LangGraph."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .manifest import load_agent_manifest
from .models import AgentManifest


def build_a2a_card(manifest: AgentManifest, input_schema: dict[str, Any], output_schema: dict[str, Any]) -> dict[str, Any]:
    """Generate an A2A-compliant Agent Card dictionary."""
    return {
        "name": manifest.name,
        "id": manifest.id,
        "version": manifest.version,
        "description": manifest.summary,
        "capabilities": {
            "streaming": manifest.pattern in {"react", "plan-and-execute"},
            "stateTransitionHistory": manifest.memory != "none",
        },
        "skills": [
            {
                "id": manifest.id,
                "name": manifest.name,
                "description": manifest.purpose,
                "tags": manifest.tags,
                "inputSchema": input_schema,
                "outputSchema": output_schema,
            }
        ],
        "metadata": {
            "safetyLevel": manifest.safety_level,
            "autonomyLevel": manifest.autonomy,
            "maturity": manifest.maturity,
            "license": manifest.license,
        },
    }


def build_agent_skill_md(manifest: AgentManifest, system_prompt: str) -> str:
    """Generate an open Agent Skills (`SKILL.md`) file."""
    slug = manifest.id.split("/", 1)[-1]
    return (
        "---\n"
        f"name: {slug}\n"
        f"description: {manifest.summary}\n"
        "---\n\n"
        f"# {manifest.name} (`{manifest.id}`)\n\n"
        f"{manifest.purpose}\n\n"
        "## Instructions\n\n"
        f"{system_prompt.strip()}\n"
    )


def build_mcp_wrapper_py(manifest: AgentManifest) -> str:
    """Generate a standalone runnable MCP stdio wrapper for an agent."""
    return f'''"""Generated MCP wrapper for {manifest.id}."""
import json
import sys
from agents_for_everything import AgentRunner

def main() -> None:
    runner = AgentRunner()
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        params = req.get("params", {{}})
        result = runner.run("{manifest.id}", params)
        sys.stdout.write(json.dumps({{"id": req.get("id"), "result": result.output}}) + "\\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
'''


def build_subagent_md(manifest: AgentManifest, system_prompt: str) -> str:
    """Generate a Claude Code / Antigravity compatible subagent Markdown file."""
    slug = manifest.id.split("/", 1)[-1]
    tools_line = ", ".join(manifest.required_tools) if manifest.required_tools else "none"
    return (
        "---\n"
        f"name: {slug}\n"
        f"description: {manifest.summary}\n"
        f"tools: {tools_line}\n"
        "---\n\n"
        f"{system_prompt.strip()}\n"
    )


def build_langgraph_stub_py(manifest: AgentManifest) -> str:
    """Generate a LangGraph node wrapper calling `agents_for_everything.AgentRunner`."""
    fn_name = manifest.id.replace("/", "_").replace("-", "_")
    return f'''"""LangGraph node wrapper for {manifest.id}."""
from typing import Any
from agents_for_everything import AgentRunner

_runner = AgentRunner()

def {fn_name}_node(state: dict[str, Any]) -> dict[str, Any]:
    res = _runner.run("{manifest.id}", state)
    return {{**state, **res.output}}
'''


def export_agent(agent_dir: Path, target: str, out_dir: Path) -> list[Path]:
    """Export an agent folder into `a2a`, `skill`, `mcp-server`, `subagent`, or `langgraph`."""
    manifest = load_agent_manifest(agent_dir)
    slug = manifest.id.split("/", 1)[-1]
    system_prompt = (agent_dir / "prompts" / "system.md").read_text(encoding="utf-8")
    input_schema = json.loads((agent_dir / manifest.input_schema_path).read_text(encoding="utf-8"))
    output_schema = json.loads((agent_dir / manifest.output_schema_path).read_text(encoding="utf-8"))

    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    normalized = target.lower()

    if normalized in {"a2a", "a2a-card"}:
        dest = out_dir / f"{slug}.agent-card.json"
        dest.write_text(json.dumps(build_a2a_card(manifest, input_schema, output_schema), indent=2), encoding="utf-8")
        written.append(dest)
    elif normalized in {"skill", "agent-skill"}:
        skill_dir = out_dir / slug
        skill_dir.mkdir(parents=True, exist_ok=True)
        dest = skill_dir / "SKILL.md"
        dest.write_text(build_agent_skill_md(manifest, system_prompt), encoding="utf-8")
        written.append(dest)
    elif normalized == "mcp-server":
        dest = out_dir / f"{slug}_mcp_server.py"
        dest.write_text(build_mcp_wrapper_py(manifest), encoding="utf-8")
        written.append(dest)
    elif normalized == "subagent":
        dest = out_dir / f"{slug}.md"
        dest.write_text(build_subagent_md(manifest, system_prompt), encoding="utf-8")
        written.append(dest)
    elif normalized == "langgraph":
        dest = out_dir / f"{slug}_langgraph.py"
        dest.write_text(build_langgraph_stub_py(manifest), encoding="utf-8")
        written.append(dest)
    else:
        raise ValueError(f"Unknown export target: {target!r}")

    return written
