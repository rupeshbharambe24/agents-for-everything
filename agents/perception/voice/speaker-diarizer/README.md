# Speaker Diarizer `voice/speaker-diarizer`

prototype · P1 · atomic · safety S1 · autonomy L1

## What it does
Labels speaker turns and timestamps in multi-speaker audio transcripts.

## When to use / not use
- **Use when:** Performing speaker diarizer tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `voice/speaker-diarizer` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add voice/speaker-diarizer
afe test voice/speaker-diarizer
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
Run `afe test voice/speaker-diarizer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
