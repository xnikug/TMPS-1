# Strength Potion Decorator - Temporarily boosts character's strength and damage
from .character_decorator import CharacterDecorator


class StrengthPotionDecorator(CharacterDecorator):
    
    def __init__(self, character, strength_bonus: int = 8):
        super().__init__(character)
        self._strength_bonus = strength_bonus
    
    @property
    def strength(self):
        return self._character.strength + self._strength_bonus
    
    def basic_attack(self) -> int:
        base_damage = self._character.basic_attack()
        # Strength boost increases basic attack damage
        bonus_damage = self._strength_bonus
        return base_damage + bonus_damage
    
    def get_description(self) -> str:
        return (f"  Status: Strength Potion Active\n"
                f"  STR: {self._character.strength} + {self._strength_bonus} = {self.strength}")
