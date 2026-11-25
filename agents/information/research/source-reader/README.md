# Source Reader `research/source-reader`

beta · P0 · atomic · safety S1 · autonomy L1

## What it does
Produces structured research notes with exact quotes from a single source.

## When to use / not use
- **Use when:** Extracting structured notes from an article, paper, or page.
- **Do not use when:** Multi-source synthesis.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `research/source-reader` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add research/source-reader
afe test research/source-reader
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/http, afe/documents

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test research/source-reader` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
