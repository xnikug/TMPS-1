from domain.models.character_class import CharacterClass
from domain.factory.character_factories.character_creator import CharacterCreator
from domain.factory.equipment_factory import (
    FireEquipmentFactory, IceEquipmentFactory, 
    ShadowEquipmentFactory, HolyEquipmentFactory
)
from domain.builder.character_builder import CharacterBuilder
from domain.builder.character_director import CharacterDirector
from domain.singleton.game_manager import GameManager
from domain.factory.combat_system import CombatSystem
from domain.factory.monster_factories import MonsterCreator
from domain.models.monsters import MonsterType


def print_section(title: str):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def demonstrate_factory_method():
    print_section("Factory Pattern - Character Creation")
    
    warrior = CharacterCreator.create_character(CharacterClass.WARRIOR, "Thorin")
    mage = CharacterCreator.create_character(CharacterClass.MAGE, "Gandalf")
    archer = CharacterCreator.create_character(CharacterClass.ARCHER, "Legolas")
    rogue = CharacterCreator.create_character(CharacterClass.ROGUE, "Assassin")
    
    characters = [warrior, mage, archer, rogue]
    for char in characters:
        print(f"\n{char}")
        print(f"Special: {char.special_ability()}")
    
    return characters


def demonstrate_monster_factory():
    print_section("Monster Creation")
    
    print("--- Creating specific monsters ---")
    goblin = MonsterCreator.create_monster(MonsterType.GOBLIN, "Grax the Nasty", 2)
    undead = MonsterCreator.create_monster(MonsterType.UNDEAD, "Bone Lord", 3)
    beast = MonsterCreator.create_monster(MonsterType.BEAST, "Shadow Wolf", 2)
    demon = MonsterCreator.create_monster(MonsterType.DEMON, "Bael", 4)
    
    monsters = [goblin, undead, beast, demon]
    for monster in monsters:
        print(f"\n{monster}")
        special = monster.special_attack()
        print(f"Special: {special['description']}")
    
    print("\n--- Creating random monster wave ---")
    random_monsters = MonsterCreator.create_monster_wave(3, 2)
    for monster in random_monsters:
        print(f"• {monster.name} - {monster.__class__.__name__} (Level {monster.level})")
    
    return monsters


def demonstrate_abstract_factory():
    print_section("Abstract Factory Pattern - Equipment Sets")
    
    factories = {
        "Fire": FireEquipmentFactory(),
        "Ice": IceEquipmentFactory(),
        "Shadow": ShadowEquipmentFactory(),
        "Holy": HolyEquipmentFactory()
    }
    
    equipment_sets = {}
    for theme, factory in factories.items():
        print(f"\n--- {theme} Equipment Set ---")
        equipment_set = factory.create_full_set()
        equipment_sets[theme] = equipment_set
        
        print(f"Weapon: {equipment_set['weapon'].get_description()}")
        print(f"Armor: {equipment_set['armor'].get_description()}")
        print(f"Accessory: {equipment_set['accessory'].get_description()}")
    
    return equipment_sets


def demonstrate_builder_pattern():
    print_section("Builder Pattern - Custom Character Creation")
    
    print("--- Manual Builder Usage ---")
    builder = CharacterBuilder()
    custom_hero = (builder
                   .set_base_class("warrior")
                   .set_name("Custom Hero")
                   .set_level(15)
                   .set_health(300)
                   .set_strength(35)
                   .set_intelligence(8)
                   .set_agility(12)
                   .build())
    
    print(f"\n{custom_hero}")
    
    print("\n--- Director Pattern (Predefined Builds) ---")
    director = CharacterDirector()
    
    tank = director.create_tank_warrior("Iron Wall")
    glass_cannon = director.create_glass_cannon_mage("Archmage Pyrion")
    sniper = director.create_sniper_archer("Hawkeye")
    assassin = director.create_assassin_rogue("Shadow Blade")
    
    preset_chars = [tank, glass_cannon, sniper, assassin]
    for char in preset_chars:
        print(f"\n{char}")
    
    return [custom_hero] + preset_chars


def demonstrate_singleton_pattern():
    print_section("Singleton pattern - Game Manager")
    
    game_manager1 = GameManager()
    print(game_manager1.get_game_info())
    
    print("\n--- Attempting to create another GameManager instance ---")
    game_manager2 = GameManager()
    
    print(f"\nAre both instances the same? {game_manager1 is game_manager2}")
    print(f"Instance 1 ID: {id(game_manager1)}")
    print(f"Instance 2 ID: {id(game_manager2)}")
    
    return game_manager1


def equip_characters(characters, equipment_sets):
    print_section("EQUIPPING CHARACTERS")
    
    themes = ["Fire", "Ice", "Shadow", "Holy"]
    
    for i, char in enumerate(characters[:4]):
        theme = themes[i % len(themes)]
        equipment = equipment_sets[theme]
        
        char.weapon = equipment['weapon']
        char.armor = equipment['armor']
        char.accessories.append(equipment['accessory'])
        
        print(f"\n{char.name} equipped with {theme} set!")
        print(f"  {equipment['weapon'].get_description()}")
        print(f"  {equipment['armor'].get_description()}")
        print(f"  {equipment['accessory'].get_description()}")


def demonstrate_combat_system(party):
    print_section("COMBAT SYSTEM - Monster Battles & Leveling")
    
    print("Welcome to the Arena!")
    
    # Show initial party status
    print(f"\nYour Party:")
    for char in party:
        print(f"   • {char.name} (Level {char.level}) - {char.get_health_bar()}")
    
    input("\nPress Enter to start the adventure...")
    print(party)
    # Start a 3-round adventure

    combat_system = CombatSystem(party)
    combat_system.start_adventure(15)
    


def main():
    print("""
    ============================================
                    Fantasy Quest
    ============================================
    """)
    
    # Initialize game manager
    game_manager = demonstrate_singleton_pattern()
    game_manager.set_difficulty("Normal")
    
    # Create characters using factory pattern
    factory_characters = demonstrate_factory_method()
    
    # Demonstrate monster creation
    demonstrate_monster_factory()
    
    # Create equipment sets
    equipment_sets = demonstrate_abstract_factory()
    
    # Create custom characters using builder
    builder_characters = demonstrate_builder_pattern()
    
    # Combine all characters
    all_characters = factory_characters + builder_characters
    
    # Equip the first 4 characters
    equip_characters(all_characters, equipment_sets)
    
    # Add equipped characters to game manager
    print_section("PARTY MANAGEMENT (Singleton)")
    for char in all_characters[:4]:
        game_manager.add_to_party(char)
    
    print(game_manager.get_party_info())
    
    # Get the active party for combat
    active_party = all_characters[:4]
    
    # Demonstrate combat system
    demonstrate_combat_system(active_party)
    
    print_section("FINAL SUMMARY")
    print(game_manager.get_game_info())
    print(game_manager.get_party_info())
    
    print(f"\nFinal Party Status:")
    for char in active_party:
        print(f"\n{char}")


if __name__ == "__main__":
    main()
