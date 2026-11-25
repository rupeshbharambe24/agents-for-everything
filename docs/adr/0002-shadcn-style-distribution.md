# ADR 0002: Copy-In Distribution (`afe add`) Over 500 Micro-Packages

## Status
Accepted

## Context
Publishing 500+ individual PyPI/npm packages creates prohibitive dependency version conflicts and release overhead.

## Decision
Publish core runtimes (`agents-for-everything` on PyPI, `@agents-for-everything/core` on npm) and copy individual agents plus their recursive dependencies into user repositories via `afe add <agent-id>` (inspired by `shadcn/ui`).

## Consequences
Users keep full ownership and inspectability of copied prompts, schemas, and implementations with zero package bloat.
