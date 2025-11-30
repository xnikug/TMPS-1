from abc import ABC, abstractmethod
from typing import Dict, Any, List


class CombatStrategy(ABC):
    @abstractmethod
    def choose_action(self, monster, party: List) -> Dict[str, Any]:
        pass
