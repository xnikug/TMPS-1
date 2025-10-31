from abc import ABC, abstractmethod
from domain.models.monsters import Monster
import random


class IMonsterFactory(ABC):
    @abstractmethod
    def create_monster(self, name: str, level: int = 1) -> Monster:
        pass
    
    def create_with_random_name(self, level: int = 1) -> Monster:
        names = self.get_random_names()
        name = random.choice(names)
        return self.create_monster(name, level)
    
    @abstractmethod
    def get_random_names(self) -> list:
        pass