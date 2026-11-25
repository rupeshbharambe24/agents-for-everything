import importlib.util
import unittest
from pathlib import Path

RECIPE_DIR = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("recipe_farmer_app", RECIPE_DIR / "app.py")
assert _spec and _spec.loader
_app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_app)


class FarmerAdvisoryTest(unittest.TestCase):
    def test_multilingual_farmer_workflow(self) -> None:
        res = _app.advise_farmer(
            crop="Wheat",
            symptoms="Yellow rust stripes on lower leaves",
            location="Ludhiana, PB",
            locale="hi-IN",
            provider_name="mock",
        )
        self.assertEqual(res["locale"], "hi-IN")
        self.assertIn("agriculture/crop-doctor", res["crop_advisory"]["result"])
        self.assertIn("agriculture/farm-weather-advisor", res["weather_advisory"]["result"])
        self.assertIn("agriculture/market-price-advisor", res["mandi_prices"]["result"])
        self.assertEqual(res["spoken_audio"]["locale"], "hi-IN")
        self.assertTrue(res["spoken_audio"]["audio_uri"].startswith("afe://"))


if __name__ == "__main__":
    unittest.main()
