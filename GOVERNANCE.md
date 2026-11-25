# Governance

`agents-for-everything` is maintained as an open, community-driven Apache-2.0 project.

## Roles

| Role | Responsibilities |
|---|---|
| **Core Maintainers** | Maintain `spec/`, `packages/core-*`, `cli/`, CI pipelines, release management, and overall repository architecture. |
| **Category Maintainers** | Listed in `CODEOWNERS` per category folder; review new agents, enforce atomicity, and maintain eval quality. |
| **Safety Reviewers** | Required sign-off on all `S3` and `S4` agents (finance, legal, healthcare, security, identity, destructive OS/web actions). |
| **Domain Reviewers** | Subject-matter experts reviewing specialized packs (banking, clinical workflows, law, agriculture). |
| **Contributors** | Propose agents, add implementations, expand multilingual eval datasets, and improve documentation. |

## Decision Process

- **New Agents & Bug Fixes:** Reviewed via Pull Request against `afe validate` and `afe test`.
- **New Categories or Spec Changes (`afe/v1`):** Proposed via an issue using `new-category-rfc` or an Architecture Decision Record (`docs/adr/`).
- **Maturity Promotions:** Governed strictly by `spec/SPEC.md` criteria (`spec` -> `prototype` -> `beta` -> `stable`).
