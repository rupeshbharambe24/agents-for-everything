<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [🎙️ Voice and speech](../README.md) › **Narrator**

# 🎙️ Narrator

![id: voice/text-to-speech](https://img.shields.io/badge/id-voice%2Ftext--to--speech-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: atomic](https://img.shields.io/badge/tier-atomic-0d9488?style=flat-square) ![safety: S0](https://img.shields.io/badge/safety-S0-16a34a?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Natural speech synthesis from text with locale, speed, and tone control.

Synthesizes spoken responses, read-backs, and multilingual confirmations from text.

| | |
|---|---|
| **Use it when** | Reading responses, confirmations, or missing-field prompts aloud. |
| **Don't use it when** | Text-only headless pipelines. |
| **Pattern** | `augmented-llm` |
| **Modality** | voice, text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en`, `hi`, `ta`, `te`, `bn`, `mr`, `es`, `fr` |
| **Tags** | `voice` `text-to-speech` |

## 🚀 Quick start

```bash
afe add voice/text-to-speech          # copy this agent (and the agents it uses) into ./agents
afe info voice/text-to-speech         # manifest, tools, safety level
afe test voice/text-to-speech         # run its 58 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"text": ""}  # from evals/cases.jsonl
result = AgentRunner().run("voice/text-to-speech", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Narrator"]
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
| `locale` | `string` |  | default `"en"` |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `audio_uri` | `string` | ✅ |  |
| `spoken_text` | `string` | ✅ |  |
| `locale` | `string` | ✅ |  |
| `duration_seconds` | `number` |  |  |

## 🔗 Composes with

- **Uses:** _none (atomic building block)_
- **Used by agents:** [`accessibility/screen-narrator`](../../accessibility/screen-narrator/README.md), [`accessibility/sign-language-interpreter`](../../accessibility/sign-language-interpreter/README.md), [`agriculture/crop-doctor`](../../../industries/agriculture/crop-doctor/README.md), [`audio/audiobook-producer`](../../audio/audiobook-producer/README.md), [`banking/financial-literacy-guide`](../../../industries/banking/financial-literacy-guide/README.md), [`education/language-partner`](../../../life/education/language-partner/README.md), [`government/citizen-services-assistant`](../../../industries/government/citizen-services-assistant/README.md), [`manufacturing/maintenance-copilot`](../../../industries/manufacturing/maintenance-copilot/README.md), [`video/dubbing-agent`](../../video/dubbing-agent/README.md), [`voice/ivr-designer`](../ivr-designer/README.md), [`voice/live-interpreter`](../live-interpreter/README.md), [`voice/phone-call-agent`](../phone-call-agent/README.md), [`voice/realtime-voice-assistant`](../realtime-voice-assistant/README.md), [`voice/voice-form-filler`](../voice-form-filler/README.md), [`voice/voice-search`](../voice-search/README.md)
- **In teams:** [`voice-concierge`](../../../../teams/voice-concierge/README.md)
- **In recipes:** [`farmer-advisory`](../../../../recipes/farmer-advisory/README.md), [`voice-form-filling`](../../../../recipes/voice-form-filling/README.md)

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

- **58 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test voice/text-to-speech`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bvoice/text-to-speech%5D%20) about this agent.

<!-- afe:end-generated -->
