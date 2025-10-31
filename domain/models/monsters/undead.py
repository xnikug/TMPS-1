from domain.models.monsters.monster_base import Monster
import random


class Undead(Monster):
    def __init__(self, name: str, level: int = 1):
        super().__init__(name, level)
        self.intelligence += 3  # Undead are more intelligent
        self.max_health = int(self.max_health * 1.2)  # More health
        self.health = self.max_health
    
    def special_attack(self) -> dict:
        damage = random.randint(self.intelligence, self.intelligence + 8)
        return {
            'damage': damage,
            'description': f"{self.name} casts LIFE DRAIN!"
        }