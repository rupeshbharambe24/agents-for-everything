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

            rc_export_all = main(
                [
                    "--repo-root",
                    str(root),
                    "export",
                    "--all",
                    "--as",
                    "subagent",
                    "--out",
                    str(root / "out_all"),
                ]
            )
            self.assertEqual(rc_export_all, 0)
            self.assertTrue((root / "out_all" / "text" / "demo-cleaner.md").exists())
            self.assertTrue((root / "out_all" / "text" / "demo-cleaner.toml").exists())

            rc_test = main(["--repo-root", str(root), "test", "text/demo-cleaner"])
            self.assertEqual(rc_test, 0)

            rc_verify = main(["--repo-root", str(root), "verify", "text/demo-cleaner"])
            self.assertEqual(rc_verify, 0)

            migrated_dir = root / "migrated" / "information" / "text" / "demo-cleaner"
            rc_migrate = main(
                [
                    "--repo-root",
                    str(root),
                    "migrate",
                    "text/demo-cleaner",
                    "--out",
                    str(migrated_dir),
                ]
            )
            self.assertEqual(rc_migrate, 0)
            self.assertIn("apiVersion: afe/v2", (migrated_dir / "agent.yaml").read_text(encoding="utf-8"))
            rc_verify_v2 = main(["--repo-root", str(root), "verify", str(migrated_dir), "--skip-evals"])
            self.assertEqual(rc_verify_v2, 0)


if __name__ == "__main__":
    unittest.main()
