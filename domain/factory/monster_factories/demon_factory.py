from domain.factory.monster_factories.monster_factory_interface import IMonsterFactory
from domain.models.monsters import Demon


class DemonFactory(IMonsterFactory):
    def create_monster(self, name: str, level: int = 1) -> Demon:
        return Demon(name, level)
    
    def get_random_names(self) -> list:
        return ["Bael", "Malphas", "Asmodeus", "Belial", "Mammon", "Leviathan", "Belphegor", "Beelzebub"]