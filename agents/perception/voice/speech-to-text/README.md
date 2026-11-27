<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [🎙️ Voice and speech](../README.md) › **Transcriber**

# 🎙️ Transcriber

![id: voice/speech-to-text](https://img.shields.io/badge/id-voice%2Fspeech--to--text-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: atomic](https://img.shields.io/badge/tier-atomic-0d9488?style=flat-square) ![safety: S1](https://img.shields.io/badge/safety-S1-65a30d?style=flat-square) ![autonomy: L1](https://img.shields.io/badge/autonomy-L1-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Batch or streaming speech recognition with punctuation, language detection, and code-switching.

Converts audio streams or files into clean Transcript JSON across English and Indic/global languages.

| | |
|---|---|
| **Use it when** | Transcribing spoken audio or voice utterances into normalized text. |
| **Don't use it when** | Already-transcribed plain text. |
| **Pattern** | `augmented-llm` |
| **Modality** | voice, text |
| **Runtime** | interactive · memory: `none` |
| **Languages** | `en`, `hi`, `ta`, `te`, `bn`, `mr`, `es`, `fr`, `ar` |
| **Tags** | `voice` `speech-to-text` |

## 🚀 Quick start

```bash
afe add voice/speech-to-text          # copy this agent (and the agents it uses) into ./agents
afe info voice/speech-to-text         # manifest, tools, safety level
afe test voice/speech-to-text         # run its 62 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"audio": {"format": "text-simulated", "transcript_hint": ""}}  # from evals/cases.jsonl
result = AgentRunner().run("voice/speech-to-text", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Transcriber"]
    AG --> OUT[/"Output"/]
    AG -. tool .-> T0[("afe/stt")]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S1** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `augmented-llm` pattern.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `audio` | [`AudioSource`](../../../../spec/types/AudioSource.schema.json) | ✅ |  |
| `locale` | `string` |  | default `"en"` |

## 📤 Output

See [`output.schema.json`](schemas/output.schema.json).

## 🔗 Composes with

- **Uses:** _none (atomic building block)_
- **Used by agents:** [`accessibility/live-captioner`](../../accessibility/live-captioner/README.md), [`accessibility/voice-control-navigator`](../../accessibility/voice-control-navigator/README.md), [`audio/audio-search`](../../audio/audio-search/README.md), [`audio/audiobook-producer`](../../audio/audiobook-producer/README.md), [`audio/podcast-producer`](../../audio/podcast-producer/README.md), [`education/language-partner`](../../../life/education/language-partner/README.md), [`government/citizen-services-assistant`](../../../industries/government/citizen-services-assistant/README.md), [`healthcare/appointment-manager`](../../../industries/healthcare/appointment-manager/README.md), [`healthcare/clinical-trial-matcher`](../../../industries/healthcare/clinical-trial-matcher/README.md), [`healthcare/medical-evidence-agent`](../../../industries/healthcare/medical-evidence-agent/README.md), [`healthcare/medical-scribe`](../../../industries/healthcare/medical-scribe/README.md), [`healthcare/patient-intake`](../../../industries/healthcare/patient-intake/README.md), [`healthcare/prior-authorization`](../../../industries/healthcare/prior-authorization/README.md), [`manufacturing/maintenance-copilot`](../../../industries/manufacturing/maintenance-copilot/README.md), [`meetings/live-meeting-copilot`](../../../business/meetings/live-meeting-copilot/README.md), [`meetings/meeting-notetaker`](../../../business/meetings/meeting-notetaker/README.md), [`sales/sales-call-analyzer`](../../../business/sales/sales-call-analyzer/README.md), [`video/clip-generator`](../../video/clip-generator/README.md), [`video/dubbing-agent`](../../video/dubbing-agent/README.md), [`video/lecture-to-notes`](../../video/lecture-to-notes/README.md), [`video/live-stream-monitor`](../../video/live-stream-monitor/README.md), [`video/video-captioner`](../../video/video-captioner/README.md), [`video/video-editor`](../../video/video-editor/README.md), [`video/video-search`](../../video/video-search/README.md), [`video/video-summarizer`](../../video/video-summarizer/README.md), [`voice/ivr-designer`](../ivr-designer/README.md), [`voice/live-interpreter`](../live-interpreter/README.md), [`voice/phone-call-agent`](../phone-call-agent/README.md), [`voice/realtime-voice-assistant`](../realtime-voice-assistant/README.md), [`voice/voice-form-filler`](../voice-form-filler/README.md), [`voice/voice-note-summarizer`](../voice-note-summarizer/README.md), [`voice/voice-search`](../voice-search/README.md)
- **In teams:** [`voice-concierge`](../../../../teams/voice-concierge/README.md)
- **In recipes:** [`voice-form-filling`](../../../../recipes/voice-form-filling/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/stt`](../../../../mcp-servers/stt/README.md) | ✅ | Streaming and batch speech transcription with multilingual code-switching support. |

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S1** — Reads data: Read-only tool scopes; untrusted input screened for prompt injection |
| **Autonomy** | **L1** — human executes |
| **Side effects** | none |
| **Needs approval for** | nothing |
| **Handles personal data** | yes · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.03 max |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **62 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test voice/speech-to-text`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bvoice/speech-to-text%5D%20) about this agent.

<!-- afe:end-generated -->
