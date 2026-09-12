from core.config import SUSPICIOUS_PORTS


def detect_findings(processes: list[dict], connections: list[dict], listening_ports: list[dict], users: list[dict]) -> list[dict]:
    """Apply simple explainable defensive rules to local telemetry."""
    findings = []

    for process in processes:
        name = (process.get("name") or "").lower()
        if name in {"powershell.exe", "cmd.exe", "wscript.exe", "cscript.exe", "mshta.exe"} and process.get("cpu_percent", 0) >= 50:
            findings.append({
                "severity": "medium",
                "type": "high_cpu_shell",
                "message": f"Shell process {process.get('name')} (PID {process.get('pid')}) is using high CPU.",
            })

    for port in listening_ports:
        address = port.get("local_address") or ""
        try:
            port_number = int(address.rsplit(":", 1)[-1])
        except ValueError:
            continue
        if port_number in SUSPICIOUS_PORTS:
            findings.append({
                "severity": "medium",
                "type": "sensitive_listener",
                "message": f"Process {port.get('pid')} is listening on port {port_number} ({address}).",
            })

    for connection in connections:
        if connection.get("status") == "ESTABLISHED" and connection.get("remote_address"):
            findings.append({
                "severity": "info",
                "type": "established_connection",
                "message": f"PID {connection.get('pid')} has an established connection to {connection.get('remote_address')}.",
            })

    if len(users) > 1:
        findings.append({
            "severity": "info",
            "type": "multiple_sessions",
            "message": f"Multiple active user sessions detected: {len(users)}.",
        })

    return findings
