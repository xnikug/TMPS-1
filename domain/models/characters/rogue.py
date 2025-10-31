from domain.models.character_base import Character
import random

class Rogue(Character):
    def __init__(self, name: str):
        super().__init__(name)
        self.max_health = 90
        self.health = self.max_health
        self.strength = 15
        self.intelligence = 12
        self.agility = 18
    
    def special_ability(self) -> str:
        return f"{self.name} uses BACKSTAB! Critical hit with bonus damage!"
    
    def special_attack(self) -> dict:
        """Rogue's critical backstab attack"""
        damage = random.randint(self.agility + 8, self.agility + 16)
        weapon_bonus = self.weapon.damage if self.weapon else 0
        total_damage = damage + weapon_bonus
        return {
            'damage': total_damage,
            'description': f"{self.name} strikes with a lethal BACKSTAB!"
        }
