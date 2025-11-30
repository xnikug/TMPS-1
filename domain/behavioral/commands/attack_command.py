from typing import Optional
from .command import Command


class AttackCommand(Command):
    def __init__(self, attacker, target):
        self.attacker = attacker
        self.target = target
        self._damage_dealt: Optional[int] = None

    def execute(self) -> None:
        dmg = self.attacker.basic_attack()
        self._damage_dealt = dmg
        self.target.take_damage(dmg)
    
    def log(self) -> str:
        return f"{self.attacker.name} attacked {self.target.name} for {self._damage_dealt} damage."
    
    def undo(self) -> None:
        if self._damage_dealt is not None:
            # best-effort restore health (cannot resurrect reliably)
            self.target.health = min(self.target.max_health, self.target.health + self._damage_dealt)
