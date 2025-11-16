# Spell Buff Decorator - Enhances character's intelligence and mana
from .character_decorator import CharacterDecorator


class SpellBuffDecorator(CharacterDecorator):
    
    def __init__(self, character, intelligence_bonus: int = 5, mana_bonus: int = 20):
        super().__init__(character)
        self._intelligence_bonus = intelligence_bonus
        self._mana_bonus = mana_bonus
    
    @property
    def intelligence(self):
        return self._character.intelligence + self._intelligence_bonus
    
    @property
    def mana(self):
        return self._character.mana + self._mana_bonus
    
    def special_attack(self) -> dict:
        base_attack = self._character.special_attack()
        # 20% bonus damage
        bonus_damage = int(base_attack['damage'] * 0.2)
        return {
            'damage': base_attack['damage'] + bonus_damage,
            'description': f"{base_attack['description']} [SPELL ENHANCED +20%]"
        }
    
    def get_description(self) -> str:
        return (f"  Status: Spell Buffed\n"
                f"  INT: {self._character.intelligence} + {self._intelligence_bonus} = {self.intelligence}\n"
                f"  Mana: {self._character.mana} + {self._mana_bonus} = {self.mana}")
