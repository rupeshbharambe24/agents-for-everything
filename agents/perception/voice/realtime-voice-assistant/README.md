# Real-time Voice Assistant `voice/realtime-voice-assistant`

prototype · P0 · composite · safety S1 · autonomy L2

## What it does
Coordinates STT, command parsing, and TTS output in interactive voice sessions.

## When to use / not use
- **Use when:** Interactive duplex voice experiences.
- **Do not use when:** Offline batch document processing.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `voice/realtime-voice-assistant` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add voice/realtime-voice-assistant
afe test voice/realtime-voice-assistant
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/stt, afe/tts

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test voice/realtime-voice-assistant` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
