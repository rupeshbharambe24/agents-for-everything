from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class VoiceFormFillerAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        locale = str(input_data.get("locale", "en-IN"))
        form = input_data["form"]
        transcript = runner.call_agent("voice/speech-to-text", {"audio": input_data["audio"], "locale": locale})
        schema_fields = [{"id": f["id"], "type": f.get("type", "string"), "label": f.get("label", f["id"])} for f in form.get("fields", [])]
        extracted = runner.call_agent("text/structured-extractor", {"text": transcript["text"], "fields": schema_fields})

        merged = dict(input_data.get("prefill") or {})
        for k, v in extracted.get("extracted", {}).items():
            if v not in (None, ""):
                merged[k] = v

        required_fields = [f["id"] for f in form.get("fields", []) if f.get("required", False)]
        rules = {f["id"]: {"format": f["id"] if f["id"] in {"pincode", "dob", "email", "ifsc", "phone"} else f.get("type")} for f in form.get("fields", [])}
        verdict = runner.call_agent("orchestration/verifier", {"data": merged, "required_fields": required_fields, "rules": rules})

        missing = verdict.get("missing", [])
        invalid = verdict.get("invalid", [])
        if missing or invalid:
            ask_target = missing[0] if missing else invalid[0]["field"]
            prompt_text = f"Please provide valid {ask_target.replace('_', ' ')}."
            runner.call_agent("voice/text-to-speech", {"text": prompt_text, "locale": locale})
            return {"values": merged, "confidence": extracted.get("confidence", {}), "missing": missing, "invalid": invalid, "status": "needs_input", "prompt_back": prompt_text, "transcript": transcript}

        if input_data.get("confirm_submit"):
            gate = runner.call_agent("orchestration/human-approval-gate", {"action": "submit", "summary": f"Submit form {form.get('id')} with {len(merged)} fields", "safety_level": "S2", "user_response": "yes"})
            if gate.get("decision") == "approved":
                return {"values": merged, "confidence": extracted.get("confidence", {}), "missing": [], "invalid": [], "status": "submitted", "prompt_back": "Form submitted.", "transcript": transcript}

        runner.call_agent("voice/text-to-speech", {"text": "All required fields captured. Say yes to submit.", "locale": locale})
        return {"values": merged, "confidence": extracted.get("confidence", {}), "missing": [], "invalid": [], "status": "awaiting_confirmation", "prompt_back": "All required fields captured. Say yes to submit.", "transcript": transcript}
