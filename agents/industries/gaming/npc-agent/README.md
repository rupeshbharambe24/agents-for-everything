<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [🎮 Gaming and interactive entertainment](../README.md) › **NPC Agent**

# 🎮 NPC Agent

![id: gaming/npc-agent](https://img.shields.io/badge/id-gaming%2Fnpc--agent-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P2](https://img.shields.io/badge/priority-P2-a78bfa?style=flat-square) ![tier: composite](https://img.shields.io/badge/tier-composite-0d9488?style=flat-square) ![safety: S0](https://img.shields.io/badge/safety-S0-16a34a?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Dynamic non-player character dialogue with memory, personality and game-rule constraints.

Dynamic non-player character dialogue with memory, personality and game-rule constraints.

| | |
|---|---|
| **Use it when** | You need single-purpose npc agent (game state + player → dialogue/actions). |
| **Don't use it when** | Actions exceed declared MCP tools or bypass required human sign-off. |
| **Pattern** | `orchestrator-workers` |
| **Modality** | gui, text |
| **Runtime** | interactive · memory: `session` |
| **Languages** | `en` |
| **Tags** | `gaming` `industries` `npc` |

## 🚀 Quick start

```bash
afe add gaming/npc-agent          # copy this agent (and the agents it uses) into ./agents
afe info gaming/npc-agent         # manifest, tools, safety level
afe test gaming/npc-agent         # run its 10 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"input": ""}  # from evals/cases.jsonl
result = AgentRunner().run("gaming/npc-agent", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["NPC Agent"]
    AG --> OUT[/"Output"/]
    AG -. uses .-> D0["memory/memory-retriever"]
    AG -. uses .-> D1["memory/memory-writer"]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S0** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `orchestrator-workers` pattern, calling the agents it composes.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `input` | `string` | ✅ | Primary task payload (game state + player → dialogue/actions) |
| `locale` | `string` |  | default `"en"` |
| `context` | `object` |  |  |
| `execute` | `boolean` |  | default `false` |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `result` | `string` | ✅ |  |
| `items` | array of `object` |  |  |
| `confidence` | `number` |  |  |
| `status` | `string` | ✅ |  |
| `locale` | `string` |  |  |

## 🔗 Composes with

- **Uses:** [`memory/memory-retriever`](../../../core/memory/memory-retriever/README.md), [`memory/memory-writer`](../../../core/memory/memory-writer/README.md)
- **Used by agents:** _none yet_

## 🧰 Tools (MCP servers)

_No tools: this agent works only on its input._

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S0** — Pure computation: No external access; schema validation only |
| **Autonomy** | **L1** — human executes |
| **Side effects** | none |
| **Needs approval for** | nothing |
| **Handles personal data** | no · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.03 max |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **10 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test gaming/npc-agent`

## 🧠 Model requirements

- **Needs:** `structured_output`
- **Context:** 8,000+ tokens
- **Tested with:** `frontier-large`, `frontier-small`, `open-weights-8b`
- **Exports:** `python`, `typescript`, `mcp-server`, `a2a-card`, `agent-skill`, `subagent`

## ⚠️ Limitations

Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## 📁 Files

| File | Purpose |
|---|---|
| [`agent.yaml`](agent.yaml) | Manifest: the single source of truth |
| [`prompts/system.md`](prompts/system.md) | Instructions the model follows |
| [`schemas/`](schemas/input.schema.json) | Input and output contracts |
| [`tools.yaml`](tools.yaml) | MCP servers and permissions |
| [`evals/`](evals/eval.yaml) | Test cases, rubric, targets |
| `impl/` | Python and TypeScript implementations |
| [`examples/basic.md`](examples/basic.md) | Worked example |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history |

## 🤝 Help improve this agent

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bgaming/npc-agent%5D%20) about this agent.

<!-- afe:end-generated -->
