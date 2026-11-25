<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [🧭 Orchestration and meta-agents](../README.md) › **Intent Router**

# 🧭 Intent Router

![id: orchestration/router](https://img.shields.io/badge/id-orchestration%2Frouter-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: atomic](https://img.shields.io/badge/tier-atomic-0d9488?style=flat-square) ![safety: S0](https://img.shields.io/badge/safety-S0-16a34a?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Classifies a user request and selects the best matching agent or team with extracted arguments.

Routes incoming natural-language requests to the right specialized agent ID and structured starter arguments.

| | |
|---|---|
| **Use it when** | Dispatching user intents across multiple specialized agents. |
| **Don't use it when** | Single-agent pipelines where the target agent is already known. |
| **Pattern** | `routing` |
| **Modality** | text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `orchestration` `router` |

## 🚀 Quick start

```bash
afe add orchestration/router          # copy this agent (and the agents it uses) into ./agents
afe info orchestration/router         # manifest, tools, safety level
afe test orchestration/router         # run its 50 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"request": "Please summarize this 10-page PDF"}  # from evals/cases.jsonl
result = AgentRunner().run("orchestration/router", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Intent Router"]
    AG --> OUT[/"Output"/]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S0** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `routing` pattern.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `request` | `string` | ✅ | min length 1 |
| `candidates` | array of `object` |  |  |
| `top_k` | `integer` |  | default `3`; min 1 |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `agent_id` | `string` | ✅ |  |
| `arguments` | `object` | ✅ |  |
| `confidence` | `number` | ✅ | min 0; max 1 |
| `alternatives` | array of `object` |  |  |

## 🔗 Composes with

- **Uses:** _none (atomic building block)_
- **Used by agents:** [`orchestration/supervisor`](../supervisor/README.md)
- **In teams:** [`voice-concierge`](../../../../teams/voice-concierge/README.md)

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
| **Run limits** | 10 steps · 60 s · $0.02 max |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **50 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test orchestration/router`

## 🧠 Model requirements

- **Needs:** `structured_output`
- **Context:** 8,000+ tokens
- **Tested with:** `frontier-large`, `frontier-small`, `open-weights-8b`
- **Exports:** `python`, `typescript`, `mcp-server`, `a2a-card`, `agent-skill`, `subagent`

## ⚠️ Limitations

Deterministic offline fallback operates heuristically; connect a live model provider for complex semantic cases.

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Borchestration/router%5D%20) about this agent.

<!-- afe:end-generated -->
