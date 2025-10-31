from domain.models.monsters.monster_base import Monster
import random


class Demon(Monster):
    def __init__(self, name: str, level: int = 1):
        super().__init__(name, level)
        self.strength += 3
        self.intelligence += 2
        self.max_health = int(self.max_health * 1.3)  # Demons are tough
        self.health = self.max_health
    
    def special_attack(self) -> dict:
        damage = random.randint(self.strength + 2, self.strength + self.intelligence)
        return {
            'damage': damage,
            'description': f"{self.name} unleashes HELLFIRE BLAST!"
        }