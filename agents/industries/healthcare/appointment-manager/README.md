# Appointment Manager `healthcare/appointment-manager`

prototype · P2 · composite · safety S3 · autonomy L2

## What it does
Scheduling, reminders and waitlist backfill to reduce no-shows.

> **Important Safety Notice:** Clinical workflow aid for licensed professionals only; outputs are unapproved drafts requiring clinician review and never replace medical judgement.

## When to use / not use
- **Use when:** You need single-purpose appointment manager (schedule + patients → bookings).
- **Do not use when:** Actions exceed declared MCP tools or bypass required human sign-off.

## How it works
1. Validates input against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (`S3`) and declared MCP permissions.
3. Runs `healthcare/appointment-manager` logic locally (`mock` or `ollama`) or via any configured model provider.
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add healthcare/appointment-manager
afe test healthcare/appointment-manager
```

## Composes with
voice/speech-to-text, text/translator

## Tools required
afe/calendar, afe/chat

## Safety
- Safety tier: `S3`
- Side effects: `['external-action-requires-approval']`
- Approval gates: `['approve_external_action']`
- Handles PII: `True`

## Evaluation
Run `afe test healthcare/appointment-manager` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic structured heuristics; connect Ollama or a frontier model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
