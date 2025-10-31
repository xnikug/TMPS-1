from domain.models.equipments.equipment_base import Equipment, EquipmentType

class Armor(Equipment):
    def __init__(self, name: str, defense: int, armor_type: str):
        super().__init__(name, EquipmentType.ARMOR)
        self.defense = defense
        self.armor_type = armor_type
    
    def get_description(self) -> str:
        return f"{self.name} ({self.armor_type}) - Defense: {self.defense}"
