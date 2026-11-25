# Basic Example — voice/voice-form-filler

```bash
afe run voice/voice-form-filler --input '{"form": {"id": "loan_basic", "fields": [{"id": "full_name", "label": "Full Name", "type": "string", "required": true}, {"id": "dob", "label": "DOB", "type": "date", "required": true}, {"id": "pincode", "label": "PIN", "type": "string", "required": true}, {"id": "monthly_income", "label": "Income", "type": "number", "required": true}, {"id": "mobile_number", "label": "Mobile", "type": "phone", "required": true}, {"id": "loan_amount", "label": "Loan", "type": "number", "required": true}]}, "audio": {"format": "text-simulated", "transcript_hint": "mera naam Priya Sharma hai, DOB 12 March 1990, PIN 411001, monthly income pachas hazaar", "locale_hint": "hi-IN"}, "locale": "hi-IN"}'
```
