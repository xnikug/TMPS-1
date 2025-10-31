from domain.factory.character_factories.character_factory_interface import ICharacterFactory
from domain.models.characters.mage import Mage
from domain.models.character_base import Character

class MageFactory(ICharacterFactory):
    def create_character(self, name: str) -> Character:
        print(f"[MageFactory] Creating a powerful mage named '{name}'")
        return Mage(name)
