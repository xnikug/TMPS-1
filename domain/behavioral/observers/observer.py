from abc import ABC, abstractmethod
from typing import Dict, Any


class Observer(ABC):
    @abstractmethod
    def update(self, event: str, data: Dict[str, Any]):
        pass
