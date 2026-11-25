# Meeting Prep Brief `meetings/meeting-prep`

prototype · P1 · composite · safety S1 · autonomy L1

## What it does
Compiles pre-meeting briefs on attendees, prior threads, open items, and suggested agenda.

## When to use / not use
- **Use when:** Performing meeting prep brief tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `meetings/meeting-prep` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add meetings/meeting-prep
afe test meetings/meeting-prep
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/calendar, afe/email

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test meetings/meeting-prep` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
