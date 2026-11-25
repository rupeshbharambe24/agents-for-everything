# ADR 0004: Open A2A Discovery Registry and Verified Badges

## Status
Accepted

## Context
As third-party contributors and organizations adopt `agents-for-everything`, teams need a standardized machine-readable way to discover compatible agents via the Agent2Agent (`A2A`) protocol and verify whether an agent meets safety, schema, and evaluation standards before use.

## Decision
1. Publish static open A2A discovery artifacts in `registry/`:
   - `registry/a2a-index.json`: full A2A Agent Card directory for all cataloged agents, including skills, schemas, safety tiers, and verification badges.
   - `registry/.well-known/agent.json`: top-level A2A Registry Agent Card for automated discovery on GitHub Pages or static mirrors.
   - `registry/verified-index.json`: deterministic verification records (`sha256` contract digest + verification criteria).
2. Grant an agent a `verified` badge via `afe verify` only when it passes:
   - Schema & structural validation (`validate_agent_dir`),
   - Passing evaluation suite thresholds (`>= 10` cases for `prototype`, `>= 50` cases for `beta`/`stable`),
   - Safety compliance (`S0` declares zero tools; `S3`/`S4` declare `approval_required_for` and `SAFETY_REVIEW.md`),
   - Secret scan hygiene (no embedded API tokens or credentials in prompts/code).

## Consequences
Every hosted or mirrored copy of this repository exposes zero-backend A2A discovery and reproducible verification without centralized lock-in.
