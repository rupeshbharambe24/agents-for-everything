from __future__ import annotations
import re
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

_MONTHS = {"january": "01", "jan": "01", "february": "02", "feb": "02", "march": "03", "mar": "03", "april": "04", "apr": "04", "may": "05", "june": "06", "jun": "06", "july": "07", "jul": "07", "august": "08", "aug": "08", "september": "09", "sep": "09", "october": "10", "oct": "10", "november": "11", "nov": "11", "december": "12", "dec": "12"}
_INDIC_NUMBERS = {"pachas hazaar": 50000, "pachas hajar": 50000, "ek lakh": 100000, "bees hazaar": 20000, "das hazaar": 10000}

class StructuredExtractorAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        if runner.provider.config.name != "mock":
            return runner.complete(input_data)
        text = str(input_data["text"])
        fields = [f["id"] if isinstance(f, dict) else str(f) for f in input_data.get("fields", [])]
        out: dict[str, Any] = {}
        conf: dict[str, float] = {}

        if "full_name" in fields:
            m = re.search(
                r"(?:mera naam|my name is|maze naav|en peyar|naa peru|amar naam)\s+(.+?)(?=\s+(?:hai|ahe|and)\b|,|$)",
                text,
                re.I,
            )
            if m:
                words = [w for w in m.group(1).strip().split() if w.isalpha()][:3]
                if words:
                    out["full_name"] = " ".join(w.capitalize() for w in words)
                    conf["full_name"] = 0.95
        if "email" in fields:
            m = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
            if m:
                out["email"] = m.group(0)
                conf["email"] = 0.99
        if "pincode" in fields:
            m = re.search(r"pin\s*(?:code)?\s*(?:is|:)?\s*([1-9][0-9]{3,5})\b", text, re.I) or re.search(
                r"\b([1-9][0-9]{5})\b", text
            )
            if m:
                out["pincode"] = m.group(1)
                conf["pincode"] = 0.96
        if "dob" in fields:
            m = re.search(r"(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})", text)
            if m and m.group(2).lower() in _MONTHS:
                out["dob"] = f"{m.group(3)}-{_MONTHS[m.group(2).lower()]}-{int(m.group(1)):02d}"
                conf["dob"] = 0.95
        if "monthly_income" in fields:
            low = text.lower()
            matched_word = next((val for phrase, val in _INDIC_NUMBERS.items() if phrase in low), None)
            if matched_word is not None:
                out["monthly_income"] = matched_word
                conf["monthly_income"] = 0.92
            else:
                m = re.search(r"income\s+(?:is\s+)?(\d+)", low)
                if m:
                    out["monthly_income"] = int(m.group(1))
                    conf["monthly_income"] = 0.9
        if "mobile_number" in fields:
            m = re.search(r"\b[6-9]\d{9}\b", text)
            if m:
                out["mobile_number"] = m.group(0)
                conf["mobile_number"] = 0.97
        if "city" in fields:
            m = re.search(r"city\s+(?:is\s+)?([A-Z][a-z]+)", text, re.I)
            if m:
                out["city"] = m.group(1).capitalize()
                conf["city"] = 0.93

        return {"extracted": out, "confidence": conf}
