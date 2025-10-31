from domain.factory.equipment_factories.equipment_factory_interface import IEquipmentFactory
from domain.models.equipments.weapon import Weapon
from domain.models.equipments.armor import Armor
from domain.models.equipments.accessory import Accessory
import random

class IceEquipmentFactory(IEquipmentFactory):
    def create_weapon(self) -> Weapon:
        return Weapon("Frostbite Bow", random.randint(35, 45), "Longbow")
    
    def create_armor(self) -> Armor:
        return Armor("Glacial Robes", random.randint(20, 25), "Light Armor")
    
    def create_accessory(self) -> Accessory:
        return Accessory("Frozen Heart Ring", "+15% Ice Damage, +10 Mana")
