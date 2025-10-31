from domain.factory.equipment_factories.equipment_factory_interface import IEquipmentFactory
from domain.models.equipments.weapon import Weapon
from domain.models.equipments.armor import Armor
from domain.models.equipments.accessory import Accessory
import random

class FireEquipmentFactory(IEquipmentFactory):
    def create_weapon(self) -> Weapon:
        return Weapon("Flamebrand Sword", random.randint(40, 50), "Longsword")
    
    def create_armor(self) -> Armor:
        return Armor("Inferno Plate", random.randint(30, 35), "Heavy Armor")
    
    def create_accessory(self) -> Accessory:
        return Accessory("Phoenix Amulet", "+20% Fire Damage")
