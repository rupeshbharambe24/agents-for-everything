<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [🛡️ Guardrails, trust and safety](../README.md) › **Injection Detector**

# 🛡️ Injection Detector

![id: guardrails/prompt-injection-detector](https://img.shields.io/badge/id-guardrails%2Fprompt--injection--detector-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: atomic](https://img.shields.io/badge/tier-atomic-0d9488?style=flat-square) ![safety: S0](https://img.shields.io/badge/safety-S0-16a34a?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Scans untrusted content (web pages, emails, files, speech transcripts) for hidden prompt-injection instructions.

Detects indirect prompt injection attempts before untrusted data reaches downstream executors.

| | |
|---|---|
| **Use it when** | Before feeding external web pages, PDFs, emails, or speech inputs to tool-calling agents. |
| **Don't use it when** | Already-trusted internal static config. |
| **Pattern** | `augmented-llm` |
| **Modality** | text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en` |
| **Tags** | `guardrails` `prompt-injection-detector` |

## 🚀 Quick start

```bash
afe add guardrails/prompt-injection-detector          # copy this agent (and the agents it uses) into ./agents
afe info guardrails/prompt-injection-detector         # manifest, tools, safety level
afe test guardrails/prompt-injection-detector         # run its 50 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"content": "Mera naam Priya Sharma hai, PIN 411001."}  # from evals/cases.jsonl
result = AgentRunner().run("guardrails/prompt-injection-detector", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Injection Detector"]
    AG --> OUT[/"Output"/]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S0** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `content` | `string` | ✅ |  |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `is_safe` | `boolean` | ✅ |  |
| `risk_score` | `number` | ✅ | min 0; max 1 |
| `spans` | array of `string` | ✅ |  |

## 🔗 Composes with

- **Uses:** _none (atomic building block)_
- **Used by agents:** [`browser/web-navigator`](../../../action/browser/web-navigator/README.md), [`guardrails/red-teamer`](../red-teamer/README.md), [`security/pentest-assistant`](../../../builders/security/pentest-assistant/README.md), [`security/security-compliance-auditor`](../../../builders/security/security-compliance-auditor/README.md), [`security/siem-analyst`](../../../builders/security/siem-analyst/README.md), [`security/threat-intel-summarizer`](../../../builders/security/threat-intel-summarizer/README.md)
- **In recipes:** [`voice-form-filling`](../../../../recipes/voice-form-filling/README.md)

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
- **Run:** `afe test guardrails/prompt-injection-detector`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bguardrails/prompt-injection-detector%5D%20) about this agent.

<!-- afe:end-generated -->
