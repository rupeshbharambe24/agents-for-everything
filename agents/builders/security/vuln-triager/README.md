# Vulnerability Triager `security/vuln-triager`

prototype · P1 · atomic · safety S1 · autonomy L1

## What it does
Prioritizes scanner CVEs by reachability, exploitability, and asset exposure.

## When to use / not use
- **Use when:** Performing vulnerability triager tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S1) and declared MCP server permissions.
3. Executes `security/vuln-triager` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add security/vuln-triager
afe test security/vuln-triager
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/threat-intel, afe/filesystem

## Safety
- Safety tier: `S1`
- Side effects: ['none']
- Approval gates: ['none']

## Evaluation
Run `afe test security/vuln-triager` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
