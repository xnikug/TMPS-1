from domain.factory.character_factories.character_factory_interface import ICharacterFactory
from domain.models.characters.rogue import Rogue
from domain.models.character_base import Character

class RogueFactory(ICharacterFactory):
    def create_character(self, name: str) -> Character:
        print(f"[RogueFactory] Creating a stealthy rogue named '{name}'")
        return Rogue(name)
