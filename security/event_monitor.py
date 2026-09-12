import os
import subprocess


def get_recent_security_events(limit: int = 20) -> list[dict]:
    """Best-effort read-only Windows System event snapshot via wevtutil.

    Falls back to an empty list when Windows event access is unavailable.
    """
    if os.name != "nt":
        return []
    try:
        completed = subprocess.run(
            ["wevtutil", "qe", "System", "/c:{0}".format(limit), "/f:text", "/rd:true"],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        if completed.returncode != 0:
            return []

        events = []
        current = {}
        for raw_line in completed.stdout.splitlines():
            line = raw_line.strip()
            if not line:
                if current:
                    events.append(current)
                    current = {}
                continue
            if ":" in line:
                key, value = line.split(":", 1)
                current[key.strip()] = value.strip()
        if current:
            events.append(current)
        return events[:limit]
    except (FileNotFoundError, subprocess.SubprocessError, OSError):
        return []
