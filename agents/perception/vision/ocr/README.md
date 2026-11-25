<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [👁️ Vision and images](../README.md) › **Text Extractor (OCR)**

# 👁️ Text Extractor (OCR)

![id: vision/ocr](https://img.shields.io/badge/id-vision%2Focr-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: atomic](https://img.shields.io/badge/tier-atomic-0d9488?style=flat-square) ![safety: S1](https://img.shields.io/badge/safety-S1-65a30d?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Extracts printed and handwritten text with layout blocks from images and scans.

Converts document images and scanned receipts into clean text and structured layout lines.

| | |
|---|---|
| **Use it when** | Reading scanned PDFs, receipts, whiteboards, and IDs. |
| **Don't use it when** | Already-digital text files. |
| **Pattern** | `augmented-llm` |
| **Modality** | vision, text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `vision` `ocr` |

## 🚀 Quick start

```bash
afe add vision/ocr          # copy this agent (and the agents it uses) into ./agents
afe info vision/ocr         # manifest, tools, safety level
afe test vision/ocr         # run its 50 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"image": {"text_hint": "Invoice #101\nTotal INR 500"}}  # from evals/cases.jsonl
result = AgentRunner().run("vision/ocr", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Text Extractor (OCR)"]
    AG --> OUT[/"Output"/]
    AG -. tool .-> T0[("afe/ocr")]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S1** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `image` | [`ImageSource`](../../../../spec/types/ImageSource.schema.json) | ✅ |  |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `text` | `string` | ✅ |  |
| `blocks` | array of `object` | ✅ |  |

## 🔗 Composes with

- **Uses:** _none (atomic building block)_
- **Used by agents:** [`agriculture/crop-doctor`](../../../industries/agriculture/crop-doctor/README.md), [`insurance/claims-adjuster-assistant`](../../../industries/insurance/claims-adjuster-assistant/README.md), [`insurance/underwriting-assistant`](../../../industries/insurance/underwriting-assistant/README.md), [`manufacturing/ehs-incident-agent`](../../../industries/manufacturing/ehs-incident-agent/README.md), [`manufacturing/predictive-maintenance`](../../../industries/manufacturing/predictive-maintenance/README.md), [`manufacturing/quality-inspector`](../../../industries/manufacturing/quality-inspector/README.md), [`real-estate/maintenance-request-agent`](../../../industries/real-estate/maintenance-request-agent/README.md), [`real-estate/property-search-assistant`](../../../industries/real-estate/property-search-assistant/README.md), [`real-estate/property-valuator`](../../../industries/real-estate/property-valuator/README.md), [`real-estate/tenant-screening-assistant`](../../../industries/real-estate/tenant-screening-assistant/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/ocr`](../../../../mcp-servers/ocr/README.md) | ✅ | Printed and handwritten text extraction with layout bounding boxes. |

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S1** — Reads data: Read-only tool scopes; untrusted input screened for prompt injection |
| **Autonomy** | **L1** — human executes |
| **Side effects** | none |
| **Needs approval for** | nothing |
| **Handles personal data** | no · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.03 max |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **50 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test vision/ocr`

## 🧠 Model requirements

- **Needs:** `vision`, `structured_output`
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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bvision/ocr%5D%20) about this agent.

<!-- afe:end-generated -->
