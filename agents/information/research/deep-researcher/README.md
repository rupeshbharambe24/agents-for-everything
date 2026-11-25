# Deep Researcher `research/deep-researcher`

beta · P0 · composite · safety S1 · autonomy L2

## What it does
End-to-end composite research orchestrator combining search, reading, fact-checking, and report writing.

## When to use / not use
- **Use when:** Thorough multi-source investigation producing cited reports.
- **Do not use when:** Simple single-fact lookups.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `research/deep-researcher` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add research/deep-researcher
afe test research/deep-researcher
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/web-search, afe/http, afe/documents

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test research/deep-researcher` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
