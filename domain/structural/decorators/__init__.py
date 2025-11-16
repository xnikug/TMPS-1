"""
Decorator Pattern - Adds additional behaviors to characters dynamically.
Allows enhancing character abilities without modifying the original class.
"""
from .character_decorator import CharacterDecorator
from .spell_buff_decorator import SpellBuffDecorator
from .shield_enchantment_decorator import ShieldEnchantmentDecorator
from .strength_potion_decorator import StrengthPotionDecorator

__all__ = [
    'CharacterDecorator',
    'SpellBuffDecorator',
    'ShieldEnchantmentDecorator',
    'StrengthPotionDecorator'
]
