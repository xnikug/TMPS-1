from typing import Dict, Any, List, Optional, Set
from .observer import Observer


class LevelObserver(Observer):
    def __init__(self, achievements: Optional[List[str]] = None, unlocked_keys: Optional[Set[str]] = None):
        self.achievements: List[str] = achievements if achievements is not None else []
        self._unlocked_keys = unlocked_keys if unlocked_keys is not None else set()

    def _unlock(self, key: str, title: str) -> None:
        if key in self._unlocked_keys:
            return
        self._unlocked_keys.add(key)
        self.achievements.append(title)
        print(f"[Achievement] Unlocked: {title}")

    def update(self, event: str, data: Dict[str, Any]):
        if event != 'level_up':
            return

        char = data.get('character')
        if not char:
            return

        prev_level = data.get('previous_level')
        try:
            current_level = int(getattr(char, 'level', 0))
        except Exception:
            return

        if prev_level is None:
            prev_level = max(0, current_level - 1)
        
        # First level-up (reaching level >=2)
        if prev_level < 2 <= current_level:
            self._unlock(f"{char.name}_first_levelup", f"{char.name} achieved their first level up")

        # Milestones
        milestones = ((5, 'Seasoned'), (10, 'Veteran'), (20, 'Legend'))
        for threshold, label in milestones:
            if prev_level < threshold <= current_level:
                self._unlock(f"{char.name}_level_{threshold}", f"{char.name} reached level {threshold} ({label})")
