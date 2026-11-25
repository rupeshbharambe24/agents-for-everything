# Concept Explainer `text/explainer`

prototype · P1 · atomic · safety S0 · autonomy L1

## What it does
Explains technical or domain concepts at a target reading level with examples.

## When to use / not use
- **Use when:** Performing concept explainer tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S0) and declared MCP server permissions.
3. Executes `text/explainer` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add text/explainer
afe test text/explainer
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
None

## Safety
- Safety tier: `S0`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test text/explainer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
