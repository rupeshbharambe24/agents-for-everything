<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [🖥️ Computer use and desktop](../README.md) › **Desktop Operator**

# 🖥️ Desktop Operator

![id: computer-use/desktop-operator](https://img.shields.io/badge/id-computer--use%2Fdesktop--operator-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P1](https://img.shields.io/badge/priority-P1-8b5cf6?style=flat-square) ![tier: composite](https://img.shields.io/badge/tier-composite-0d9488?style=flat-square) ![safety: S3](https://img.shields.io/badge/safety-S3-ea580c?style=flat-square) ![autonomy: L2](https://img.shields.io/badge/autonomy-L2-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Operates native desktop apps via screenshots, mouse, and keyboard with approval gates.

Operates native desktop apps via screenshots, mouse, and keyboard with approval gates.

| | |
|---|---|
| **Use it when** | Performing desktop operator tasks cleanly within typed I/O contracts. |
| **Don't use it when** | Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions. |
| **Pattern** | `augmented-llm` |
| **Modality** | gui, vision |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `computer-use` `desktop-operator` |

## 🚀 Quick start

```bash
afe add computer-use/desktop-operator          # copy this agent (and the agents it uses) into ./agents
afe info computer-use/desktop-operator         # manifest, tools, safety level
afe test computer-use/desktop-operator         # run its 10 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"input": "Sample desktop-operator request #1"}  # from evals/cases.jsonl
result = AgentRunner().run("computer-use/desktop-operator", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Desktop Operator"]
    AG --> OUT[/"Output"/]
    AG -. uses .-> D0["vision/screenshot-understander"]
    AG -. tool .-> T0[("afe/browser")]
    AG -. needs approval .-> H0{{"human approval: execute_gui_action"}}
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S3** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern, calling the agents it composes.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `input` | `string` | ✅ |  |
| `context` | `object` |  |  |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `result` | `string` | ✅ |  |
| `items` | array of `object` |  |  |
| `confidence` | `number` |  |  |
| `status` | `string` | ✅ |  |

## 🔗 Composes with

- **Uses:** [`vision/screenshot-understander`](../../../perception/vision/screenshot-understander/README.md)
- **Used by agents:** [`accessibility/voice-control-navigator`](../../../perception/accessibility/voice-control-navigator/README.md), [`computer-use/macro-recorder`](../macro-recorder/README.md), [`computer-use/mobile-operator`](../mobile-operator/README.md), [`computer-use/rpa-bridge`](../rpa-bridge/README.md), [`gaming/game-tester`](../../../industries/gaming/game-tester/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/browser`](../../../../mcp-servers/browser/README.md) | ✅ | Playwright-based browser navigation, accessibility-tree reading, and safe form filling. |

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S3** — External side effects: Human approval per action by default |
| **Autonomy** | **L2** — acts with per-action approval |
| **Side effects** | `computer-use-action` |
| **Needs approval for** | `execute_gui_action` |
| **Handles personal data** | no · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.03 max |
| **Safety review** | [SAFETY_REVIEW.md](SAFETY_REVIEW.md) |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **10 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test computer-use/desktop-operator`

## 🧠 Model requirements

- **Needs:** `structured_output`
- **Context:** 8,000+ tokens
- **Tested with:** `frontier-large`, `frontier-small`, `open-weights-8b`
- **Exports:** `python`, `typescript`, `mcp-server`, `a2a-card`, `agent-skill`, `subagent`

## ⚠️ Limitations

Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bcomputer-use/desktop-operator%5D%20) about this agent.

<!-- afe:end-generated -->
