# Orios

Orios is a local, defensive cybersecurity assistant focused on system monitoring, threat detection, security automation, file/log analysis, and reporting.

## Core purpose

1. System security monitoring
2. File and log analysis
3. Suspicious activity detection
4. Security automation
5. AI-assisted explanations and reports
6. Authorized security checks only

## Current MVP capabilities

- System telemetry
- Process monitoring
- Network connection monitoring
- Listening-port monitoring
- User/session monitoring
- Best-effort Windows System event collection
- Rule-based suspicious-activity detection
- SHA-256 file analysis
- Text log scanning
- Read-only authorized checks
- JSON reporting
- Local explanation layer with no API key required
- Basic pytest coverage

## Setup

```powershell
python -m venv .venv
.venv\\Scripts\\activate
python -m pip install -r requirements.txt
python main.py
```

## Test

```powershell
pytest -q
```

## Safety

Use Orios only on systems and data you own or are explicitly authorized to monitor or assess. The included checks are read-only and defensive.
