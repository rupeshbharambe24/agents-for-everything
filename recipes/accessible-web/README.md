<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🍳 Recipes](../../README.md#-product-recipes) › **Accessible Voice Web Companion**

# 🍳 Accessible Voice Web Companion

![recipe: accessible-web](https://img.shields.io/badge/recipe-accessible--web-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P2](https://img.shields.io/badge/priority-P2-a78bfa?style=flat-square)

> Browser companion that narrates page state aloud, audits WCAG gaps, and fills web forms hands-free by voice before human submit.

| | |
|---|---|
| **Problem** | Complex web portals and unlabelled forms lock out visually impaired or motor-restricted users. |
| **Solution** | Composes screen-narrator, accessibility-auditor, and voice-form-filler with a strict human confirmation step before submission. |

## 🧩 Built from

| Agent | What it does | Safety |
|---|---|:---:|
| [`accessibility/screen-narrator`](../../agents/perception/accessibility/screen-narrator/README.md) | Describes active UI screens aloud for blind and low-vision navigation. | S2 |
| [`accessibility/accessibility-auditor`](../../agents/perception/accessibility/accessibility-auditor/README.md) | Checks HTML/UI attributes against WCAG contrast, alt-text, and landmark rules. | S1 |
| [`voice/voice-form-filler`](../../agents/perception/voice/voice-form-filler/README.md) | Listens to natural speech, maps answers to typed form fields, checks gaps, and confirms before submit. | S2 |

**MCP servers:** [`afe/browser`](../../mcp-servers/browser/README.md), [`afe/stt`](../../mcp-servers/stt/README.md), [`afe/tts`](../../mcp-servers/tts/README.md)

<!-- afe:end-generated -->

## Run

```bash
PYTHONPATH=.:packages/core-python/src python3 recipes/accessible-web/app.py
PYTHONPATH=.:packages/core-python/src python3 -m unittest recipes/accessible-web/tests/test_recipe.py
```
