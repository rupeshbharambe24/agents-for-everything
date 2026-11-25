# Meeting Notetaker `meetings/meeting-notetaker`

beta · P0 · composite · safety S1 · autonomy L1

## What it does
Composes speech-to-text and summarization to capture clean meeting records.

## When to use / not use
- **Use when:** Turning recorded meetings or transcripts into crisp notes.
- **Do not use when:** Extracting task records directly into trackers (pair with action-item-extractor).

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `meetings/meeting-notetaker` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add meetings/meeting-notetaker
afe test meetings/meeting-notetaker
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/stt

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test meetings/meeting-notetaker` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
