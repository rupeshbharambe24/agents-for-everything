# ADR 0001: Atomic Composable Contracts (`afe/v1`)

## Status
Accepted

## Context
Monolithic prompts bundle too many tools and responsibilities, making agents brittle and non-reusable.

## Decision
Every agent in `agents-for-everything` defines a framework-neutral `agent.yaml` manifest plus JSON Schema 2020-12 input/output contracts referencing shared types in `spec/types/`. Composite agents and teams chain atomic agents strictly through typed schemas.

## Consequences
Any two agents with compatible schemas can compose automatically and be verified statically during `afe validate` and `scripts/build_catalog.py`.
