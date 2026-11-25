# Digital Declutterer `personal/digital-declutterer`

prototype · P2 · composite · safety S2 · autonomy L2

## What it does
Cleans up photos, files and inbox with a reviewable plan.

## When to use / not use
- **Use when:** You need single-purpose digital declutterer (accounts → cleanup plan).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `personal/digital-declutterer` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add personal/digital-declutterer
afe test personal/digital-declutterer
```

## Composes with
text/structured-extractor, search/web-search

## Tools required
afe/filesystem, afe/email

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `True`

## Evaluation
Run `afe test personal/digital-declutterer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
