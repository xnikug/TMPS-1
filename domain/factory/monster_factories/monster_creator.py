from domain.factory.monster_factories.monster_factory_interface import IMonsterFactory
from domain.factory.monster_factories.goblin_factory import GoblinFactory
from domain.factory.monster_factories.undead_factory import UndeadFactory
from domain.factory.monster_factories.beast_factory import BeastFactory
from domain.factory.monster_factories.demon_factory import DemonFactory
from domain.models.monsters import Monster, MonsterType
import random


class MonsterCreator:
    """Factory creator for monsters, similar to CharacterCreator"""
    
    @staticmethod
    def get_factory(monster_type: MonsterType) -> IMonsterFactory:
        factories = {
            MonsterType.GOBLIN: GoblinFactory(),
            MonsterType.UNDEAD: UndeadFactory(),
            MonsterType.BEAST: BeastFactory(),
            MonsterType.DEMON: DemonFactory()
        }
        return factories.get(monster_type)
    
    @staticmethod
    def create_monster(monster_type: MonsterType, name: str, level: int = 1) -> Monster:
        factory = MonsterCreator.get_factory(monster_type)
        return factory.create_monster(name, level)
    
    @staticmethod
    def create_random_monster(level: int = 1) -> Monster:
        monster_type = random.choice(list(MonsterType))
        factory = MonsterCreator.get_factory(monster_type)
        return factory.create_with_random_name(level)
    
    @staticmethod
    def create_monster_wave(count: int, level: int = 1) -> list:
        """Create a wave of random monsters for combat"""
        return [MonsterCreator.create_random_monster(level) for _ in range(count)]