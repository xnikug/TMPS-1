from abc import ABC, abstractmethod
import random

class Character(ABC):
    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.experience = 0
        self.experience_to_next_level = 100
        self.max_health = 100
        self.health = self.max_health
        self.mana = 50
        self.strength = 10
        self.intelligence = 10
        self.agility = 10
        self.weapon = None
        self.armor = None
        self.accessories = []
    
    @abstractmethod
    def special_ability(self) -> str:
        pass
    
    def basic_attack(self) -> int:
        base_damage = random.randint(self.strength // 2, self.strength)
        weapon_bonus = self.weapon.damage if self.weapon else 0
        return base_damage + weapon_bonus
    
    def special_attack(self) -> dict:
        damage = random.randint(self.strength, self.strength + 10)
        return {
            'damage': damage,
            'description': self.special_ability()
        }
    
    def take_damage(self, damage: int) -> bool:

        armor_defense = self.armor.defense if self.armor else 0
        actual_damage = max(1, damage - armor_defense)  # Minimum 1 damage
        self.health = max(0, self.health - actual_damage)
        return self.health > 0
    
    def heal(self, amount: int):

        self.health = min(self.max_health, self.health + amount)
    
    def is_alive(self) -> bool:
        return self.health > 0
    
    def gain_experience(self, exp: int):

        self.experience += exp
        while self.experience >= self.experience_to_next_level:
            self.level_up()
    
    def level_up(self):
        self.experience -= self.experience_to_next_level
        self.level += 1
        
        # Increase stats on level up
        old_max_health = self.max_health
        self.max_health += 20
        self.mana += 10
        self.strength += 2
        self.intelligence += 2
        self.agility += 2
        
        # Heal to full when leveling up
        health_gained = self.max_health - old_max_health
        self.health += health_gained
        
        # Increase experience requirement
        self.experience_to_next_level = int(self.experience_to_next_level * 1.5)
        
        print(f"🎉 {self.name} leveled up to Level {self.level}!")
        print(f"   Health: +{health_gained} (now {self.health}/{self.max_health})")
        print(f"   All stats increased by 2!")
    
    def get_health_bar(self) -> str:

        if self.max_health == 0:
            return "[░░░░░░░░░░] 0/0"
        health_ratio = self.health / self.max_health
        filled_bars = int(health_ratio * 10)
        health_bar = "█" * filled_bars
        empty_bar = "░" * (10 - filled_bars)
        return f"[{health_bar}{empty_bar}] {self.health}/{self.max_health}"
    
    def __str__(self):
        return (f"{self.__class__.__name__} '{self.name}' (Level {self.level})\n"
                f"  HP: {self.get_health_bar()}\n"
                f"  Mana: {self.mana} | EXP: {self.experience}/{self.experience_to_next_level}\n"
                f"  STR: {self.strength} | INT: {self.intelligence} | AGI: {self.agility}\n"
                f"  Weapon: {self.weapon.name if self.weapon else 'None'}\n"
                f"  Armor: {self.armor.name if self.armor else 'None'}")
