from domain.models.character_base import Character
import random

class Warrior(Character):
    def __init__(self, name: str):
        super().__init__(name)
        self.max_health = 150
        self.health = self.max_health
        self.strength = 20
        self.intelligence = 5
        self.agility = 8
    
    def special_ability(self) -> str:
        return f"{self.name} uses SHIELD BASH! Stuns enemy and deals massive damage!"
    
    def special_attack(self) -> dict:
        """Warrior's powerful shield bash attack"""
        damage = random.randint(self.strength + 5, self.strength + 15)
        weapon_bonus = self.weapon.damage if self.weapon else 0
        total_damage = damage + weapon_bonus
        return {
            'damage': total_damage,
            'description': f"{self.name} performs a devastating SHIELD BASH!"
        }
