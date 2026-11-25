# Lecture to Notes `video/lecture-to-notes`

prototype · P2 · composite · safety S1 · autonomy L1

## What it does
Turns lectures into structured notes, slides index and a quiz.

## When to use / not use
- **Use when:** You need single-purpose lecture to notes (video → notes + quiz).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `video/lecture-to-notes` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add video/lecture-to-notes
afe test video/lecture-to-notes
```

## Composes with
voice/speech-to-text, vision/screenshot-understander

## Tools required
afe/stt

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `False`

## Evaluation
Run `afe test video/lecture-to-notes` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
