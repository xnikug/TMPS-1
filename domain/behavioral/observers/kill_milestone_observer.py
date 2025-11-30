from typing import Dict, Any, List, Optional, Set
from .observer import Observer


class KillMilestoneObserver(Observer):
    def __init__(self, achievements: Optional[List[str]] = None, unlocked_keys: Optional[Set[str]] = None, total_ref: Optional[List[int]] = None):
        self.achievements: List[str] = achievements if achievements is not None else []
        # total_ref is a mutable container holding the total count at index 0
        self._total_ref = total_ref if total_ref is not None else [0]
        self._unlocked_keys = unlocked_keys if unlocked_keys is not None else set()

    def _unlock(self, key: str, title: str) -> None:
        if key in self._unlocked_keys:
            return
        self._unlocked_keys.add(key)
        self.achievements.append(title)
        print(f"[Achievement] Unlocked: {title}")

    def _get_total(self) -> int:
        return int(self._total_ref[0])

    def _add_total(self, amount: int) -> None:
        self._total_ref[0] = int(self._total_ref[0]) + int(amount)

    def update(self, event: str, data: Dict[str, Any]):
        # Victory contributes to cumulative kills as well
        if event == 'victory':
            monsters_defeated = int(data.get('monsters_defeated', 0))
            prev_total = self._get_total()
            self._add_total(monsters_defeated)

            if prev_total < 1 <= self._get_total():
                self._unlock('first_blood', 'First Blood: defeated your first monster')

            if prev_total < 20 <= self._get_total():
                self._unlock('monster_hunter_20_total', 'Monster Hunter: defeated 20 monsters total')

        elif event == 'monster_killed':
            count = int(data.get('count', 1))
            prev_total = self._get_total()
            self._add_total(count)

            if prev_total < 1 <= self._get_total():
                self._unlock('first_blood', 'First Blood: defeated your first monster')

            if prev_total < 20 <= self._get_total():
                self._unlock('monster_hunter_20_total', 'Monster Hunter: defeated 20 monsters total')
