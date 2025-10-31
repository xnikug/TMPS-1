from domain.factory.monster_factories.monster_factory_interface import IMonsterFactory
from domain.models.monsters import Undead


class UndeadFactory(IMonsterFactory):
    def create_monster(self, name: str, level: int = 1) -> Undead:
        return Undead(name, level)
    
    def get_random_names(self) -> list:
        return ["Bone Walker", "Soul Reaper", "Wraith", "Specter", "Lich Lord", "Death Knight", "Ghoul", "Skeleton Mage"]