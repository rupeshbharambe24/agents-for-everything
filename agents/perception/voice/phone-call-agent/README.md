# Phone Call Agent `voice/phone-call-agent`

prototype · P1 · composite · safety S3 · autonomy L2

## What it does
Inbound/outbound telephony assistant for bookings and reminders with mandatory AI disclosure.

## When to use / not use
- **Use when:** Performing phone call agent tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S3) and declared MCP server permissions.
3. Executes `voice/phone-call-agent` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add voice/phone-call-agent
afe test voice/phone-call-agent
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/telephony, afe/stt, afe/tts

## Safety
- Safety tier: `S3`
- Side effects: ['voice-action']
- Approval gates: ['place_or_answer_call']

## Evaluation
Run `afe test voice/phone-call-agent` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
