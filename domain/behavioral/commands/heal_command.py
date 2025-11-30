from typing import Optional
from .command import Command


class HealCommand(Command):
    def __init__(self, target, amount: int):
        self.target = target
        self.amount = amount
        self._prev_health: Optional[int] = None

    def execute(self) -> None:
        self._prev_health = int(self.target.health)
        self.target.heal(self.amount)
    
    def log(self) -> str:
        return f"{self.target.name} was healed for {self.amount} health."
    
    def undo(self) -> None:
        if self._prev_health is not None:
            self.target.health = self._prev_health
