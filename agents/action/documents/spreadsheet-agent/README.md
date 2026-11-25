# Spreadsheet Agent `documents/spreadsheet-agent`

prototype · P0 · atomic · safety S2 · autonomy L1

## What it does
Executes safe deterministic aggregations and formula checks on tabular rows.

## When to use / not use
- **Use when:** Summarizing or transforming CSV/XLSX table rows.
- **Do not use when:** Arbitrary database joins (use data/text-to-sql).

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `documents/spreadsheet-agent` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add documents/spreadsheet-agent
afe test documents/spreadsheet-agent
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/documents

## Safety
- Safety tier: `S2`
- Side effects: ['updates-sheet-copy']
- Approval gates: ['none']

## Evaluation
Run `afe test documents/spreadsheet-agent` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
