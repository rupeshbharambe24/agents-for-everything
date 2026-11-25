<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [👥 Teams](../../README.md#-ready-made-teams) › **KYC Onboarding Pipeline**

# 👥 KYC Onboarding Pipeline

![team: kyc-pipeline](https://img.shields.io/badge/team-kyc--pipeline-0f172a?style=flat-square) ![pattern: prompt-chaining](https://img.shields.io/badge/pattern-prompt--chaining-0d9488?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P1](https://img.shields.io/badge/priority-P1-8b5cf6?style=flat-square) ![safety: S4](https://img.shields.io/badge/safety-S4-dc2626?style=flat-square)

> Consented ID extraction, KYC checks, sanctions/PEP screening, officer approval, and audit logging.

## 🔀 Workflow

```mermaid
flowchart LR
    id_document_reader["ID Document Reader"] --> kyc_onboarding["KYC Onboarding Agent"]
    kyc_onboarding["KYC Onboarding Agent"] --> sanctions_screener["Sanctions & PEP Screener"]
    sanctions_screener["Sanctions & PEP Screener"] --> human_approval_gate{{"Human-in-the-Loop Gate"}}
    human_approval_gate{{"Human-in-the-Loop Gate"}} --> audit_logger["Audit Logger"]
```

Starts at `vision/id-document-reader`. Human approval at: `id-document-reader`, `kyc-onboarding`, `sanctions-screener`, `human-approval-gate`.

## 🧑‍🤝‍🧑 Members

| Agent | What it does | Safety |
|---|---|:---:|
| [`vision/id-document-reader`](../../agents/perception/vision/id-document-reader/README.md) | Extracts identity card fields for consented KYC workflows with quality checks. | S4 |
| [`banking/kyc-onboarding`](../../agents/industries/banking/kyc-onboarding/README.md) | Extracts and cross-checks KYC applicant records and flags mismatches for a human compliance officer. | S4 |
| [`banking/sanctions-screener`](../../agents/industries/banking/sanctions-screener/README.md) | Transliteration-aware fuzzy name screening against sanctions/PEP lists with explained matches for officer review. | S4 |
| [`orchestration/human-approval-gate`](../../agents/core/orchestration/human-approval-gate/README.md) | Pauses a workflow before risky steps, displays a clear summary/diff, and records approve/reject decisions. | S1 |
| [`guardrails/audit-logger`](../../agents/core/guardrails/audit-logger/README.md) | Records structured, PII-safe audit trail entries for agent actions and approvals. | S2 |

## 🚀 Try it

```bash
afe graph kyc-pipeline   # print the workflow and check that agent contracts fit
for a in vision/id-document-reader banking/kyc-onboarding banking/sanctions-screener orchestration/human-approval-gate guardrails/audit-logger; do afe add $a; done   # copy every member
```

Files: [`team.yaml`](team.yaml) · [`schemas/`](schemas) · [`evals/`](evals)

<!-- afe:end-generated -->
