"""Tests for YAML parser and JSON Schema validator."""

import json
import tempfile
import unittest
from pathlib import Path

from agents_for_everything._compat import load_yaml, validate_json_schema


class CompatTests(unittest.TestCase):
    def test_yaml_parses_manifest_shapes(self) -> None:
        doc = """
apiVersion: afe/v1
kind: Agent
metadata:
  id: voice/voice-form-filler
  tags: [voice, forms, accessibility]
  maintainers: ["@rupeshbharambe24"]
spec:
  purpose: >
    Lets users complete forms hands-free
    in their own language.
  safety:
    level: S2
    handles_pii: true
  limits:
    max_steps: 25
    max_cost_usd: 0.10
"""
        parsed = load_yaml(doc)
        self.assertEqual(parsed["apiVersion"], "afe/v1")
        self.assertEqual(parsed["metadata"]["tags"], ["voice", "forms", "accessibility"])
        self.assertTrue(parsed["spec"]["safety"]["handles_pii"])
        self.assertEqual(parsed["spec"]["limits"]["max_steps"], 25)
        self.assertAlmostEqual(parsed["spec"]["limits"]["max_cost_usd"], 0.10)
        self.assertIn("hands-free", parsed["spec"]["purpose"])

    def test_json_schema_resolves_afe_types_ref(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            types_dir = Path(tmp)
            (types_dir / "Transcript.schema.json").write_text(
                json.dumps(
                    {
                        "type": "object",
                        "required": ["text"],
                        "properties": {"text": {"type": "string"}},
                    }
                ),
                encoding="utf-8",
            )
            schema = {
                "type": "object",
                "required": ["transcript"],
                "properties": {"transcript": {"$ref": "afe://types/Transcript"}},
            }
            self.assertEqual(
                validate_json_schema({"transcript": {"text": "hello"}}, schema, types_dir),
                [],
            )
            errs = validate_json_schema({"transcript": {}}, schema, types_dir)
            self.assertEqual(len(errs), 1)
            self.assertIn("text", errs[0])


if __name__ == "__main__":
    unittest.main()
