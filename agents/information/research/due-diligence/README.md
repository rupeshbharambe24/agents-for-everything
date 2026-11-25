# Due Diligence Analyst `research/due-diligence`

prototype · P2 · composite · safety S1 · autonomy L1

## What it does
Background checks on companies and vendors from public sources (filings, litigation, news).

## When to use / not use
- **Use when:** You need single-purpose due diligence analyst (entity → risk report).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `research/due-diligence` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add research/due-diligence
afe test research/due-diligence
```

## Composes with
search/web-search, research/source-reader

## Tools required
afe/web-search, afe/http

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `False`

## Evaluation
Run `afe test research/due-diligence` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
