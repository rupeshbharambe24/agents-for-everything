"""Check relative Markdown links in docs and top-level files."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "packages" / "core-python" / "src"))
sys.path.insert(0, str(ROOT / "cli" / "src"))

from afe_cli.validator import check_markdown_links  # noqa: E402


def main() -> int:
    broken = check_markdown_links(ROOT)
    if broken:
        for b in broken:
            print(f"BROKEN LINK: {b}", file=sys.stderr)
        return 1
    print("All checked Markdown links resolved cleanly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
