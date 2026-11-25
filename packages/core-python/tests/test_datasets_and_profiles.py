"""Tests for deployment profiles, local-onprem provider config, and shared datasets."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from agents_for_everything._compat import load_yaml_file
from agents_for_everything.providers.factory import resolve_provider

REPO_ROOT = Path(__file__).resolve().parents[3]


class DatasetsAndProfilesTests(unittest.TestCase):
    def test_deployment_profiles_valid(self) -> None:
        profiles_dir = REPO_ROOT / "profiles"
        expected = ("local-onprem.yaml", "regulated-airgapped.yaml", "low-bandwidth-edge.yaml")
        for fname in expected:
            data = load_yaml_file(profiles_dir / fname)
            self.assertEqual(data["apiVersion"], "afe/v1")
            self.assertEqual(data["kind"], "Profile")
            self.assertEqual(data["spec"]["provider"], "ollama")
            self.assertTrue(data["spec"]["safety"]["mask_pii_in_traces"])
            self.assertFalse(data["spec"]["safety"]["allow_auto_approve_s3_s4"])

    def test_ollama_provider_resolution_for_onprem(self) -> None:
        provider = resolve_provider("ollama", model="qwen2.5:14b")
        self.assertEqual(provider.config.name, "ollama")
        self.assertEqual(provider.config.model, "qwen2.5:14b")

    def test_shared_eval_datasets_valid_jsonl(self) -> None:
        ds_dir = REPO_ROOT / "evals" / "datasets"
        for fname in (
            "multilingual_form_utterances.jsonl",
            "indic_voice_queries.jsonl",
            "regulated_safety_prompts.jsonl",
        ):
            lines = [ln for ln in (ds_dir / fname).read_text(encoding="utf-8").splitlines() if ln.strip()]
            self.assertGreaterEqual(len(lines), 10, fname)
            for ln in lines:
                obj = json.loads(ln)
                self.assertIn("id", obj)


if __name__ == "__main__":
    unittest.main()
