<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [👥 Teams](../../README.md#-ready-made-teams) › **SDR Prospecting Team**

# 👥 SDR Prospecting Team

![team: sdr-team](https://img.shields.io/badge/team-sdr--team-0f172a?style=flat-square) ![pattern: prompt-chaining](https://img.shields.io/badge/pattern-prompt--chaining-0d9488?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P1](https://img.shields.io/badge/priority-P1-8b5cf6?style=flat-square) ![safety: S3](https://img.shields.io/badge/safety-S3-ea580c?style=flat-square)

> Finds ICP leads, enriches and scores accounts, drafts tailored outreach, and stages CRM updates.

## 🔀 Workflow

```mermaid
flowchart LR
    lead_finder["Lead Finder"] --> lead_enricher["Lead Enricher"]
    lead_enricher["Lead Enricher"] --> lead_scorer["Lead Scorer"]
    lead_scorer["Lead Scorer"] --> account_researcher["Account Researcher"]
    account_researcher["Account Researcher"] --> outreach_personalizer["Outreach Personalizer"]
    outreach_personalizer["Outreach Personalizer"] --> crm_updater["CRM Updater"]
```

Starts at `sales/lead-finder`. Human approval at: `crm-updater`.

## 🧑‍🤝‍🧑 Members

| Agent | What it does | Safety |
|---|---|:---:|
| [`sales/lead-finder`](../../agents/business/sales/lead-finder/README.md) | Identifies target companies matching an ideal customer profile from public sources. | S1 |
| [`sales/lead-enricher`](../../agents/business/sales/lead-enricher/README.md) | Adds public firmographics, industry, and recent news to lead records. | S1 |
| [`sales/lead-scorer`](../../agents/business/sales/lead-scorer/README.md) | Scores leads transparently by ICP fit and intent signals with reasons. | S1 |
| [`sales/account-researcher`](../../agents/business/sales/account-researcher/README.md) | Builds pre-call briefs summarizing company priorities, leadership, and recent news. | S1 |
| [`sales/outreach-personalizer`](../../agents/business/sales/outreach-personalizer/README.md) | Drafts tailored outreach email sequences grounded in verified account research (draft only). | S2 |
| [`sales/crm-updater`](../../agents/business/sales/crm-updater/README.md) | Extracts call/meeting takeaways into structured CRM field updates gated by approval. | S3 |

## 🚀 Try it

```bash
afe graph sdr-team   # print the workflow and check that agent contracts fit
for a in sales/lead-finder sales/lead-enricher sales/lead-scorer sales/account-researcher sales/outreach-personalizer sales/crm-updater; do afe add $a; done   # copy every member
```

Files: [`team.yaml`](team.yaml) · [`schemas/`](schemas) · [`evals/`](evals)

<!-- afe:end-generated -->
