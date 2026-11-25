# Wardrobe Stylist `creative/wardrobe-stylist`

prototype · P2 · atomic · safety S1 · autonomy L1

## What it does
Outfit suggestions from photos of your own wardrobe.

## When to use / not use
- **Use when:** You need single-purpose wardrobe stylist (wardrobe + occasion → outfits).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S1`) and declared MCP permissions.
3. Runs `creative/wardrobe-stylist` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add creative/wardrobe-stylist
afe test creative/wardrobe-stylist
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/media

## Safety
- Safety tier: `S1`
- Side effects: `['read-only-external-query']`
- Approval gates: `[]`
- Handles PII: `False`

## Evaluation
Run `afe test creative/wardrobe-stylist` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
