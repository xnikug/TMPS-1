from domain.factory.monster_factories.monster_factory_interface import IMonsterFactory
from domain.models.monsters import Beast


class BeastFactory(IMonsterFactory):
    def create_monster(self, name: str, level: int = 1) -> Beast:
        return Beast(name, level)
    
    def get_random_names(self) -> list:
        return ["Dire Wolf", "Shadow Cat", "Iron Bear", "Venom Spider", "Storm Eagle", "Frost Tiger", "Rock Boar", "Lightning Stag"]