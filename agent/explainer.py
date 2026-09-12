def explain_findings(findings: list[dict]) -> str:
    """Create a concise human-readable explanation without requiring an external AI service."""
    if not findings:
        return "No rule-based findings were generated from the collected telemetry."
    lines = [f"Orios generated {len(findings)} finding(s):"]
    for finding in findings[:20]:
        lines.append(f"- [{finding.get('severity', 'info').upper()}] {finding.get('message', 'No message')}")
    return "\n".join(lines)
