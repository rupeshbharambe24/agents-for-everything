# Knowledge Base Writer `support/kb-writer`

prototype · P1 · composite · safety S2 · autonomy L2

## What it does
Converts resolved support tickets into clean KB articles and highlights missing docs.

## When to use / not use
- **Use when:** Performing knowledge base writer tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `support/kb-writer` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add support/kb-writer
afe test support/kb-writer
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/vector-store

## Safety
- Safety tier: `S2`
- Side effects: ['support-action']
- Approval gates: ['none']

## Evaluation
Run `afe test support/kb-writer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
