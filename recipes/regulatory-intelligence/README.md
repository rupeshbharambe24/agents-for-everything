# Regulatory Intelligence (`recipes/regulatory-intelligence`)

Monitors regulatory circulars and statutory bulletins, maps affected internal controls, and produces source-cited impact briefings.

## Run

```bash
PYTHONPATH=.:packages/core-python/src python3 recipes/regulatory-intelligence/app.py
PYTHONPATH=.:packages/core-python/src python3 -m unittest recipes/regulatory-intelligence/tests/test_recipe.py
```
