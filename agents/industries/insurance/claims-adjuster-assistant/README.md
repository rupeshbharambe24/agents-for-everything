# Claims Adjuster Assistant `insurance/claims-adjuster-assistant`

prototype · P2 · composite · safety S4 · autonomy L2

## What it does
Damage assessment, coverage check against the policy and fraud indicators for the adjuster.

> **Important Safety Notice:** Insurance workflow assistant; claims, coverage, and underwriting outputs require licensed adjuster/underwriter verification.

## When to use / not use
- **Use when:** You need single-purpose claims adjuster assistant (claim + policy → assessment).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S4`) and declared MCP permissions.
3. Runs `insurance/claims-adjuster-assistant` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add insurance/claims-adjuster-assistant
afe test insurance/claims-adjuster-assistant
```

## Composes with
documents/document-parser, vision/ocr

## Tools required
afe/documents

## Safety
- Safety tier: `S4`
- Side effects: `['high-stakes-action-requires-human-signoff']`
- Approval gates: `['human_officer_signoff']`
- Handles PII: `True`

## Evaluation
Run `afe test insurance/claims-adjuster-assistant` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
