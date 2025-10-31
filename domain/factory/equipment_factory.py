"""
Abstract Factory Pattern for creating themed equipment sets.
Each factory creates a family of related equipment (weapon + armor + accessory).
"""
from abc import ABC, abstractmethod
from domain.models.equipments import Weapon, Armor, Accessory
from domain.factory.equipment_factories import (
    FireEquipmentFactory, 
    IceEquipmentFactory, 
    ShadowEquipmentFactory, 
    HolyEquipmentFactory
)

__all__ = ['FireEquipmentFactory', 'IceEquipmentFactory', 'ShadowEquipmentFactory', 'HolyEquipmentFactory']


class EquipmentFactory(ABC):
    """Abstract factory for creating themed equipment sets"""
    
    @abstractmethod
    def create_weapon(self) -> Weapon:
        """Create a weapon for this theme"""
        pass
    
    @abstractmethod
    def create_armor(self) -> Armor:
        """Create armor for this theme"""
        pass
    
    @abstractmethod
    def create_accessory(self) -> Accessory:
        """Create an accessory for this theme"""
        pass
    
    def create_full_set(self) -> dict:
        """Create a complete equipment set"""
        return {
            'weapon': self.create_weapon(),
            'armor': self.create_armor(),
            'accessory': self.create_accessory()
        }
