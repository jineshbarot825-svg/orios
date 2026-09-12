import json
from pathlib import Path
from datetime import datetime, timezone


def write_json_report(data: dict, output_path: str = "workspace/orios_report.json") -> str:
    """Write a machine-readable Orios report."""
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        **data,
    }
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    return str(destination)
