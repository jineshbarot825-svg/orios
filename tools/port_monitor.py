import psutil


def get_listening_ports() -> list[dict]:
    """Collect TCP listeners on the local machine."""
    ports = []
    seen = set()
    for connection in psutil.net_connections(kind="tcp"):
        try:
            if connection.status != psutil.CONN_LISTEN or not connection.laddr:
                continue
            item = {
                "pid": connection.pid,
                "local_address": f"{connection.laddr.ip}:{connection.laddr.port}",
                "status": connection.status,
            }
            key = (item["pid"], item["local_address"])
            if key not in seen:
                seen.add(key)
                ports.append(item)
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    return ports
