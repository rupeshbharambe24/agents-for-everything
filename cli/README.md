# `agents-for-everything-cli`

The `afe` command-line tool for [Agents for Everything](https://github.com/rupeshbharambe24/agents-for-everything): search the catalog of 571 typed AI agents, copy agents into your project, run them, test them and export them (Agent Skills, A2A cards, MCP servers, LangGraph, subagents).

The CLI works on a clone of the repository, which holds the agents:

```bash
git clone https://github.com/rupeshbharambe24/agents-for-everything.git
cd agents-for-everything
uv sync --all-packages
uv run afe search "fill a form by voice"
uv run afe add voice/voice-form-filler --dest ../my-app/agents
```

Commands: `search`, `info`, `add`, `run`, `test`, `new`, `export`, `validate`, `verify`, `migrate`, `graph`. Run `afe <command> --help` for details.

License: Apache-2.0.
