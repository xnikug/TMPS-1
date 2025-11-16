# Squad - Composite node in Composite Pattern

from typing import List
from .squad_component import SquadComponent


class Squad(SquadComponent):
    
    def __init__(self, name: str):
        self.name = name
        self.members: List[SquadComponent] = []
    
    def add_member(self, component: SquadComponent) -> None:
        self.members.append(component)
    
    def remove_member(self, component: SquadComponent) -> None:
        if component in self.members:
            self.members.remove(component)
    
    def get_total_damage(self) -> int:
        return sum(member.get_total_damage() for member in self.members)
    
    def get_total_health(self) -> int:
        return sum(member.get_total_health() for member in self.members)
    
    def get_members_count(self) -> int:
        return sum(member.get_members_count() for member in self.members)
    
    def get_average_level(self) -> float:
        if not self.members:
            return 0.0
        return self.get_total_level() / self.get_members_count()
    
    def get_total_level(self) -> int:
        total = 0
        for member in self.members:
            if isinstance(member, Squad):
                total += member.get_total_level()
            else:
                total += int(member.get_average_level())
        return total
    
    def display_info(self, indent: int = 0) -> str:
        spacing = "  " * indent
        info = f"{spacing} Squad: {self.name}\n"
        info += f"{spacing}   Members: {self.get_members_count()} | "
        info += f"Avg Level: {self.get_average_level():.1f} | "
        info += f"Total Damage: {self.get_total_damage()}\n"
        
        for member in self.members:
            info += member.display_info(indent + 1) + "\n"
        
        return info.rstrip()
