# Incident Responder `devops/incident-responder`

prototype · P1 · composite · safety S3 · autonomy L2

## What it does
Correlates alerts, metrics, and recent deploys; suggests mitigations and runs approved runbooks.

## When to use / not use
- **Use when:** Performing incident responder tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S3) and declared MCP server permissions.
3. Executes `devops/incident-responder` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add devops/incident-responder
afe test devops/incident-responder
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/observability, afe/documents

## Safety
- Safety tier: `S3`
- Side effects: ['devops-action']
- Approval gates: ['execute_runbook']

## Evaluation
Run `afe test devops/incident-responder` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
