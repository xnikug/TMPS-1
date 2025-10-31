from abc import ABC, abstractmethod
from domain.models.equipments.weapon import Weapon
from domain.models.equipments.armor import Armor
from domain.models.equipments.accessory import Accessory

class IEquipmentFactory(ABC):
    @abstractmethod
    def create_weapon(self) -> Weapon:
        pass
    
    @abstractmethod
    def create_armor(self) -> Armor:
        pass
    
    @abstractmethod
    def create_accessory(self) -> Accessory:
        pass
    
    def create_full_set(self) -> dict:
        return {
            'weapon': self.create_weapon(),
            'armor': self.create_armor(),
            'accessory': self.create_accessory()
        }
