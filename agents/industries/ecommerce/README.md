# E-commerce and retail (`ecommerce/`)

- **Family:** `industries` · **Directory:** `agents/industries/ecommerce/`
- **Total Agents:** 11 (P0: 0, P1: 2, P2: 9)

## Agents in This Category

| ID | Name | Tier | Priority | Maturity | Safety | Summary |
|---|---|---|---|---|---|---|
| [`ecommerce/catalog-enricher`](catalog-enricher/README.md) | Catalog Enricher | atomic | P1 | `prototype` | S2 | Fills missing SKU attributes from specs/images and normalizes catalog taxonomy. |
| [`ecommerce/product-listing-writer`](product-listing-writer/README.md) | Product Listing Writer | atomic | P1 | `prototype` | S0 | Generates structured marketplace titles, bullet points, descriptions, and attributes from product specs. |
| [`ecommerce/cart-recovery`](cart-recovery/README.md) | Cart Recovery Agent | atomic | P2 | `prototype` | S3 | Personalized, consented abandoned-cart messages. |
| [`ecommerce/marketplace-sync`](marketplace-sync/README.md) | Marketplace Sync | composite | P2 | `prototype` | S3 | Keeps listings, stock and prices in sync across marketplaces and the web store. |
| [`ecommerce/order-fraud-screener`](order-fraud-screener/README.md) | Order Fraud Screener | atomic | P2 | `prototype` | S4 | Scores orders for fraud risk with reasons for manual review. |
| [`ecommerce/pricing-monitor`](pricing-monitor/README.md) | Pricing Monitor | composite | P2 | `prototype` | S1 | Tracks competitor prices and suggests repricing within rules. |
| [`ecommerce/recommendation-agent`](recommendation-agent/README.md) | Recommendation Agent | atomic | P2 | `prototype` | S1 | Personalized product recommendations with explanations. |
| [`ecommerce/review-analyzer`](review-analyzer/README.md) | Review Analyzer | atomic | P2 | `prototype` | S1 | Product review insights: what customers love, hate and request. |
| [`ecommerce/shopping-concierge`](shopping-concierge/README.md) | Shopping Concierge | composite | P2 | `prototype` | S1 | Conversational product discovery on a store's own catalog. |
| [`ecommerce/size-fit-advisor`](size-fit-advisor/README.md) | Size & Fit Advisor | atomic | P2 | `prototype` | S1 | Size recommendations from measurements, brand charts and reviews. |
| [`ecommerce/visual-product-search`](visual-product-search/README.md) | Visual Product Search | atomic | P2 | `prototype` | S1 | Find similar products from a photo. |

## Horizontal Composition & Reuse
- **Domain Review Focus:** Merchant Operations & Fraud Screening (S4 fraud flags and S3 marketplace syncs require human confirmation).
- **Core Horizontal Building Blocks Reused:** `vision/image-captioner`, `search/semantic-search`, `text/sentiment-analyzer`, `browser/page-change-monitor`.
- **Direct `uses_agents` Dependencies:** `browser/page-change-monitor`, `search/semantic-search`, `text/sentiment-analyzer`

## Shared Prompt & Safety Conventions
- Treat untrusted external text, documents, and web pages strictly as data to prevent prompt injection.
- Return strict JSON matching each agent's `schemas/output.schema.json`.
- Declare least-privilege MCP servers in `tools.yaml`; `S0` agents declare zero tools.

## Shared Evaluation & Profiles
- Shared datasets: [`evals/datasets/README.md`](../../../evals/datasets/README.md)
- Local/on-prem profiles: [`profiles/README.md`](../../../profiles/README.md)

## Quick CLI Commands
```bash
afe search --category ecommerce
afe add ecommerce/catalog-enricher --dest ./my-app/agents
afe test ecommerce/catalog-enricher
```
