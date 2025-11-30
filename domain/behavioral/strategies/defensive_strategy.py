from typing import Dict, Any, List
import random
from .strategy import CombatStrategy


class DefensiveStrategy(CombatStrategy):
    def choose_action(self, monster, party: List) -> Dict[str, Any]:
        living = [p for p in party if p.is_alive()]
        if not living:
            return {'type': 'wait', 'target': None}

        # If monster health is low, try to defend (or use basic attack less often)
        if hasattr(monster, 'health') and hasattr(monster, 'max_health'):
            health_ratio = monster.health / max(1, monster.max_health)
            if health_ratio < 0.3:
                return {'type': 'defend', 'target': None}

        # 20% chance to use special, otherwise basic
        use_special = random.random() < 0.2
        target = random.choice(living)
        return {'type': 'special' if use_special else 'basic', 'target': target}
