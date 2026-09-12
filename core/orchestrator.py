from core.config import APP_NAME, APP_VERSION


class OriosOrchestrator:
    """Main coordinator for Orios modules."""

    def __init__(self) -> None:
        self.name = APP_NAME
        self.version = APP_VERSION

    def start(self) -> None:
        """Start the Orios core engine."""
        print(f"{self.name} v{self.version}")
        print("Orios core engine initialized.")
        