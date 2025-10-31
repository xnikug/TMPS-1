from domain.models.monsters.monster_base import Monster
import random


class Beast(Monster):
    def __init__(self, name: str, level: int = 1):
        super().__init__(name, level)
        self.agility += 4  # Beasts are faster
        self.strength += 1
    
    def special_attack(self) -> dict:
        damage = random.randint(self.agility, self.agility + self.strength // 2)
        return {
            'damage': damage,
            'description': f"{self.name} unleashes a FERAL POUNCE!"
        }