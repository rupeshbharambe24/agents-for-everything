"""Tests for Phase 4 verification badges and afe/v1 -> afe/v2 automated migration."""

from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from agents_for_everything import (
    load_agent_manifest,
    migrate_agent_dir,
    validate_agent_dir,
    verify_agent_dir,
)

REPO_ROOT = Path(__file__).resolve().parents[3]


class Phase4VerifyAndMigrateTests(unittest.TestCase):
    def test_verify_grants_badge_to_clean_s2_and_s4_agents(self) -> None:
        v_rec = verify_agent_dir(
            REPO_ROOT / "agents" / "perception" / "voice" / "voice-form-filler",
            REPO_ROOT,
            run_evals=True,
        )
        self.assertTrue(v_rec.verified, v_rec.issues)
        self.assertEqual(v_rec.badge, "verified")
        self.assertEqual(v_rec.eval_total, 50)
        self.assertTrue(v_rec.digest.startswith("sha256:"))

        kyc_rec = verify_agent_dir(
            REPO_ROOT / "agents" / "industries" / "banking" / "kyc-onboarding",
            REPO_ROOT,
            run_evals=True,
        )
        self.assertTrue(kyc_rec.verified, kyc_rec.issues)
        self.assertTrue(kyc_rec.safety_reviewed)

    def test_verify_rejects_s4_without_safety_review(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(REPO_ROOT / "spec", root / "spec")
            src = REPO_ROOT / "agents" / "industries" / "banking" / "kyc-onboarding"
            dst = root / "agents" / "industries" / "banking" / "kyc-onboarding"
            shutil.copytree(src, dst)
            (dst / "SAFETY_REVIEW.md").unlink()

            rec = verify_agent_dir(dst, root, run_evals=False)
            self.assertFalse(rec.verified)
            self.assertEqual(rec.badge, "unverified")
            self.assertTrue(any("SAFETY_REVIEW.md" in iss for iss in rec.issues))

    def test_migrate_v1_to_v2_roundtrip_validates_and_runs(self) -> None:
        src = REPO_ROOT / "agents" / "industries" / "banking" / "kyc-onboarding"
        with tempfile.TemporaryDirectory() as tmp:
            out_dir = Path(tmp) / "agents" / "industries" / "banking" / "kyc-onboarding"
            written_path, upgraded = migrate_agent_dir(src, REPO_ROOT, out_dir=out_dir)
            self.assertIsNotNone(written_path)
            self.assertEqual(upgraded["apiVersion"], "afe/v2")
            self.assertEqual(upgraded["spec"]["verification"]["badge"], "verified")
            self.assertIn("profiles/regulated-airgapped.yaml", upgraded["spec"]["deployments"]["profiles"])

            errors = validate_agent_dir(out_dir, REPO_ROOT)
            self.assertEqual(errors, [])

            manifest = load_agent_manifest(out_dir)
            self.assertEqual(manifest.id, "banking/kyc-onboarding")
            rec = verify_agent_dir(out_dir, REPO_ROOT, run_evals=True)
            self.assertTrue(rec.verified, rec.issues)


if __name__ == "__main__":
    unittest.main()
