from domain.models.character_base import Character
import random

class Archer(Character):
    def __init__(self, name: str):
        super().__init__(name)
        self.max_health = 100
        self.health = self.max_health
        self.strength = 12
        self.intelligence = 10
        self.agility = 22
    
    def special_ability(self) -> str:
        return f"{self.name} fires MULTI-SHOT! Hits multiple enemies at once!"
    
    def special_attack(self) -> dict:
        """Archer's precision shot attack"""
        damage = random.randint(self.agility + 6, self.agility + 14)
        weapon_bonus = self.weapon.damage if self.weapon else 0
        total_damage = damage + weapon_bonus
        return {
            'damage': total_damage,
            'description': f"{self.name} fires a precise MULTI-SHOT!"
        }
