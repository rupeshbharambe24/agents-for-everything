# Symptom Navigator `wellness/symptom-navigator`

prototype · P2 · composite · safety S4 · autonomy L2

## What it does
Asks structured questions and suggests the right level of care (self-care, doctor, emergency).

> **Important Safety Notice:** Informational wellbeing/self-care support only; not medical diagnosis or therapy. Always route acute crises to emergency services or verified helplines.

## When to use / not use
- **Use when:** You need single-purpose symptom navigator (symptoms → care-level guidance).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S4`) and declared MCP permissions.
3. Runs `wellness/symptom-navigator` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add wellness/symptom-navigator
afe test wellness/symptom-navigator
```

## Composes with
documents/document-parser, text/summarizer

## Tools required
afe/medical-kb

## Safety
- Safety tier: `S4`
- Side effects: `['high-stakes-action-requires-human-signoff']`
- Approval gates: `['human_officer_signoff']`
- Handles PII: `True`

## Evaluation
Run `afe test wellness/symptom-navigator` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
