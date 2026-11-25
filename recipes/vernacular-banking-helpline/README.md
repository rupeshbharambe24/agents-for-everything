# Vernacular Banking Helpline (`recipes/vernacular-banking-helpline`)

Voice-first local-language customer helpline for banking queries, scam message checks, and complaint triage.

> **Regulated Safeguard:** Runs cleanly with local/on-prem open-weights models (`ollama`), discloses AI assistance, and gates S3/S4 grievance submission or banking actions behind explicit human approval.

## Run

```bash
PYTHONPATH=.:packages/core-python/src python3 recipes/vernacular-banking-helpline/app.py
PYTHONPATH=.:packages/core-python/src python3 -m unittest recipes/vernacular-banking-helpline/tests/test_recipe.py
```
