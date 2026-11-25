<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [📝 Language and text](../README.md) › **Translator**

# 📝 Translator

![id: text/translator](https://img.shields.io/badge/id-text%2Ftranslator-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: atomic](https://img.shields.io/badge/tier-atomic-0d9488?style=flat-square) ![safety: S0](https://img.shields.io/badge/safety-S0-16a34a?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Context-aware translation preserving formatting and glossaries across 100+ languages including Indic.

Translates text cleanly while preserving glossary terms and placeholders.

| | |
|---|---|
| **Use it when** | Multilingual localization and cross-language communication. |
| **Don't use it when** | Script-only transliteration. |
| **Pattern** | `augmented-llm` |
| **Modality** | text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en`, `hi`, `ta`, `te`, `bn`, `mr`, `es`, `fr`, `ar` |
| **Tags** | `text` `translator` |

## 🚀 Quick start

```bash
afe add text/translator          # copy this agent (and the agents it uses) into ./agents
afe info text/translator         # manifest, tools, safety level
afe test text/translator         # run its 50 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"text": "Hello", "target_language": "hi"}  # from evals/cases.jsonl
result = AgentRunner().run("text/translator", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Translator"]
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
| `target_language` | `string` | ✅ |  |
| `glossary` | `object` |  |  |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `translated_text` | `string` | ✅ |  |
| `target_language` | `string` | ✅ |  |

## 🔗 Composes with

- **Uses:** _none (atomic building block)_
- **Used by agents:** [`healthcare/appointment-manager`](../../../industries/healthcare/appointment-manager/README.md), [`healthcare/clinical-trial-matcher`](../../../industries/healthcare/clinical-trial-matcher/README.md), [`healthcare/prior-authorization`](../../../industries/healthcare/prior-authorization/README.md), [`travel/flight-hotel-searcher`](../../../life/travel/flight-hotel-searcher/README.md), [`travel/local-guide`](../../../life/travel/local-guide/README.md), [`video/dubbing-agent`](../../../perception/video/dubbing-agent/README.md), [`video/video-captioner`](../../../perception/video/video-captioner/README.md), [`voice/live-interpreter`](../../../perception/voice/live-interpreter/README.md)

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

- **50 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test text/translator`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Btext/translator%5D%20) about this agent.

<!-- afe:end-generated -->
