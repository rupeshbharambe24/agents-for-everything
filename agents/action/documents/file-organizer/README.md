# File Organizer `documents/file-organizer`

beta · P0 · atomic · safety S2 · autonomy L2

## What it does
Turns messy directories into clean category folders with explicit preview/approval before moving.

## When to use / not use
- **Use when:** Tidying Downloads, project assets, or scanned document folders.
- **Do not use when:** Deleting files permanently.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `documents/file-organizer` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add documents/file-organizer
afe test documents/file-organizer
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/filesystem

## Safety
- Safety tier: `S2`
- Side effects: ['plans-file-moves']
- Approval gates: ['apply_moves']

## Evaluation
Run `afe test documents/file-organizer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
