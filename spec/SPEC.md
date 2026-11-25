# `afe/v1` Specification — Agents for Everything

`afe/v1` is the canonical, framework-neutral contract governing agents, multi-agent teams, end-to-end recipes, and shared MCP tools in `agents-for-everything`.

## 1. Design Principles

1. **One agent, one job.** Atomic agents execute a single focused capability with optional tool calls, never calling other agents directly. Composite agents orchestrate atomic agents into a single user-facing job.
2. **Contracts first.** Every agent defines JSON Schema 2020-12 files (`schemas/input.schema.json` and `schemas/output.schema.json`) reusing shared definitions in `spec/types/` (`afe://types/<TypeName>`).
3. **Model- and framework-agnostic.** Manifests declare required *capabilities* (`tool_use`, `structured_output`, `vision`, `native_audio`), never hardcoded proprietary model IDs.
4. **Safety & human control by default.** Every agent declares an honest safety tier (`S0`–`S4`) and autonomy level (`L0`–`L4`). Side effects above `S2` require explicit approval gates unless overridden by verified policy.
5. **Tested or it doesn't advance.** Agents progress from `spec` -> `prototype` (>= 10 passing eval cases) -> `beta` (>= 50 cases + 2 adapters + S3/S4 safety review) -> `stable` (used in >= 1 recipe).

## 2. Manifest Kinds

| Kind | File | Schema |
|---|---|---|
| `Agent` | `agents/<family>/<category>/<slug>/agent.yaml` | `spec/agent.schema.json` |
| `Team` | `teams/<slug>/team.yaml` | `spec/team.schema.json` |
| `Recipe` | `recipes/<slug>/recipe.yaml` | `spec/recipe.schema.json` |
| `Tools` | `agents/.../tools.yaml` | `spec/tools.schema.json` |
| `MCPServer` | `mcp-servers/<slug>/server.yaml` | `spec/tools.schema.json` |

## 3. Identifiers & Aliases

- Agent IDs have the short form `<category>/<slug>` (e.g. `voice/voice-form-filler`). Category names are globally unique across all 8 families so folders can reorganize without breaking IDs.
- IDs are immutable once published. Renames or deprecations must be recorded in `registry/aliases.yaml`.

## 4. Safety Levels (`S0`–`S4`) & Autonomy (`L0`–`L4`)

| Level | Safety Meaning | Default Control |
|---|---|---|
| `S0` | Pure computation, zero external I/O | Schema validation |
| `S1` | Reads external or private data | Read-only scope + prompt-injection check |
| `S2` | Reversible local writes / unsubmitted drafts | Diff/undo + structured audit log |
| `S3` | External side effects (send, post, write APIs, shell) | Human approval before each action |
| `S4` | High stakes (money, legal, clinical, identity, delete) | Mandatory human approval + audit log + disclaimers |

| Level | Autonomy Meaning |
|---|---|
| `L0` | Suggest only |
| `L1` | Human triggers & executes |
| `L2` | Acts with per-action human confirmation |
| `L3` | Acts within policy, escalates exceptions |
| `L4` | Autonomous within bounded sandbox |

## 5. Composition & Exports

Two agents `A -> B` are **schema-compatible** when `A`'s `output.schema.json` satisfies `B`'s `input.schema.json` required fields/types (verified automatically by `afe validate` and compiled into `registry/compatibility-graph.json`).

Every valid agent can be exported at build or CLI time via `afe export` into:
- **A2A Agent Card** (`agent-card.json`)
- **Agent Skill** (`SKILL.md` folder)
- **MCP Server wrapper** (`mcp-server`)
- **Coding Assistant Subagent** (`subagent`)
- **Framework Adapter** (`langgraph`, `openai-agents`, `claude-agent-sdk`, `google-adk`, `ms-agent-framework`, `crewai`, `mastra`)
