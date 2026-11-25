<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [💰 Finance and accounting](../README.md) › **Accounts Payable Agent**

# 💰 Accounts Payable Agent

![id: finance/accounts-payable](https://img.shields.io/badge/id-finance%2Faccounts--payable-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P1](https://img.shields.io/badge/priority-P1-8b5cf6?style=flat-square) ![tier: composite](https://img.shields.io/badge/tier-composite-0d9488?style=flat-square) ![safety: S4](https://img.shields.io/badge/safety-S4-dc2626?style=flat-square) ![autonomy: L2](https://img.shields.io/badge/autonomy-L2-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Matches parsed invoices against PO/receipt totals and prepares an approval queue (no autonomous payment).

Matches parsed invoices against PO/receipt totals and prepares an approval queue (no autonomous payment).

| | |
|---|---|
| **Use it when** | Performing accounts payable agent tasks cleanly within typed I/O contracts. |
| **Don't use it when** | Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions. |
| **Pattern** | `augmented-llm` |
| **Modality** | text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `finance` `accounts-payable` |

## 🚀 Quick start

```bash
afe add finance/accounts-payable          # copy this agent (and the agents it uses) into ./agents
afe info finance/accounts-payable         # manifest, tools, safety level
afe test finance/accounts-payable         # run its 10 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"invoice_total": 1000, "po_total": 900, "vendor": "Vendor 8"}  # from evals/cases.jsonl
result = AgentRunner().run("finance/accounts-payable", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Accounts Payable Agent"]
    AG --> OUT[/"Output"/]
    AG -. uses .-> D0["documents/invoice-receipt-parser"]
    AG -. tool .-> T0[("afe/accounting")]
    AG -. needs approval .-> H0{{"human approval: approve_payment_batch"}}
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S4** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern, calling the agents it composes.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `invoice_total` | `number` | ✅ |  |
| `po_total` | `number` | ✅ |  |
| `vendor` | `string` | ✅ |  |
| `approve` | `boolean` |  | default `false` |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `matched` | `boolean` | ✅ |  |
| `variance` | `number` | ✅ |  |
| `status` | `string` | ✅ |  |

## 🔗 Composes with

- **Uses:** [`documents/invoice-receipt-parser`](../../../action/documents/invoice-receipt-parser/README.md)
- **Used by agents:** _none yet_
- **In teams:** [`accounts-payable-team`](../../../../teams/accounts-payable-team/README.md)
- **In recipes:** [`invoice-automation`](../../../../recipes/invoice-automation/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/accounting`](../../../../mcp-servers/accounting/README.md) | ✅ | Read-only ledger inspection, reconciliation matching, and staged AP/expense drafts. |

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S4** — High stakes: Mandatory human sign-off, immutable audit log, no autonomous mode |
| **Autonomy** | **L2** — acts with per-action approval |
| **Side effects** | `finance-action` |
| **Needs approval for** | `approve_payment_batch` |
| **Handles personal data** | yes · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.03 max |
| **Safety review** | [SAFETY_REVIEW.md](SAFETY_REVIEW.md) |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **10 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test finance/accounts-payable`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bfinance/accounts-payable%5D%20) about this agent.

<!-- afe:end-generated -->
