# Web Scraper `browser/web-scraper`

prototype · P0 · atomic · safety S1 · autonomy L1

## What it does
Turns HTML tables or lists into validated JSON arrays cleanly.

## When to use / not use
- **Use when:** Extracting public product tables, docs, or structured listings.
- **Do not use when:** Bypassing logins, paywalls, or CAPTCHAs.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `browser/web-scraper` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add browser/web-scraper
afe test browser/web-scraper
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/browser, afe/http

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test browser/web-scraper` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
