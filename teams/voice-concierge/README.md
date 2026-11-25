<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [👥 Teams](../../README.md#-ready-made-teams) › **Voice Concierge Team**

# 👥 Voice Concierge Team

![team: voice-concierge](https://img.shields.io/badge/team-voice--concierge-0f172a?style=flat-square) ![pattern: routing](https://img.shields.io/badge/pattern-routing-0d9488?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P0](https://img.shields.io/badge/priority-P0-7c3aed?style=flat-square) ![safety: S1](https://img.shields.io/badge/safety-S1-65a30d?style=flat-square)

> Voice in, intent routing and action execution, and spoken response out.

## 🔀 Workflow

```mermaid
flowchart LR
    speech_to_text["Transcriber"] --> router["Intent Router"]
    router["Intent Router"] --> voice_command["Voice Command Interpreter"]
    voice_command["Voice Command Interpreter"] --> text_to_speech["Narrator"]
```

Starts at `voice/speech-to-text`.

## 🧑‍🤝‍🧑 Members

| Agent | What it does | Safety |
|---|---|:---:|
| [`voice/speech-to-text`](../../agents/perception/voice/speech-to-text/README.md) | Batch or streaming speech recognition with punctuation, language detection, and code-switching. | S1 |
| [`orchestration/router`](../../agents/core/orchestration/router/README.md) | Classifies a user request and selects the best matching agent or team with extracted arguments. | S0 |
| [`voice/voice-command`](../../agents/perception/voice/voice-command/README.md) | Maps spoken commands to structured app actions or function calls. | S1 |
| [`voice/text-to-speech`](../../agents/perception/voice/text-to-speech/README.md) | Natural speech synthesis from text with locale, speed, and tone control. | S0 |

## 🚀 Try it

```bash
afe graph voice-concierge   # print the workflow and check that agent contracts fit
for a in voice/speech-to-text orchestration/router voice/voice-command voice/text-to-speech; do afe add $a; done   # copy every member
```

Files: [`team.yaml`](team.yaml) · [`schemas/`](schemas) · [`evals/`](evals)

<!-- afe:end-generated -->
