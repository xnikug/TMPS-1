from domain.models.equipments.equipment_base import Equipment, EquipmentType

class Accessory(Equipment):
    def __init__(self, name: str, bonus: str):
        super().__init__(name, EquipmentType.ACCESSORY)
        self.bonus = bonus
    
    def get_description(self) -> str:
        return f"{self.name} - Bonus: {self.bonus}"
