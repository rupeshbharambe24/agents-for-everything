# Page Change Monitor `browser/page-change-monitor`

prototype · P1 · composite · safety S1 · autonomy L1

## What it does
Compares page snapshots for price, stock, or policy changes and emits concise diffs.

## When to use / not use
- **Use when:** Performing page change monitor tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `browser/page-change-monitor` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add browser/page-change-monitor
afe test browser/page-change-monitor
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/http, afe/browser

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test browser/page-change-monitor` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
