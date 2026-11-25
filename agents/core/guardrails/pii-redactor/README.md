<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [🛡️ Guardrails, trust and safety](../README.md) › **PII Redactor**

# 🛡️ PII Redactor

![id: guardrails/pii-redactor](https://img.shields.io/badge/id-guardrails%2Fpii--redactor-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: atomic](https://img.shields.io/badge/tier-atomic-0d9488?style=flat-square) ![safety: S0](https://img.shields.io/badge/safety-S0-16a34a?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Detects and masks personal data (emails, phones, Aadhaar, PAN, SSN, card numbers) reversibly.

Protects privacy before prompts leave trust boundaries or enter logs/traces.

| | |
|---|---|
| **Use it when** | Pre-processing user transcripts, logs, invoices, or support tickets. |
| **Don't use it when** | Already-anonymized synthetic identifiers. |
| **Pattern** | `augmented-llm` |
| **Modality** | text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `guardrails` `pii-redactor` |

## 🚀 Quick start

```bash
afe add guardrails/pii-redactor          # copy this agent (and the agents it uses) into ./agents
afe info guardrails/pii-redactor         # manifest, tools, safety level
afe test guardrails/pii-redactor         # run its 50 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"text": "SSN 123-45-6789"}  # from evals/cases.jsonl
result = AgentRunner().run("guardrails/pii-redactor", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["PII Redactor"]
    AG --> OUT[/"Output"/]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S0** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `text` | `string` | ✅ |  |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `redacted_text` | `string` | ✅ |  |
| `redaction_map` | `object` | ✅ |  |
| `pii_found` | array of `string` | ✅ |  |

## 🔗 Composes with

- **Uses:** _none (atomic building block)_
- **Used by agents:** [`banking/cashflow-lending-analyst`](../../../industries/banking/cashflow-lending-analyst/README.md), [`banking/collections-assistant`](../../../industries/banking/collections-assistant/README.md), [`banking/dispute-chargeback-handler`](../../../industries/banking/dispute-chargeback-handler/README.md), [`banking/grievance-redressal`](../../../industries/banking/grievance-redressal/README.md), [`banking/model-risk-validator`](../../../industries/banking/model-risk-validator/README.md), [`banking/regulatory-return-preparer`](../../../industries/banking/regulatory-return-preparer/README.md), [`documents/doc-redactor`](../../../action/documents/doc-redactor/README.md), [`hr/interview-scheduler`](../../../business/hr/interview-scheduler/README.md)
- **In recipes:** [`chat-with-your-docs`](../../../../recipes/chat-with-your-docs/README.md), [`voice-form-filling`](../../../../recipes/voice-form-filling/README.md)

## 🧰 Tools (MCP servers)

_No tools: this agent works only on its input._

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S0** — Pure computation: No external access; schema validation only |
| **Autonomy** | **L1** — human executes |
| **Side effects** | none |
| **Needs approval for** | nothing |
| **Handles personal data** | yes · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.02 max |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **50 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test guardrails/pii-redactor`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bguardrails/pii-redactor%5D%20) about this agent.

<!-- afe:end-generated -->
