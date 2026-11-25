<!-- afe:begin-generated (scripts/build_readmes.py) — edit the manifest, not this block -->

[🏠 Agents for Everything](../../README.md) › [🍳 Recipes](../../README.md#-product-recipes) › **Content Engine**

# 🍳 Content Engine

![recipe: content-engine](https://img.shields.io/badge/recipe-content--engine-0f172a?style=flat-square) ![maturity: prototype](https://img.shields.io/badge/maturity-prototype-f59e0b?style=flat-square) ![priority: P1](https://img.shields.io/badge/priority-P1-8b5cf6?style=flat-square)

> Turns one raw recording into a podcast package, edited blog post, social posts, and short clip suggestions.

| | |
|---|---|
| **Problem** | Creators spend hours manually repurposing one long recording across formats and channels. |
| **Solution** | Composes podcast-producer, blog-writer, editor, social-post-writer, and clip-generator. |

## 🚀 Run it

```bash
PYTHONPATH=.:packages/core-python/src:cli/src python3 recipes/content-engine/app.py
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m unittest recipes/content-engine/tests/test_recipe.py
```

## 🧩 Built from

| Agent | What it does | Safety |
|---|---|:---:|
| [`audio/podcast-producer`](../../agents/perception/audio/podcast-producer/README.md) | Produces transcripts, chapters, silence cuts, and show notes from raw podcast audio. | S1 |
| [`content/blog-writer`](../../agents/business/content/blog-writer/README.md) | Researches, outlines, and drafts source-backed articles tuned for readability. | S1 |
| [`content/editor`](../../agents/business/content/editor/README.md) | Performs structural and clarity editing with tracked suggestions and rationale. | S0 |
| [`content/social-post-writer`](../../agents/business/content/social-post-writer/README.md) | Adapts topics or articles into platform-ready posts and threads. | S0 |
| [`video/clip-generator`](../../agents/perception/video/clip-generator/README.md) | Selects high-engagement highlight segments and timestamps for short-form clips. | S1 |

**Teams:** [`content-studio`](../../teams/content-studio/README.md)

**MCP servers:** [`afe/stt`](../../mcp-servers/stt/README.md), [`afe/media`](../../mcp-servers/media/README.md)

<!-- afe:end-generated -->
