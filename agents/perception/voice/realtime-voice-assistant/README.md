<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../../../README.md) › [📖 Catalog](../../../../CATALOG.md) › [🎙️ Voice and speech](../README.md) › **Real-time Voice Assistant**

# 🎙️ Real-time Voice Assistant

![id: voice/realtime-voice-assistant](https://img.shields.io/badge/id-voice%2Frealtime--voice--assistant-0f172a?style=flat-square) ![maturity: beta](https://img.shields.io/badge/maturity-beta-2563eb?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![tier: composite](https://img.shields.io/badge/tier-composite-0d9488?style=flat-square) ![safety: S1](https://img.shields.io/badge/safety-S1-65a30d?style=flat-square) ![autonomy: L2](https://img.shields.io/badge/autonomy-L2-475569?style=flat-square) ![version: 0.1.0](https://img.shields.io/badge/version-0.1.0-64748b?style=flat-square)

> Full-duplex speech assistant with low latency, interruption handling, and tool dispatch.

Coordinates STT, command parsing, and TTS output in interactive voice sessions.

| | |
|---|---|
| **Use it when** | Interactive duplex voice experiences. |
| **Don't use it when** | Offline batch document processing. |
| **Pattern** | `handoff` |
| **Modality** | voice |
| **Runtime** | streaming · memory: `session` |
| **Languages** | `en` |
| **Tags** | `voice` `realtime-voice-assistant` |

## 🚀 Quick start

```bash
afe add voice/realtime-voice-assistant          # copy this agent (and the agents it uses) into ./agents
afe info voice/realtime-voice-assistant         # manifest, tools, safety level
afe test voice/realtime-voice-assistant         # run its 60 eval cases
```

```python
from agents_for_everything import AgentRunner

payload = {"audio": {"format": "text-simulated", "transcript_hint": ""}, "barge_in": false}  # from evals/cases.jsonl
result = AgentRunner().run("voice/realtime-voice-assistant", payload)
print(result.output)
```

> No `afe` command yet? See [Install the CLI](../../../../README.md#-quick-start).

## 🧩 How it works

```mermaid
flowchart LR
    IN[/"Input"/] --> AG["Real-time Voice Assistant"]
    AG --> OUT[/"Output"/]
    AG -. uses .-> D0["voice/speech-to-text"]
    AG -. uses .-> D1["voice/voice-command"]
    AG -. uses .-> D2["voice/text-to-speech"]
    AG -. tool .-> T0[("afe/stt")]
    AG -. tool .-> T1[("afe/tts")]
```

1. The input is validated against [`input.schema.json`](schemas/input.schema.json).
2. The runtime enforces safety level **S1** and allows only the tools declared in [`tools.yaml`](tools.yaml).
3. The agent follows its [system prompt](prompts/system.md) using the `handoff` pattern, calling the agents it composes.
4. The output is validated against [`output.schema.json`](schemas/output.schema.json) before it is returned.

## 📥 Input

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `audio` | [`AudioSource`](../../../../spec/types/AudioSource.schema.json) | ✅ |  |
| `locale` | `string` |  | default `"en"` |
| `barge_in` | `boolean` |  | default `false` |

## 📤 Output

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `reply_text` | `string` | ✅ |  |
| `audio_uri` | `string` | ✅ |  |
| `interrupted` | `boolean` | ✅ |  |

## 🔗 Composes with

- **Uses:** [`voice/speech-to-text`](../speech-to-text/README.md), [`voice/voice-command`](../voice-command/README.md), [`voice/text-to-speech`](../text-to-speech/README.md)
- **Used by agents:** [`banking/banking-voice-assistant`](../../../industries/banking/banking-voice-assistant/README.md)
- **In recipes:** [`vernacular-banking-helpline`](../../../../recipes/vernacular-banking-helpline/README.md)

## 🧰 Tools (MCP servers)

| Server | Required | What it provides |
|---|:---:|---|
| [`afe/stt`](../../../../mcp-servers/stt/README.md) | ✅ | Streaming and batch speech transcription with multilingual code-switching support. |
| [`afe/tts`](../../../../mcp-servers/tts/README.md) | ✅ | Natural multilingual text-to-speech synthesis with SSML and pacing controls. |

## 🛡️ Safety and limits

| | |
|---|---|
| **Safety level** | **S1** — Reads data: Read-only tool scopes; untrusted input screened for prompt injection |
| **Autonomy** | **L2** — acts with per-action approval |
| **Side effects** | none |
| **Needs approval for** | nothing |
| **Handles personal data** | no · retention: `none` |
| **Run limits** | 10 steps · 60 s · $0.03 max |

Full policy: [SECURITY.md](../../../../SECURITY.md).

## 📏 Evaluation

- **60 test cases** in [`evals/cases.jsonl`](evals/cases.jsonl), judged with [`evals/rubric.md`](evals/rubric.md).
- **Targets:** pass_rate ≥ 0.9 ([`eval.yaml`](evals/eval.yaml)).
- **Run:** `afe test voice/realtime-voice-assistant`

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

Add eval cases (especially non-English and edge cases), a live-model implementation, or a framework adapter. Start with the [contributing guide](../../../../CONTRIBUTING.md), or [open an issue](https://github.com/rupeshbharambe24/agents-for-everything/issues/new?title=%5Bvoice/realtime-voice-assistant%5D%20) about this agent.

<!-- afe:end-generated -->
