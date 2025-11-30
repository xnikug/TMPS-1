from typing import Dict, Any
from .observer import Observer


class LoggerObserver(Observer):
    def update(self, event: str, data: Dict[str, Any]):
        print(f"[GameEventManager] {event} -> {data}")
