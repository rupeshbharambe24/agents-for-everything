# Transcript-based Editor `video/video-editor`

prototype · P2 · composite · safety S2 · autonomy L2

## What it does
Edits video by editing the transcript or by instruction (cut, reorder, add b-roll).

## When to use / not use
- **Use when:** You need single-purpose transcript-based editor (video + instructions → video).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `video/video-editor` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add video/video-editor
afe test video/video-editor
```

## Composes with
voice/speech-to-text, vision/screenshot-understander

## Tools required
afe/stt, afe/media

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `True`

## Evaluation
Run `afe test video/video-editor` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
