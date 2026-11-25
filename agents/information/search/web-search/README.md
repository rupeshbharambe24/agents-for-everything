# Web Searcher `search/web-search`

beta · P0 · atomic · safety S1 · autonomy L1

## What it does
Provides clean deduplicated SearchResult items for answer engines and researchers.

## When to use / not use
- **Use when:** Retrieving live external web references.
- **Do not use when:** Searching private local files or vector stores.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `search/web-search` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add search/web-search
afe test search/web-search
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/web-search

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test search/web-search` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
