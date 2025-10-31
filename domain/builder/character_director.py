
from domain.builder.character_builder import CharacterBuilder
from domain.models.character_base import Character


class CharacterDirector:
    def __init__(self):
        self._builder = CharacterBuilder()
    
    def create_tank_warrior(self, name: str) -> Character:
        return (self._builder
                .set_base_class("warrior")
                .set_name(name)
                .set_level(10)
                .set_health(250)
                .set_strength(30)
                .set_intelligence(5)
                .set_agility(10)
                .build())
    
    def create_glass_cannon_mage(self, name: str) -> Character:
        return (self._builder
                .set_base_class("mage")
                .set_name(name)
                .set_level(10)
                .set_health(60)
                .set_mana(200)
                .set_strength(3)
                .set_intelligence(40)
                .set_agility(5)
                .build())
    
    def create_sniper_archer(self, name: str) -> Character:
        return (self._builder
                .set_base_class("archer")
                .set_name(name)
                .set_level(10)
                .set_health(110)
                .set_strength(15)
                .set_intelligence(12)
                .set_agility(35)
                .build())
    
    def create_assassin_rogue(self, name: str) -> Character:
        return (self._builder
                .set_base_class("rogue")
                .set_name(name)
                .set_level(10)
                .set_health(95)
                .set_strength(20)
                .set_intelligence(10)
                .set_agility(30)
                .build())
