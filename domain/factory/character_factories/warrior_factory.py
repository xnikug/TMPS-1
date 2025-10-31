from domain.factory.character_factories.character_factory_interface import ICharacterFactory
from domain.models.characters.warrior import Warrior
from domain.models.character_base import Character

class WarriorFactory(ICharacterFactory):
    def create_character(self, name: str) -> Character:
        print(f"[WarriorFactory] Creating a mighty warrior named '{name}'")
        return Warrior(name)
