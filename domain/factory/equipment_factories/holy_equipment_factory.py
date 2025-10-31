from domain.factory.equipment_factories.equipment_factory_interface import IEquipmentFactory
from domain.models.equipments.weapon import Weapon
from domain.models.equipments.armor import Armor
from domain.models.equipments.accessory import Accessory
import random

class HolyEquipmentFactory(IEquipmentFactory):
    def create_weapon(self) -> Weapon:
        return Weapon("Divine Mace", random.randint(40, 45), "Mace")
    
    def create_armor(self) -> Armor:
        return Armor("Blessed Chainmail", random.randint(30, 35), "Medium Armor")
    
    def create_accessory(self) -> Accessory:
        return Accessory("Halo of Light", "+15% Healing, +5% Defense")
