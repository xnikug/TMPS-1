# Character Proxy - Controls access to character data with lazy-loading and logging
from typing import Optional


class CharacterProxy:
    
    def __init__(self, character_class, name: str):
        # Initialize proxy with character class and name, but don't create character yet
        self._character_class = character_class
        self._name = name
        self._character: Optional[object] = None
        self._access_count = 0
        self._access_log = []
    
    def _load_character(self):
        # Lazy-load the actual character object
        if self._character is None:
            print(f"[CharacterProxy] Loading character '{self._name}'...")
            self._character = self._character_class(self._name)
            self._log("Character loaded")
    
    def _log(self, action: str):
        self._access_count += 1
        log_entry = f"[Access #{self._access_count}] {action}"
        self._access_log.append(log_entry)
        print(f"  {log_entry}")
    
    @property
    def name(self):
        self._load_character()
        self._log(f"Accessed name: {self._character.name}")
        return self._character.name
    
    @property
    def level(self):
        self._load_character()
        self._log(f"Accessed level: {self._character.level}")
        return self._character.level
    
    @property
    def health(self):
        self._load_character()
        return self._character.health
    
    @property
    def max_health(self):
        self._load_character()
        return self._character.max_health
    
    @property
    def strength(self):
        self._load_character()
        self._log(f"Accessed strength: {self._character.strength}")
        return self._character.strength
    
    @property
    def intelligence(self):
        self._load_character()
        self._log(f"Accessed intelligence: {self._character.intelligence}")
        return self._character.intelligence
    
    @property
    def agility(self):
        self._load_character()
        self._log(f"Accessed agility: {self._character.agility}")
        return self._character.agility
    
    def basic_attack(self) -> int:
        self._load_character()
        self._log(f"Executed basic attack")
        return self._character.basic_attack()
    
    def special_attack(self) -> dict:
        self._load_character()
        self._log(f"Executed special attack")
        return self._character.special_attack()
    
    def take_damage(self, damage: int) -> bool:
        self._load_character()
        self._log(f"Took {damage} damage")
        return self._character.take_damage(damage)
    
    def heal(self, amount: int):
        self._load_character()
        self._log(f"Healed for {amount} HP")
        self._character.heal(amount)
    
    def is_alive(self) -> bool:
        self._load_character()
        return self._character.is_alive()
    
    def gain_experience(self, exp: int):
        self._load_character()
        self._log(f"Gained {exp} experience")
        self._character.gain_experience(exp)
    
    def get_access_log(self) -> str:
        return '\n'.join(self._access_log)
    
    def get_access_count(self) -> int:
        return self._access_count
    
    def __str__(self):
        self._load_character()
        self._log("Accessed string representation")
        return str(self._character)
