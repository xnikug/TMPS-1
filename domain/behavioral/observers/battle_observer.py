from typing import Dict, Any, List, Optional, Set
from .observer import Observer


class BattleObserver(Observer):
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
        if event != 'victory':
            return

        monsters_defeated = int(data.get('monsters_defeated', 0))
        party = data.get('party', [])

        # Record a readable victory entry
        if monsters_defeated > 0:
            names = ', '.join([getattr(p, 'name', str(p)) for p in party])
            title = f"{names} defeated {monsters_defeated} monsters"
            if title not in self.achievements:
                self.achievements.append(title)

        # Single-battle milestone: massacre
        if monsters_defeated >= 5:
            self._unlock('massacre_5_in_battle', 'Massacre: defeated 5 monsters in one battle')
