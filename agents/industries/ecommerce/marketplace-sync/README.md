# Marketplace Sync `ecommerce/marketplace-sync`

prototype · P2 · composite · safety S3 · autonomy L2

## What it does
Keeps listings, stock and prices in sync across marketplaces and the web store.

## When to use / not use
- **Use when:** You need single-purpose marketplace sync (catalog → sync report).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S3`) and declared MCP permissions.
3. Runs `ecommerce/marketplace-sync` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add ecommerce/marketplace-sync
afe test ecommerce/marketplace-sync
```

## Composes with
search/semantic-search, text/sentiment-analyzer

## Tools required
afe/http

## Safety
- Safety tier: `S3`
- Side effects: `['external-action-requires-approval']`
- Approval gates: `['approve_external_action']`
- Handles PII: `True`

## Evaluation
Run `afe test ecommerce/marketplace-sync` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
