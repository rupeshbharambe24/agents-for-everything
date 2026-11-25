<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [👁️ Vision and images](../README.md) › **ID Document Reader**

# 👁️ ID Document Reader

![id: vision/id-document-reader](https://img.shields.io/badge/id-vision%2Fid--document--reader-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P1](https://img.shields.io/badge/priority-P1-8b5cf6?style=flat-square) ![tier: atomic](https://img.shields.io/badge/tier-atomic-0d9488?style=flat-square) ![safety: S4](https://img.shields.io/badge/safety-S4-dc2626?style=flat-square) ![autonomy: L2](https://img.shields.io/badge/autonomy-L2-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Extracts identity card fields for consented KYC workflows with quality checks.

Extracts identity card fields for consented KYC workflows with quality checks.

| | |
|---|---|
| **Use it when** | Performing id document reader tasks cleanly within typed I/O contracts. |
| **Don't use it when** | Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions. |
| **Pattern** | `augmented-llm` |
| **Modality** | vision, text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `vision` `id-document-reader` |

## 🚀 Quick start

```bash
afe add vision/id-document-reader          # copy this agent (and the agents it uses) into ./agents
afe info vision/id-document-reader         # manifest, tools, safety level
afe test vision/id-document-reader         # run its 10 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"image": {"text_hint": "ID"}, "user_consent": true}  # from evals/cases.jsonl
result = AgentRunner().run("vision/id-document-reader", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["ID Document Reader"]
    AG --> OUT[/"Output"/]
    AG -. tool .-> T0[("afe/ocr")]
    AG -. needs approval .-> H0{{"human approval: verified_user_consent"}}
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S4** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `image` | `object` | ✅ |  |
| `user_consent` | `boolean` | ✅ |  |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `fields` | `object` | ✅ |  |
| `status` | `string` | ✅ |  |

## 🔗 Composes with

- **Uses:** _none (atomic building block)_
- **Used by agents:** [`banking/kyc-onboarding`](../../../industries/banking/kyc-onboarding/README.md)
- **In teams:** [`kyc-pipeline`](../../../../teams/kyc-pipeline/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/ocr`](../../../../mcp-servers/ocr/README.md) | ✅ | Printed and handwritten text extraction with layout bounding boxes. |

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S4** — High stakes: Mandatory human sign-off, immutable audit log, no autonomous mode |
| **Autonomy** | **L2** — acts with per-action approval |
| **Side effects** | `vision-action` |
| **Needs approval for** | `verified_user_consent` |
| **Handles personal data** | yes · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.03 max |
| **Safety review** | [SAFETY_REVIEW.md](SAFETY_REVIEW.md) |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **10 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test vision/id-document-reader`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bvision/id-document-reader%5D%20) about this agent.

<!-- afe:end-generated -->
