# {{name}} (`{{category}}/{{slug}}`)

spec · P1 · atomic · safety S0 · autonomy L1

## What it does
{{summary}}

## When to use / not use
- Use when you need focused `{{category}}/{{slug}}` execution with typed I/O.
- Do not use for tasks requiring side effects outside declared `tools.yaml`.

## Quick start
```bash
afe add {{category}}/{{slug}}
afe test {{category}}/{{slug}}
```

## Safety
Safety level `S0` (pure computation, no external side effects).

## Limitations
Requires schema-conforming input matching `schemas/input.schema.json`.
