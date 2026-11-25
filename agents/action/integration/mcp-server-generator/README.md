# MCP Server Generator `integration/mcp-server-generator`

prototype · P1 · composite · safety S2 · autonomy L2

## What it does
Scaffolds a typed afe/v1 MCP server wrapper from an OpenAPI spec or CLI.

## When to use / not use
- **Use when:** Performing mcp server generator tasks cleanly within typed I/O contracts.
- **Do not use when:** Tasks requiring capabilities outside declared tools or unapproved autonomous high-stakes actions.

## How it works
1. Validates input payload against `schemas/input.schema.json`.
2. Enforces `SafetyPolicy` (S2) and declared MCP server permissions.
3. Executes `integration/mcp-server-generator` task logic (deterministic local processing or live model execution).
4. Validates output against `schemas/output.schema.json`.

## Input & Output
- Input schema: [`schemas/input.schema.json`](schemas/input.schema.json)
- Output schema: [`schemas/output.schema.json`](schemas/output.schema.json)

## Quick start
```bash
afe add integration/mcp-server-generator
afe test integration/mcp-server-generator
```

## Composes with
orchestration/router, orchestration/verifier

## Tools required
afe/python-sandbox

## Safety
- Safety tier: `S2`
- Side effects: ['integration-action']
- Approval gates: ['none']

## Evaluation
Run `afe test integration/mcp-server-generator` to verify all 10 cases in `evals/cases.jsonl`.

## Limitations
Offline mock mode uses deterministic domain heuristics; connect a live model provider for open-ended reasoning.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).
