import psutil


def get_network_connections() -> list[dict]:
    """Collect local network connection telemetry."""
    connections = []
    for connection in psutil.net_connections(kind="inet"):
        try:
            local_address = f"{connection.laddr.ip}:{connection.laddr.port}" if connection.laddr else None
            remote_address = f"{connection.raddr.ip}:{connection.raddr.port}" if connection.raddr else None
            connections.append({
                "pid": connection.pid,
                "local_address": local_address,
                "remote_address": remote_address,
                "status": connection.status,
            })
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    return connections
