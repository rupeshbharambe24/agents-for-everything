"""End-to-end Farmer Advisory recipe."""

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


def advise_farmer(
    crop: str,
    symptoms: str,
    location: str,
    locale: str = "mr-IN",
    provider_name: str = "auto",
) -> dict[str, Any]:
    runner = AgentRunner(repo_root=REPO_ROOT)
    ctx = RunContext(provider_name=provider_name, locale=locale)

    crop_dx = runner.run(
        "agriculture/crop-doctor",
        {"input": f"Crop: {crop}. Observed symptom: {symptoms}", "locale": locale},
        context=ctx,
    ).output
    weather = runner.run(
        "agriculture/farm-weather-advisor",
        {"input": f"Spray and irrigation advisory for {crop} in {location}", "locale": locale},
        context=ctx,
    ).output
    prices = runner.run(
        "agriculture/market-price-advisor",
        {"input": f"Today mandi rates for {crop} near {location}", "locale": locale},
        context=ctx,
    ).output
    spoken_text = f"{crop} ({location}): {crop_dx['result']} | {weather['result']} | {prices['result']}"
    audio = runner.run(
        "voice/text-to-speech",
        {"text": spoken_text, "locale": locale},
        context=ctx,
    ).output

    return {
        "locale": locale,
        "crop_advisory": crop_dx,
        "weather_advisory": weather,
        "mandi_prices": prices,
        "spoken_audio": audio,
    }


if __name__ == "__main__":
    print(json.dumps(advise_farmer("Onion", "Leaf yellowing near tips", "Nashik, MH", locale="mr-IN"), indent=2, ensure_ascii=False))
