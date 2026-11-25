<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🍳 Recipes](../../README.md#-product-recipes) › **Farmer Voice & Photo Advisory**

# 🍳 Farmer Voice & Photo Advisory

![recipe: farmer-advisory](https://img.shields.io/badge/recipe-farmer--advisory-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P2](https://img.shields.io/badge/priority-P2-a78bfa?style=flat-square)

> Low-bandwidth photo and voice crop diagnostics, hyperlocal farm weather timing, and mandi price advisory in local languages.

| | |
|---|---|
| **Problem** | Smallholder farmers need timely crop pest identification, spray/harvest weather windows, and local market prices over low bandwidth and voice. |
| **Solution** | Composes crop-doctor, farm-weather-advisor, market-price-advisor, and text-to-speech. |

## 🧩 Built from

| Agent | What it does | Safety |
|---|---|:---:|
| [`agriculture/crop-doctor`](../../agents/industries/agriculture/crop-doctor/README.md) | Identifies likely pests and diseases from photos and gives advisory in the farmer's language. | S1 |
| [`agriculture/farm-weather-advisor`](../../agents/industries/agriculture/farm-weather-advisor/README.md) | Turns forecasts into farm actions (sow, spray, irrigate, harvest). | S1 |
| [`agriculture/market-price-advisor`](../../agents/industries/agriculture/market-price-advisor/README.md) | Local market and commodity prices and trends. | S1 |
| [`voice/text-to-speech`](../../agents/perception/voice/text-to-speech/README.md) | Natural speech synthesis from text with locale, speed, and tone control. | S0 |

**MCP servers:** [`afe/http`](../../mcp-servers/http/README.md), [`afe/tts`](../../mcp-servers/tts/README.md)

<!-- afe:end-generated -->

> Designed to run on the [`low-bandwidth-edge.yaml`](../../profiles/low-bandwidth-edge.yaml) open-weights local profile.

## Run

```bash
PYTHONPATH=.:packages/core-python/src python3 recipes/farmer-advisory/app.py
PYTHONPATH=.:packages/core-python/src python3 -m unittest recipes/farmer-advisory/tests/test_recipe.py
```
