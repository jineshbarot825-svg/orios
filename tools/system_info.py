import os
import platform
import socket
import time

import psutil


def get_system_info() -> dict:
    """Collect local system telemetry for defensive monitoring."""
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage(os.path.abspath(os.sep))
    try:
        battery = psutil.sensors_battery()
    except (OSError, NotImplementedError):
        battery = None

    try:
        local_ip = socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        local_ip = "Unavailable"

    boot_time = psutil.boot_time()
    uptime_seconds = max(0.0, time.time() - boot_time)

    return {
        "hostname": socket.gethostname(),
        "operating_system": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "python_version": platform.python_version(),
        "cpu": platform.processor() or "Unknown",
        "cpu_cores": os.cpu_count() or 0,
        "cpu_usage": f"{psutil.cpu_percent(interval=0.2):.1f}%",
        "ram_total_gb": round(memory.total / (1024**3), 2),
        "ram_usage": f"{memory.percent:.1f}%",
        "disk_total_gb": round(disk.total / (1024**3), 2),
        "disk_free_gb": round(disk.free / (1024**3), 2),
        "disk_usage": f"{disk.percent:.1f}%",
        "local_ip": local_ip,
        "battery": None if battery is None else battery.percent,
        "uptime_hours": round(uptime_seconds / 3600, 2),
    }
