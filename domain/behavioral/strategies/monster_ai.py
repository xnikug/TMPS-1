from typing import Dict, Any, List, Optional
import statistics

from .strategy import CombatStrategy
from .aggressive_strategy import AggressiveStrategy
from .defensive_strategy import DefensiveStrategy


class MonsterAI:
    def __init__(self, monster, strategy: Optional[CombatStrategy] = None, config: Optional[Dict[str, Any]] = None):
        self.monster = monster
        self._strategy = strategy
        self._config = config or {
            'low_health_threshold': 0.3,  # below this ratio prefer defensive
            'aggressive_party_size': 3,    # if party size >= this prefer aggressive
        }

    def set_strategy(self, strategy: CombatStrategy) -> None:
        self._strategy = strategy

    @property
    def current_strategy_name(self) -> Optional[str]:
        return self._strategy.__class__.__name__ if self._strategy is not None else None

    def auto_select(self, party: List) -> CombatStrategy:
        # Monster health ratio
        mh = getattr(self.monster, 'health', None)
        mmh = getattr(self.monster, 'max_health', None)
        try:
            health_ratio = float(mh) / max(1.0, float(mmh)) if mh is not None and mmh is not None else 1.0
        except Exception:
            health_ratio = 1.0

        # Forced behavior flag
        if getattr(self.monster, 'aggressive', False):
            return AggressiveStrategy()

        # Low health -> defend
        if health_ratio < float(self._config.get('low_health_threshold', 0.3)):
            return DefensiveStrategy()

        # Party analysis
        living = [p for p in party if getattr(p, 'is_alive', lambda: True)()]
        party_size = len(living)

        # Level comparison
        try:
            max_party_level = max(getattr(p, 'level', 0) for p in living) if living else 0
        except Exception:
            max_party_level = 0

        monster_level = getattr(self.monster, 'level', 0)
        if monster_level >= max_party_level + 2:
            return AggressiveStrategy()

        if party_size >= int(self._config.get('aggressive_party_size', 3)):
            return AggressiveStrategy()

        # Average enemy health ratio
        try:
            avg_enemy_hr = statistics.mean(
                (float(getattr(p, 'health', 0)) / max(1.0, float(getattr(p, 'max_health', 1)))) for p in living
            ) if living else 1.0
        except Exception:
            avg_enemy_hr = 1.0

        if avg_enemy_hr < 0.5:
            return AggressiveStrategy()

        # Fallback
        return DefensiveStrategy()

    def decide(self, party: List) -> Dict[str, Any]:
        # If no explicit strategy set, auto-select based on party context
        if self._strategy is None:
            self._strategy = self.auto_select(party)
        return self._strategy.choose_action(self.monster, party)
