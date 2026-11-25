# Underwriting Assistant `insurance/underwriting-assistant`

prototype · P2 · composite · safety S4 · autonomy L2

## What it does
Summarizes submissions and risk factors for underwriters.

> **Important Safety Notice:** Insurance workflow assistant; claims, coverage, and underwriting outputs require licensed adjuster/underwriter verification.

## When to use / not use
- **Use when:** You need single-purpose underwriting assistant (submission → risk summary).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S4`) and declared MCP permissions.
3. Runs `insurance/underwriting-assistant` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add insurance/underwriting-assistant
afe test insurance/underwriting-assistant
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
Run `afe test insurance/underwriting-assistant` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
