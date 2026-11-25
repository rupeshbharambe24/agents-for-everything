from __future__ import annotations
from pathlib import Path
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

_BUCKET = {".pdf": "documents", ".docx": "documents", ".md": "notes", ".csv": "data", ".json": "data", ".png": "images", ".jpg": "images", ".mp3": "audio", ".wav": "audio"}

class FileOrganizerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        plan = []
        for f in input_data.get("files", []):
            ext = Path(str(f)).suffix.lower()
            bucket = _BUCKET.get(ext, "other")
            plan.append({"source": f, "destination": f"{bucket}/{Path(str(f)).name}"})
        return {"plan": plan, "dry_run": True}
