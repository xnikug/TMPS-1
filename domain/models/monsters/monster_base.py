from abc import ABC, abstractmethod
from enum import Enum
import random


class MonsterType(Enum):
    GOBLIN = "Goblin"
    UNDEAD = "Undead"
    BEAST = "Beast"
    DEMON = "Demon"


class Monster(ABC):
    def __init__(self, name: str, level: int = 1):
        self.name = name
        self.level = level
        self.max_health = self._calculate_health()
        self.health = self.max_health
        self.mana = 30 + (level * 5)
        self.strength = 8 + (level * 2)
        self.intelligence = 5 + level
        self.agility = 7 + level
        self.experience_reward = 20 * level
        self.gold_reward = 10 + (level * 5)
    
    def _calculate_health(self):
        return 50 + (self.level * 15)
    
    @abstractmethod
    def special_attack(self) -> dict:
        """Returns attack info with damage and description"""
        pass
    
    def basic_attack(self) -> int:
        """Basic physical attack"""
        damage = random.randint(self.strength // 2, self.strength)
        return damage
    
    def take_damage(self, damage: int) -> bool:
        """Take damage and return True if monster is alive"""
        self.health = max(0, self.health - damage)
        return self.health > 0
    
    def is_alive(self) -> bool:
        return self.health > 0
    
    def __str__(self):
        health_bar = "█" * int((self.health / self.max_health) * 10)
        empty_bar = "░" * (10 - len(health_bar))
        return (f"{self.__class__.__name__} '{self.name}' (Level {self.level})\n"
                f"  HP: [{health_bar}{empty_bar}] {self.health}/{self.max_health}\n"
                f"  STR: {self.strength} | INT: {self.intelligence} | AGI: {self.agility}")