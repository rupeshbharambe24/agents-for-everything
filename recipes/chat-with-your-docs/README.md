# Chat with Your Docs (`recipe/chat-with-your-docs`)

Private document Q&A pipeline combining `guardrails/pii-redactor` -> `memory/knowledge-ingestor` -> `search/rag-qa` -> `guardrails/hallucination-checker`.

```bash
PYTHONPATH=.:packages/core-python/src:cli/src python3 recipes/chat-with-your-docs/app.py
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m unittest recipes/chat-with-your-docs/tests/test_recipe.py
```
