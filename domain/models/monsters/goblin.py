from domain.models.monsters.monster_base import Monster
import random


class Goblin(Monster):
    def __init__(self, name: str, level: int = 1):
        super().__init__(name, level)
        self.strength += 2
    
    def special_attack(self) -> dict:
        damage = random.randint(self.strength, self.strength + 5)
        return {
            'damage': damage,
            'description': f"{self.name} performs a DIRTY STRIKE!"
        }