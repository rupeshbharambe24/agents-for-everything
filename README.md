# Agents for Everything (`agents-for-everything`)

> **One agent for every real-world task. Combine them like building blocks to build anything.**

`agents-for-everything` is an open-source, framework-agnostic, spec-first library of **single-purpose (atomic) and composite AI agents**, multi-agent **teams**, shared **MCP servers**, and runnable **product recipes**. Every agent has typed JSON Schema inputs/outputs, explicit safety levels (`S0`–`S4`), automated eval suites, and portable exports (Python, TypeScript, Agent Skills `SKILL.md`, A2A Agent Cards, MCP server wrappers, and coding-assistant subagents).

---

## Why This Exists

Most AI repositories are either link lists, unvalidated prompt dumps, or monolithic frameworks tied to a single SDK. `agents-for-everything` treats every AI capability like a composable building block:

- **One job per agent:** e.g. `voice/speech-to-text`, `text/structured-extractor`, `browser/web-form-filler`, `orchestration/human-approval-gate`.
- **Snap together via typed contracts:** Every agent declares `schemas/input.schema.json` and `schemas/output.schema.json` using shared types in `spec/types/`.
- **Model- and framework-agnostic:** Runs out-of-the-box via dependency-light `core-python` and `core-typescript`, or adapts to LangGraph, OpenAI Agents SDK, Claude Agent SDK, Google ADK, CrewAI, Microsoft Agent Framework, and Mastra.
- **Local-first & multilingual:** Supports Ollama/local open-weights endpoints alongside OpenAI, Anthropic, and Gemini, plus offline deterministic mock/replay mode for CI.
- **Copy-in or install (`afe add`):** Pull individual agent folders into your own project—`shadcn/ui`-style—without installing 500 packages.

---

## Quick Start

### Python (`uv` or `pip`)

```bash
# Run CLI directly from workspace
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m afe_cli validate
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m afe_cli search "voice form"
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m afe_cli info voice/voice-form-filler
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m afe_cli test voice/voice-form-filler
```

Or install in editable mode with `uv`:

```bash
uv sync
afe validate
afe test voice/voice-form-filler
afe run text/summarizer --input '{"text":"Agents for Everything builds composable single-purpose AI agents."}'
afe add voice/voice-form-filler --dest ./my-app/agents
afe export voice/speech-to-text --as skill --out ./exports
```

### TypeScript / Node.js (`v22.6+` / `v26+`)

```bash
node --test packages/core-typescript/tests/*.test.ts
```

---

## Repository Layout

```text
agents-for-everything/
├── BLUEPRINT.md              # Master architecture, 571-agent catalog & roadmap
├── CATALOG.md                # Auto-generated catalog from all agent.yaml manifests
├── AGENTS.md                 # Guidelines for AI coding agents contributing here
├── spec/                     # afe/v1 JSON Schemas, shared I/O types & SPEC.md
├── agents/                   # Atomic & composite agents organized by family/category
├── teams/                    # Reusable multi-agent workflow graphs (team.yaml)
├── recipes/                  # End-to-end runnable product blueprints
├── mcp-servers/              # Shared Model Context Protocol (MCP) tool servers
├── packages/
│   ├── core-python/          # `agents-for-everything` Python runtime
│   ├── core-typescript/      # `@agents-for-everything/core` TypeScript runtime
│   └── adapters/             # LangGraph, OpenAI, Claude, ADK, MS, CrewAI, Mastra
├── cli/                      # `agents-for-everything` / `afe` CLI
├── templates/                # Scaffolds used by `afe new`
├── evals/                    # Eval harness & multilingual synthetic datasets
├── registry/                 # Auto-generated catalog.json & compatibility-graph.json
├── radar/                    # Monthly ecosystem radar tracking new protocols & tools
├── docs/                     # Guides, concepts, ADRs & blueprint mirror
└── scripts/                  # Manifest validator, catalog builder, link & radar tools
```

---

## Safety & Maturity Model

| Safety Level | Scope | Default Control |
|---|---|---|
| **S0** | Pure computation, no external access | None |
| **S1** | Read-only external/private data | Scoped read access + injection screening |
| **S2** | Reversible local writes / drafts | Rollback/undo + action logging |
| **S3** | External side effects (send, post, shell) | Human approval per action by default |
| **S4** | Money, legal, health, identity, deletion | Mandatory human approval + audit trail |

Maturity badges: `spec` -> `prototype` (>= 10 passing eval cases) -> `beta` (>= 50 cases + 2 adapters) -> `stable` (used in >= 1 recipe).

---

## Documentation

- [Master Blueprint](BLUEPRINT.md)
- [Generated Agent Catalog](CATALOG.md)
- [afe/v1 Specification](spec/SPEC.md)
- [Contributing Guide](CONTRIBUTING.md)
- [Security & Agent Safety Policy](SECURITY.md)

---

## License

Apache-2.0 — see [LICENSE](LICENSE).
