from domain.factory.monster_factories.monster_factory_interface import IMonsterFactory
from domain.models.monsters import Goblin


class GoblinFactory(IMonsterFactory):
    def create_monster(self, name: str, level: int = 1) -> Goblin:
        return Goblin(name, level)
    
    def get_random_names(self) -> list:
        return ["Grax", "Snarl", "Grib", "Zak", "Nix", "Vex", "Grok", "Blix"]