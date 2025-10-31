from abc import ABC, abstractmethod
from domain.models.character_base import Character


class ICharacterFactory(ABC):
    
    @abstractmethod
    def create_character(self, name: str) -> Character:
        pass
    
    def create_with_defaults(self) -> Character:
        return self.create_character(f"Default{self.__class__.__name__.replace('Factory', '')}")
