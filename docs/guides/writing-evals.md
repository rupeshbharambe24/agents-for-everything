# Writing Evaluations

Every `prototype` agent requires **at least 10 eval cases** in `evals/cases.jsonl`.

## Required Coverage

- **Normal cases:** Standard representative inputs matching the core use case.
- **Boundary / edge cases:** Empty/short input, missing optional fields, conflicting units or dates.
- **Adversarial / safety cases:** Prompt injections embedded inside documents, emails, or transcripts; unauthorized actions gated by `S3`/`S4`.
- **Multilingual cases:** Especially for voice, text, and consumer-facing agents (including Indic languages & code-switching).

Run tests offline with deterministic mock mode (`afe test <id>`) or live against any provider (`afe test <id> --live --provider openai`).
