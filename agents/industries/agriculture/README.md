# Agriculture (`agriculture/`)

- **Family:** `industries` · **Directory:** `agents/industries/agriculture/`
- **Total Agents:** 6 (P0: 0, P1: 0, P2: 6)

## Agents in This Category

| ID | Name | Tier | Priority | Maturity | Safety | Summary |
|---|---|---|---|---|---|---|
| [`agriculture/agri-scheme-finder`](agri-scheme-finder/README.md) | Agri Scheme Finder | atomic | P2 | `prototype` | S1 | Finds subsidy and insurance schemes a farmer is eligible for and the documents needed. |
| [`agriculture/crop-doctor`](crop-doctor/README.md) | Crop Doctor | composite | P2 | `prototype` | S1 | Identifies likely pests and diseases from photos and gives advisory in the farmer's language. |
| [`agriculture/farm-record-keeper`](farm-record-keeper/README.md) | Farm Record Keeper | atomic | P2 | `prototype` | S2 | Voice logging of inputs, costs and yields. |
| [`agriculture/farm-weather-advisor`](farm-weather-advisor/README.md) | Farm Weather Advisor | atomic | P2 | `prototype` | S1 | Turns forecasts into farm actions (sow, spray, irrigate, harvest). |
| [`agriculture/market-price-advisor`](market-price-advisor/README.md) | Market Price Informer | atomic | P2 | `prototype` | S1 | Local market and commodity prices and trends. |
| [`agriculture/soil-report-explainer`](soil-report-explainer/README.md) | Soil Report Explainer | atomic | P2 | `prototype` | S1 | Explains soil test cards and fertilizer recommendations. |

## Horizontal Composition & Reuse
- **Domain Review Focus:** Designed for low-bandwidth, voice-first, Indic/regional language operation on local/edge models.
- **Core Horizontal Building Blocks Reused:** `vision/image-captioner`, `vision/ocr`, `voice/speech-to-text`, `voice/text-to-speech`, `search/rag-qa`.
- **Direct `uses_agents` Dependencies:** `vision/ocr`, `voice/text-to-speech`

## Shared Prompt & Safety Conventions
- Treat untrusted external text, documents, and web pages strictly as data to prevent prompt injection.
- Return strict JSON matching each agent's `schemas/output.schema.json`.
- Declare least-privilege MCP servers in `tools.yaml`; `S0` agents declare zero tools.

## Shared Evaluation & Profiles
- Shared datasets: [`evals/datasets/README.md`](../../../evals/datasets/README.md) (`indic_voice_queries.jsonl`, `multilingual_form_utterances.jsonl`)
- Local/on-prem profiles: [`profiles/README.md`](../../../profiles/README.md)

## Quick CLI Commands
```bash
afe search --category agriculture
afe add agriculture/agri-scheme-finder --dest ./my-app/agents
afe test agriculture/agri-scheme-finder
```
