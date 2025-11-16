# Character Component - Leaf node in Composite Pattern
from .squad_component import SquadComponent


class CharacterComponent(SquadComponent):
    
    def __init__(self, character):

        self.character = character
    
    def get_total_damage(self) -> int:
        return self.character.basic_attack()
    
    def get_total_health(self) -> int:
        return self.character.health
    
    def get_members_count(self) -> int:
        return 1
    
    def get_average_level(self) -> float:
        return float(self.character.level)
    
    def display_info(self, indent: int = 0) -> str:
        spacing = "  " * indent
        return (f"{spacing}├─ {self.character.name} "
                f"(Lvl {self.character.level}) | "
                f"HP: {self.character.health}/{self.character.max_health}")
