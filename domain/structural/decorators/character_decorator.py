# Base Decorator class for character enhancements
from abc import ABC, abstractmethod


class CharacterDecorator(ABC):
    
    def __init__(self, character):
        self._character = character
    
    @property
    def name(self):
        return self._character.name
    
    @property
    def level(self):
        return self._character.level
    
    @property
    def health(self):
        return self._character.health
    
    @property
    def max_health(self):
        return self._character.max_health
    
    @property
    def strength(self):
        return self._character.strength
    
    @property
    def intelligence(self):
        return self._character.intelligence
    
    @property
    def agility(self):
        return self._character.agility
    
    def take_damage(self, damage: int) -> bool:
        return self._character.take_damage(damage)
    
    def heal(self, amount: int):
        self._character.heal(amount)
    
    def is_alive(self) -> bool:
        return self._character.is_alive()
    
    def basic_attack(self) -> int:
        return self._character.basic_attack()
    
    def special_attack(self) -> dict:
        return self._character.special_attack()
    
    def gain_experience(self, exp: int):
        self._character.gain_experience(exp)
    
    @abstractmethod
    def get_description(self) -> str:
        pass
    
    def __str__(self):
        return f"{self._character.__class__.__name__} '{self.name}' (Level {self.level})\n{self.get_description()}"
