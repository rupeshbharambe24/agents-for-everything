"""Validate entire agents-for-everything repository (manifests, schemas, links)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "packages" / "core-python" / "src"))
sys.path.insert(0, str(ROOT / "cli" / "src"))

from afe_cli.validator import check_markdown_links, validate_repository  # noqa: E402


def main() -> int:
    errors = validate_repository(ROOT)
    errors.extend(check_markdown_links(ROOT))
    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1
    print("Repository validation passed cleanly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
