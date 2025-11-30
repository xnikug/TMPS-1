from typing import Dict, Any, List
from .observer import Observer
from .kill_milestone_observer import KillMilestoneObserver
from .battle_observer import BattleObserver
from .level_observer import LevelObserver

# This is a composite observer that delegates to specialized achievement observers.
class AchievementObserver(Observer):
    def __init__(self):
        # shared state used by child observers to prevent duplicates
        self.achievements: List[str] = []
        self._unlocked_keys = set()
        # use a mutable single-element list as a shared counter reference
        self._total_ref = [0]

        # specialized observers share the containers
        self._kill_obs = KillMilestoneObserver(self.achievements, self._unlocked_keys, self._total_ref)
        self._battle_obs = BattleObserver(self.achievements, self._unlocked_keys)
        self._level_obs = LevelObserver(self.achievements, self._unlocked_keys)

        # backward-compatible integer snapshot
        self._total_monsters_defeated = 0

    def update(self, event: str, data: Dict[str, Any]):
        # Delegate to all specialized observers. Order matters for side-effects
        self._kill_obs.update(event, data)
        self._battle_obs.update(event, data)
        self._level_obs.update(event, data)

        # Keep snapshot attribute
        try:
            self._total_monsters_defeated = int(self._total_ref[0])
        except Exception:
            self._total_monsters_defeated = 0

    @property
    def total_monsters_defeated(self) -> int:
        return int(self._total_ref[0])

    @property
    def unlocked_keys(self):
        return self._unlocked_keys
