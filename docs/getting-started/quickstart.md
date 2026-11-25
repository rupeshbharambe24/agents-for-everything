# Quick Start

## 1. Validate & Browse the Catalog

```bash
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m afe_cli validate
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m afe_cli search "voice"
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m afe_cli info voice/voice-form-filler
```

## 2. Run Any Agent Offline or with Live Models

```bash
# Offline deterministic mode (default when no API key is set)
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m afe_cli run text/summarizer \
  --input '{"text":"Agents for Everything provides composable single-purpose AI agents."}'

# Live OpenAI / Anthropic / Gemini / Ollama
export AFE_PROVIDER=ollama   # or openai, anthropic, gemini
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m afe_cli run text/summarizer --input '{"text":"..."}'
```

## 3. Copy an Agent into Your Project (`shadcn/ui`-style)

```bash
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m afe_cli add voice/voice-form-filler --dest ./my-app/agents
```

## 4. Run Eval Suites

```bash
PYTHONPATH=.:packages/core-python/src:cli/src python3 -m afe_cli test voice/voice-form-filler
```
