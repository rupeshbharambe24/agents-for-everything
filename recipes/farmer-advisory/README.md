# Farmer Advisory (`recipes/farmer-advisory`)

Low-bandwidth crop advisory pipeline turning leaf symptoms/photos, local weather conditions, and mandi queries into spoken advice in regional Indic languages.

> Designed to run on the [`low-bandwidth-edge.yaml`](../../profiles/low-bandwidth-edge.yaml) open-weights local profile.

## Run

```bash
PYTHONPATH=.:packages/core-python/src python3 recipes/farmer-advisory/app.py
PYTHONPATH=.:packages/core-python/src python3 -m unittest recipes/farmer-advisory/tests/test_recipe.py
```
