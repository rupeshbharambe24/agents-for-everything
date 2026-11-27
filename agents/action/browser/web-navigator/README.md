<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [🌐 Browser and web automation](../README.md) › **Browser Operator**

# 🌐 Browser Operator

![id: browser/web-navigator](https://img.shields.io/badge/id-browser%2Fweb--navigator-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: composite](https://img.shields.io/badge/tier-composite-0d9488?style=flat-square) ![safety: S3](https://img.shields.io/badge/safety-S3-ea580c?style=flat-square) ![autonomy: L2](https://img.shields.io/badge/autonomy-L2-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Completes multi-step web tasks safely using accessibility trees and screenshots with injection guards.

Navigates web workflows step by step, screens page content for prompt injections, and stops before side effects.

| | |
|---|---|
| **Use it when** | Multi-page interactive web workflows requiring navigation and confirmation. |
| **Don't use it when** | Simple read-only HTTP fetches. |
| **Pattern** | `react` |
| **Modality** | gui, text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `browser` `web-navigator` |

## 🚀 Quick start

```bash
afe add browser/web-navigator          # copy this agent (and the agents it uses) into ./agents
afe info browser/web-navigator         # manifest, tools, safety level
afe test browser/web-navigator         # run its 63 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"goal": "Submit application", "start_url": "https://example.org/form"}  # from evals/cases.jsonl
result = AgentRunner().run("browser/web-navigator", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Browser Operator"]
    AG --> OUT[/"Output"/]
    AG -. uses .-> D0["vision/screenshot-understander"]
    AG -. uses .-> D1["guardrails/prompt-injection-detector"]
    AG -. tool .-> T0[("afe/browser")]
    AG -. needs approval .-> H0{{"human approval: submit"}}
    AG -. needs approval .-> H1{{"human approval: purchase"}}
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S3** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `react` pattern, calling the agents it composes.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `goal` | `string` | ✅ |  |
| `start_url` | `string` | ✅ |  |
| `page_text` | `string` |  |  |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `status` | `string` | ✅ |  |
| `trace_steps` | array of `string` | ✅ |  |
| `injection_safe` | `boolean` | ✅ |  |

## 🔗 Composes with

- **Uses:** [`vision/screenshot-understander`](../../../perception/vision/screenshot-understander/README.md), [`guardrails/prompt-injection-detector`](../../../core/guardrails/prompt-injection-detector/README.md)
- **Used by agents:** [`browser/booking-agent`](../booking-agent/README.md), [`browser/checkout-assistant`](../checkout-assistant/README.md), [`browser/web-tester`](../web-tester/README.md), [`browser/web-to-api`](../web-to-api/README.md)
- **In teams:** [`web-qa-team`](../../../../teams/web-qa-team/README.md)
- **In recipes:** [`ai-qa-engineer`](../../../../recipes/ai-qa-engineer/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/browser`](../../../../mcp-servers/browser/README.md) | ✅ | Playwright-based browser navigation, accessibility-tree reading, and safe form filling. |

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S3** — External side effects: Human approval per action by default |
| **Autonomy** | **L2** — acts with per-action approval |
| **Side effects** | `browser-interaction` |
| **Needs approval for** | `submit`, `purchase` |
| **Handles personal data** | no · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.03 max |
| **Safety review** | [SAFETY_REVIEW.md](SAFETY_REVIEW.md) |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **63 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test browser/web-navigator`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bbrowser/web-navigator%5D%20) about this agent.

<!-- afe:end-generated -->
