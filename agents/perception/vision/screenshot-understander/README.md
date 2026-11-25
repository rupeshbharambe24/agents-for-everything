# Screen Parser `vision/screenshot-understander`

beta · P0 · atomic · safety S1 · autonomy L1

## What it does
Gives desktop and browser agents a structured element map from screen pixels.

## When to use / not use
- **Use when:** GUI/computer-use automation where DOM/accessibility trees are unavailable.
- **Do not use when:** APIs or semantic web DOMs where HTML suffices.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `vision/screenshot-understander` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add vision/screenshot-understander
afe test vision/screenshot-understander
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
Run `afe test vision/screenshot-understander` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
