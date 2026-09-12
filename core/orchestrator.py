from core.config import APP_NAME, APP_VERSION, MONITOR_LIMIT
from tools.system_info import get_system_info
from tools.process_monitor import get_running_processes
from tools.network_monitor import get_network_connections
from tools.port_monitor import get_listening_ports
from tools.user_monitor import get_logged_in_users
from security.event_monitor import get_recent_security_events
from security.detection_engine import detect_findings
from automation.safe_checks import run_authorized_checks
from agent.explainer import explain_findings
from reporting.report_writer import write_json_report


class OriosOrchestrator:
    """Coordinate local, defensive Orios monitoring."""

    def __init__(self) -> None:
        self.name = APP_NAME
        self.version = APP_VERSION

    def start(self) -> None:
        print(f"{self.name} v{self.version}")
        print("Orios defensive monitoring engine initialized.")

        system_info = get_system_info()
        processes = get_running_processes()
        connections = get_network_connections()
        listening_ports = get_listening_ports()
        users = get_logged_in_users()
        events = get_recent_security_events(limit=MONITOR_LIMIT)
        checks = run_authorized_checks()
        findings = detect_findings(processes, connections, listening_ports, users)
        explanation = explain_findings(findings)

        print("\n=== System Information ===")
        for key, value in system_info.items():
            print(f"{key}: {value}")

        print("\n=== Monitoring Summary ===")
        print(f"Processes: {len(processes)}")
        print(f"Network connections: {len(connections)}")
        print(f"Listening ports: {len(listening_ports)}")
        print(f"Active user sessions: {len(users)}")
        print(f"Recent system events: {len(events)}")
        print(f"Findings: {len(findings)}")

        print("\n=== Findings ===")
        print(explanation)

        report_path = write_json_report({
            "system_info": system_info,
            "processes": processes[:MONITOR_LIMIT],
            "network_connections": connections[:MONITOR_LIMIT],
            "listening_ports": listening_ports[:MONITOR_LIMIT],
            "users": users,
            "recent_events": events,
            "authorized_checks": checks,
            "findings": findings,
        })
        print(f"\nReport written to: {report_path}")
