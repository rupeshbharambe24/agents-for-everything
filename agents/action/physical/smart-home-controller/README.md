# Smart Home Controller `physical/smart-home-controller`

prototype · P1 · composite · safety S3 · autonomy L2

## What it does
Controls lights, climate, and locks via Home Assistant/Matter with confirmation on security devices.

## When to use / not use
- **Use when:** Performing smart home controller tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S3) and declared MCP server permissions.
3. Executes `physical/smart-home-controller` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add physical/smart-home-controller
afe test physical/smart-home-controller
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/home-automation

## Safety
- Safety tier: `S3`
- Side effects: ['physical-action']
- Approval gates: ['control_security_device']

## Evaluation
Run `afe test physical/smart-home-controller` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
