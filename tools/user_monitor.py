import psutil


def get_logged_in_users() -> list[dict]:
    """Collect active local user/session information."""
    users = []
    for user in psutil.users():
        users.append({
            "username": user.name,
            "terminal": user.terminal,
            "host": user.host,
            "started": user.started,
        })
    return users
