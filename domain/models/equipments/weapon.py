from domain.models.equipments.equipment_base import Equipment, EquipmentType

class Weapon(Equipment):
    def __init__(self, name: str, damage: int, weapon_type: str):
        super().__init__(name, EquipmentType.WEAPON)
        self.damage = damage
        self.weapon_type = weapon_type
    
    def get_description(self) -> str:
        return f"{self.name} ({self.weapon_type}) - Damage: {self.damage}"
