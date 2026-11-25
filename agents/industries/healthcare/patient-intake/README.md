# Patient Intake Agent `healthcare/patient-intake`

prototype · P2 · composite · safety S4 · autonomy L2

## What it does
Pre-visit questionnaires by voice or chat in the patient's language.

> **Important Safety Notice:** Clinical workflow aid for licensed professionals only; outputs are unapproved drafts requiring clinician review and never replace medical judgement.

## When to use / not use
- **Use when:** You need single-purpose patient intake agent (patient ↔ intake record).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S4`) and declared MCP permissions.
3. Runs `healthcare/patient-intake` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add healthcare/patient-intake
afe test healthcare/patient-intake
```

## Composes with
voice/voice-form-filler, voice/speech-to-text

## Tools required
afe/medical-kb

## Safety
- Safety tier: `S4`
- Side effects: `['high-stakes-action-requires-human-signoff']`
- Approval gates: `['human_officer_signoff']`
- Handles PII: `True`

## Evaluation
Run `afe test healthcare/patient-intake` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
