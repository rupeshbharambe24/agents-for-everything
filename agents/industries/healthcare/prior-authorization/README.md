# Prior Authorization Agent `healthcare/prior-authorization`

prototype · P2 · composite · safety S4 · autonomy L2

## What it does
Assembles clinical evidence and fills payer forms for review.

> **Important Safety Notice:** Clinical workflow aid for licensed professionals only; outputs are unapproved drafts requiring clinician review and never replace medical judgement.

## When to use / not use
- **Use when:** You need single-purpose prior authorization agent (case → auth packet).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S4`) and declared MCP permissions.
3. Runs `healthcare/prior-authorization` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add healthcare/prior-authorization
afe test healthcare/prior-authorization
```

## Composes with
voice/speech-to-text, text/translator

## Tools required
afe/documents

## Safety
- Safety tier: `S4`
- Side effects: `['high-stakes-action-requires-human-signoff']`
- Approval gates: `['human_officer_signoff']`
- Handles PII: `True`

## Evaluation
Run `afe test healthcare/prior-authorization` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
