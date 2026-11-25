# Infrastructure-as-Code Writer `devops/iac-generator`

prototype · P1 · atomic · safety S2 · autonomy L2

## What it does
Generates Terraform, Pulumi, or Kubernetes manifests with least-privilege checks.

## When to use / not use
- **Use when:** Performing infrastructure-as-code writer tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `devops/iac-generator` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add devops/iac-generator
afe test devops/iac-generator
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/shell-sandbox

## Safety
- Safety tier: `S2`
- Side effects: ['devops-action']
- Approval gates: ['none']

## Evaluation
Run `afe test devops/iac-generator` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
