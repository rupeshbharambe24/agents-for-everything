"""Tests for the `afe` CLI and repository validator."""

import shutil
import tempfile
import unittest
from pathlib import Path

from afe_cli.main import main
from agents_for_everything import find_repo_root


class CLITests(unittest.TestCase):
    def test_new_validate_add_export_and_search(self) -> None:
        real_root = find_repo_root()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(real_root / "spec", root / "spec")
            shutil.copytree(real_root / "templates", root / "templates")
            (root / "agents").mkdir()
            (root / "teams").mkdir()
            (root / "recipes").mkdir()

            rc_new = main(
                [
                    "--repo-root",
                    str(root),
                    "new",
                    "--tier",
                    "atomic",
                    "--category",
                    "text",
                    "--slug",
                    "demo-cleaner",
                    "--name",
                    "Demo Cleaner",
                ]
            )
            self.assertEqual(rc_new, 0)
            self.assertTrue((root / "agents" / "information" / "text" / "demo-cleaner" / "agent.yaml").exists())

            rc_val = main(["--repo-root", str(root), "validate"])
            self.assertEqual(rc_val, 0)

            rc_search = main(["--repo-root", str(root), "search", "cleaner"])
            self.assertEqual(rc_search, 0)

            rc_info = main(["--repo-root", str(root), "info", "text/demo-cleaner"])
            self.assertEqual(rc_info, 0)

            rc_add = main(["--repo-root", str(root), "add", "text/demo-cleaner", "--dest", str(root / "copied")])
            self.assertEqual(rc_add, 0)
            self.assertTrue((root / "copied" / "text" / "demo-cleaner" / "agent.yaml").exists())

            rc_export = main(
                [
                    "--repo-root",
                    str(root),
                    "export",
                    "text/demo-cleaner",
                    "--as",
                    "a2a",
                    "--out",
                    str(root / "out"),
                ]
            )
            self.assertEqual(rc_export, 0)
            self.assertTrue((root / "out" / "demo-cleaner.agent-card.json").exists())

            rc_test = main(["--repo-root", str(root), "test", "text/demo-cleaner"])
            self.assertEqual(rc_test, 0)


if __name__ == "__main__":
    unittest.main()
