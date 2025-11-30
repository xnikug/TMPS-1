from typing import Dict, Any, List
import random
from .strategy import CombatStrategy


class AggressiveStrategy(CombatStrategy):
    def choose_action(self, monster, party: List) -> Dict[str, Any]:
        living = [p for p in party if p.is_alive()]
        if not living:
            return {'type': 'wait', 'target': None}

        # 60% chance to use special attack
        use_special = random.random() < 0.6
        target = min(living, key=lambda p: p.health)
        return {'type': 'special' if use_special else 'basic', 'target': target}
