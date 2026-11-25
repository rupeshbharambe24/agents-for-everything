# Visual Q&A `vision/visual-qa`

beta · P0 · atomic · safety S1 · autonomy L1

## What it does
Inspects an image and answers factual visual questions without inventing unseen details.

## When to use / not use
- **Use when:** Asking specific questions about photos, charts, or diagrams.
- **Do not use when:** Pure text Q&A.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `vision/visual-qa` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add vision/visual-qa
afe test vision/visual-qa
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
None

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test vision/visual-qa` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
