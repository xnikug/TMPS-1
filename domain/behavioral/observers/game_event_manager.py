from typing import Dict, Any, List
from .observer import Observer
import threading

class GameEventManager:
    _instance = None
    _initialized = False
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None: 
                    print("[GameEventManager] Creating new GameEventManager instance")
                    cls._instance = super(GameEventManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self._observers: List[Observer] = []

    def register(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, event: str, data: Dict[str, Any] = None) -> None:
        if data is None:
            data = {}
        for obs in list(self._observers):
            try:
                obs.update(event, data)
            except Exception as e:
                print(f"Error notifying observer: {e}")
                continue
