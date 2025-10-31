from domain.models.character_class import CharacterClass
from domain.factory.character_factories import WarriorFactory, MageFactory, ArcherFactory, RogueFactory
from domain.models.character_base import Character

class CharacterCreator:
    
    @staticmethod
    def get_factory(character_class: CharacterClass):
        factories = {
            CharacterClass.WARRIOR: WarriorFactory(),
            CharacterClass.MAGE: MageFactory(),
            CharacterClass.ARCHER: ArcherFactory(),
            CharacterClass.ROGUE: RogueFactory()
        }
        return factories.get(character_class)
    
    @staticmethod
    def create_character(character_class: CharacterClass, name: str) -> Character:
        factory = CharacterCreator.get_factory(character_class)
        return factory.create_character(name)