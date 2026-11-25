# Health Record Organizer `wellness/health-record-organizer`

prototype · P2 · composite · safety S2 · autonomy L2

## What it does
Collects reports into a timeline and summary to share with doctors.

> **Important Safety Notice:** Informational wellbeing/self-care support only; not medical diagnosis or therapy. Always route acute crises to emergency services or verified helplines.

## When to use / not use
- **Use when:** You need single-purpose health record organizer (documents → timeline).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S2`) and declared MCP permissions.
3. Runs `wellness/health-record-organizer` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add wellness/health-record-organizer
afe test wellness/health-record-organizer
```

## Composes with
documents/document-parser, text/summarizer

## Tools required
afe/documents

## Safety
- Safety tier: `S2`
- Side effects: `['draft-or-local-write']`
- Approval gates: `['confirm_write']`
- Handles PII: `True`

## Evaluation
Run `afe test wellness/health-record-organizer` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
