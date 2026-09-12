from tools.system_info import get_system_info
from tools.process_monitor import get_running_processes
from tools.network_monitor import get_network_connections
from tools.port_monitor import get_listening_ports
from tools.user_monitor import get_logged_in_users


def test_system_info():
    data = get_system_info()
    assert "hostname" in data
    assert "operating_system" in data


def test_process_monitor():
    data = get_running_processes()
    assert isinstance(data, list)


def test_network_monitor():
    data = get_network_connections()
    assert isinstance(data, list)


def test_port_monitor():
    data = get_listening_ports()
    assert isinstance(data, list)


def test_user_monitor():
    data = get_logged_in_users()
    assert isinstance(data, list)
