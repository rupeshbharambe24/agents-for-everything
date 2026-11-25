"""Integration test for recipes/chat-with-your-docs."""

import importlib.util
import json
import unittest
from pathlib import Path

RECIPE_DIR = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("recipe_chat_docs_app", RECIPE_DIR / "app.py")
assert _spec and _spec.loader
_app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_app)
ask_docs = _app.ask_docs


class ChatWithDocsRecipeTest(unittest.TestCase):
    def test_grounded_qa_with_pii_masking(self) -> None:
        docs = json.loads((RECIPE_DIR / "fixtures" / "sample_docs.json").read_text(encoding="utf-8"))
        res = ask_docs("What is the refund policy?", docs, provider_name="mock")
        self.assertTrue(res["supported"])
        self.assertTrue(res["grounded"])
        self.assertNotIn("support@example.org", res["answer"])
        self.assertGreaterEqual(len(res["citations"]), 1)

        unsupported = ask_docs("What is the quantum encryption key?", docs, provider_name="mock")
        self.assertFalse(unsupported["supported"])


if __name__ == "__main__":
    unittest.main()
