from pathlib import Path


DEFAULT_SUSPICIOUS_PATTERNS = (
    "failed",
    "unauthorized",
    "access denied",
    "authentication failure",
    "suspicious",
    "malware",
    "blocked",
    "credential",
)


def scan_log(path: str, patterns: tuple[str, ...] = DEFAULT_SUSPICIOUS_PATTERNS) -> list[dict]:
    """Search an authorized text log for security-relevant patterns."""
    findings = []
    source = Path(path)
    with source.open("r", encoding="utf-8", errors="replace") as handle:
        for line_number, line in enumerate(handle, start=1):
            lowered = line.lower()
            matched = [pattern for pattern in patterns if pattern in lowered]
            if matched:
                findings.append({
                    "line": line_number,
                    "patterns": matched,
                    "text": line.strip(),
                })
    return findings
