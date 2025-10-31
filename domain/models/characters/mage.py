from domain.models.character_base import Character
import random

class Mage(Character):
    def __init__(self, name: str):
        super().__init__(name)
        self.max_health = 80
        self.health = self.max_health
        self.mana = 150
        self.strength = 5
        self.intelligence = 25
        self.agility = 7
    
    def special_ability(self) -> str:
        return f"{self.name} casts FIREBALL! Deals massive magical damage!"
    
    def special_attack(self) -> dict:
        """Mage's powerful fireball spell"""
        damage = random.randint(self.intelligence + 8, self.intelligence + 18)
        weapon_bonus = self.weapon.damage if self.weapon else 0
        total_damage = damage + weapon_bonus
        return {
            'damage': total_damage,
            'description': f"{self.name} unleashes a devastating FIREBALL!"
        }
