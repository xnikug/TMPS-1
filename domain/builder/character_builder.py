from domain.models.character_base import Character
from domain.models.characters import Warrior, Mage, Archer, Rogue

class CharacterBuilder:
    def __init__(self):
        self._character = None
        self._name = "Unknown Hero"
        self._base_class = "warrior"
    
    def set_base_class(self, class_type: str):
        self._base_class = class_type.lower()
        return self
    
    def set_name(self, name: str):
        self._name = name
        return self
    
    def set_level(self, level: int):
        if not self._character:
            self._create_base_character()
        self._character.level = level
        return self
    
    def set_health(self, health: int):
        if not self._character:
            self._create_base_character()
        self._character.health = health
        return self
    
    def set_mana(self, mana: int):
        if not self._character:
            self._create_base_character()
        self._character.mana = mana
        return self
    
    def set_strength(self, strength: int):
        if not self._character:
            self._create_base_character()
        self._character.strength = strength
        return self
    
    def set_intelligence(self, intelligence: int):
        if not self._character:
            self._create_base_character()
        self._character.intelligence = intelligence
        return self
    
    def set_agility(self, agility: int):
        if not self._character:
            self._create_base_character()
        self._character.agility = agility
        return self
    
    def equip_weapon(self, weapon):
        if not self._character:
            self._create_base_character()
        self._character.weapon = weapon
        return self
    
    def equip_armor(self, armor):
        if not self._character:
            self._create_base_character()
        self._character.armor = armor
        return self
    
    def add_accessory(self, accessory):
        if not self._character:
            self._create_base_character()
        self._character.accessories.append(accessory)
        return self
    
    def _create_base_character(self):
        class_map = {
            'warrior': Warrior,
            'mage': Mage,
            'archer': Archer,
            'rogue': Rogue
        }
        character_class = class_map.get(self._base_class, Warrior)
        self._character = character_class(self._name)
    
    def build(self) -> Character:
        if not self._character:
            self._create_base_character()
        
        print(f"[CharacterBuilder] Built custom character: {self._name}")
        result = self._character
        self.reset()
        return result
    
    def reset(self):
        self._character = None
        self._name = "Unknown Hero"
        self._base_class = "warrior"