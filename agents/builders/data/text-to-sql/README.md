# Text-to-SQL `data/text-to-sql`

beta · P0 · atomic · safety S1 · autonomy L1

## What it does
Generates schema-verified read-only SQL queries and refuses destructive DDL/DML.

## When to use / not use
- **Use when:** Querying analytics tables safely using natural language.
- **Do not use when:** Schema migrations or write queries.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `data/text-to-sql` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add data/text-to-sql
afe test data/text-to-sql
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/sql

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test data/text-to-sql` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
