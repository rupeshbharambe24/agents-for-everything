# Landing Page Builder `marketing/landing-page-builder`

prototype · P2 · composite · safety S2 · autonomy L2

## What it does
Builds landing pages with copy, layout and analytics.

## When to use / not use
- **Use when:** You need single-purpose landing page builder (brief → page).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `marketing/landing-page-builder` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add marketing/landing-page-builder
afe test marketing/landing-page-builder
```

## Composes with
research/market-researcher, content/copywriter

## Tools required
afe/web-search

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `True`

## Evaluation
Run `afe test marketing/landing-page-builder` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
