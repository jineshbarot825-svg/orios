import platform


def run_authorized_checks() -> list[dict]:
    """Run lightweight, read-only local security checks."""
    checks = []
    checks.append({"check": "platform", "status": "info", "detail": platform.platform()})
    checks.append({"check": "python", "status": "info", "detail": platform.python_version()})
    return checks
