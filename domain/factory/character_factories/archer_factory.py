from domain.factory.character_factories.character_factory_interface import ICharacterFactory
from domain.models.characters.archer import Archer
from domain.models.character_base import Character

class ArcherFactory(ICharacterFactory):
    def create_character(self, name: str) -> Character:
        print(f"[ArcherFactory] Creating a skilled archer named '{name}'")
        return Archer(name)
