from abc import ABC, abstractmethod
from enum import Enum

class EquipmentType(Enum):
    WEAPON = "Weapon"
    ARMOR = "Armor"
    ACCESSORY = "Accessory"

class Equipment(ABC):
    def __init__(self, name: str, equipment_type: EquipmentType):
        self.name = name
        self.equipment_type = equipment_type
    
    @abstractmethod
    def get_description(self) -> str:
        pass
