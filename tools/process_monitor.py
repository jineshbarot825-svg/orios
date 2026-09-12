import psutil


def get_running_processes() -> list[dict]:
    """Collect readable process telemetry; skip protected processes safely."""
    processes = []
    for process in psutil.process_iter(["pid", "name", "exe", "cpu_percent", "memory_info", "username"]):
        try:
            info = process.info
            memory_info = info.get("memory_info")
            processes.append({
                "pid": info.get("pid"),
                "name": info.get("name") or "Unknown",
                "executable": info.get("exe") or "Unavailable",
                "username": info.get("username") or "Unavailable",
                "cpu_percent": float(info.get("cpu_percent") or 0.0),
                "memory_mb": round(memory_info.rss / (1024**2), 2) if memory_info else 0.0,
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return processes
