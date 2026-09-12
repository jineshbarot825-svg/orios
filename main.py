from core.orchestrator import OriosOrchestrator


def main() -> None:
    orios = OriosOrchestrator()
    orios.start()


if __name__ == "__main__":
    main()