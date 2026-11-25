# ADR 0005: `afe/v2` Specification Evolution & Automated Migration

## Status
Accepted

## Context
Experience building 571 agents across 54 categories, 22 teams, 12 recipes, and local/on-prem industry packs surfaced first-class metadata needs that were previously inferred at export or build time: A2A transport capabilities, verification provenance badges, deployment profile bindings (`profiles/*.yaml`), and explicit deprecation links.

## Decision
1. Introduce `spec/v2/SPEC.md` and `spec/v2/agent.schema.json` with `apiVersion: afe/v2` adding optional structured sections:
   - `spec.a2a`: streaming, state transition history, and supported transports (`http+json`, `stdio`, `in-process`).
   - `spec.verification`: badge status, target eval pass rate, safety review reference, and on-prem readiness.
   - `spec.deployments`: referenced runtime profile files (e.g. `profiles/regulated-airgapped.yaml`).
   - `spec.deprecation`: explicit `deprecated`, `since`, and `replaced_by` pointer matching `registry/aliases.yaml`.
2. Keep `afe/v1` fully supported; `validate_agent_dir` validates both `afe/v1` and `afe/v2` manifests according to `apiVersion`.
3. Provide an automated, lossless migration command (`afe migrate`) to upgrade any `afe/v1` agent manifest to `afe/v2` and validate the output immediately.

## Consequences
Existing `afe/v1` agents continue working with zero breakage while new and promoted agents can adopt `afe/v2` incrementally using `afe migrate`.
