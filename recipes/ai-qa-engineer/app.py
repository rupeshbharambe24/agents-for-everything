"""End-to-end AI QA Engineer recipe."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

RECIPE_DIR = Path(__file__).resolve().parent
REPO_ROOT = RECIPE_DIR.parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "packages" / "core-python" / "src"))

from agents_for_everything import AgentRunner, RunContext  # noqa: E402


def inspect_staging_app(url: str, page_text: str, provider_name: str = "auto") -> dict[str, Any]:
    runner = AgentRunner(repo_root=REPO_ROOT)
    ctx = RunContext(provider_name=provider_name)

    nav = runner.run("browser/web-navigator", {"goal": "Inspect staging homepage", "start_url": url, "page_text": page_text}, context=ctx).output
    tester = runner.run("browser/web-tester", {"input": f"Verify smoke flow on {url}"}, context=ctx).output
    a11y = runner.run("accessibility/accessibility-auditor", {"input": page_text}, context=ctx).output
    return {"navigation": nav, "tests": tester["result"], "accessibility": a11y["result"]}


if __name__ == "__main__":
    print(json.dumps(inspect_staging_app("https://staging.example.org", "<main><h1>Welcome</h1></main>"), indent=2))
