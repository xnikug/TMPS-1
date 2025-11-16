# Shield Enchantment Decorator - Reduces incoming damage
from .character_decorator import CharacterDecorator


class ShieldEnchantmentDecorator(CharacterDecorator):
    
    def __init__(self, character, damage_reduction: float = 0.15):
        super().__init__(character)
        # 15% damage reduction by default
        self._damage_reduction = damage_reduction
    
    def take_damage(self, damage: int) -> bool:
        # Reduce incoming damage by percentage
        reduced_damage = int(damage * (1 - self._damage_reduction))
        return self._character.take_damage(reduced_damage)
    
    def get_description(self) -> str:
        reduction_percent = int(self._damage_reduction * 100)
        return (f"  Status: Shield Enchanted\n"
                f"  Damage Reduction: {reduction_percent}%")
