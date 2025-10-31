from domain.factory.equipment_factories.equipment_factory_interface import IEquipmentFactory
from domain.models.equipments.weapon import Weapon
from domain.models.equipments.armor import Armor
from domain.models.equipments.accessory import Accessory
import random

class ShadowEquipmentFactory(IEquipmentFactory):
    def create_weapon(self) -> Weapon:
        return Weapon("Shadowfang Dagger", random.randint(30, 40), "Dagger")
    
    def create_armor(self) -> Armor:
        return Armor("Nightstalker Leather", random.randint(25, 30), "Medium Armor")
    
    def create_accessory(self) -> Accessory:
        return Accessory("Cloak of Shadows", "+25% Stealth, +10% Critical")
