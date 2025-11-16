from domain.factory.character_factories.character_creator import CharacterCreator
from domain.models.character_class import CharacterClass
from domain.structural.decorators import (
    SpellBuffDecorator,
    ShieldEnchantmentDecorator,
    StrengthPotionDecorator
)
from domain.structural.facades import CombatFacade
from domain.structural.proxies import CharacterProxy
from domain.structural.composites import Squad, CharacterComponent
from domain.factory.monster_factories import MonsterCreator


def header(title: str):
    print(f"\n{'='*60}\n  {title}\n{'='*60}")


def prompt_continue():
    input("\n[Press Enter to continue]")


def demo_decorator():
    header("1. DECORATOR PATTERN")
    
    print("Creating Warrior: Thorin")
    warrior = CharacterCreator.create_character(CharacterClass.WARRIOR, "Thorin")
    print(f"  Base Strength: {warrior.strength}")
    print(f"  Base Attack: {warrior.basic_attack()}\n")
    
    prompt_continue()
    
    print("Adding Strength Potion (+8 STR)")
    enhanced = StrengthPotionDecorator(warrior, strength_bonus=8)
    print(f"  New Strength: {enhanced.strength}")
    print(f"  New Attack: {enhanced.basic_attack()}\n")
    
    prompt_continue()
    
    print("Adding Shield Enchantment (20% damage reduction)")
    super_enhanced = ShieldEnchantmentDecorator(enhanced, damage_reduction=0.20)
    print(f"  Damage taken (50 hit): {int(50 * 0.80)}\n")
    
    prompt_continue()
    
    print("Creating Mage: Gandalf")
    mage = CharacterCreator.create_character(CharacterClass.MAGE, "Gandalf")
    print(f"  Base Intelligence: {mage.intelligence}")
    print(f"  Base Mana: {mage.mana}\n")
    
    prompt_continue()
    
    print("Adding Spell Buff (+5 INT, +30 Mana)")
    buffed_mage = SpellBuffDecorator(mage, intelligence_bonus=5, mana_bonus=30)
    print(f"  New Intelligence: {buffed_mage.intelligence}")
    print(f"  New Mana: {buffed_mage.mana}\n")
    
    return [super_enhanced, buffed_mage]


def demo_facade(party):
    header("2. FACADE PATTERN")
    
    print("Executing quick_battle(party, 2)...\n")
    facade = CombatFacade()
    result = facade.quick_battle(party, 2)
    
    prompt_continue()
    
    print("Battle Result:")
    print(f"  Victory: {'YES' if result['victory'] else 'NO'}")
    print(f"  Monsters Defeated: {result['monsters_defeated']}")
    print(f"  Erxperience Earned: {result['experience_earned']}")
    print(f"  Gold Earned: {result['gold_earned']}\n")
    
    prompt_continue()
    
    print("Battle Log:")
    print(facade.get_battle_log())
    
    return facade


def demo_proxy():
    header("3. PROXY PATTERN")
    
    print("Creating Archer via Proxy")
    proxy = CharacterProxy(
        lambda name: CharacterCreator.create_character(CharacterClass.ARCHER, name),
        "Legolas"
    )
    print("  [OK] Proxy created (character not loaded yet)\n")
    
    prompt_continue()
    
    print("First access: proxy.name")
    name = proxy.name
    print(f"  [OK] Character loaded! Name: {name}\n")
    
    prompt_continue()
    
    print("Accessing proxy attributes:")
    strength = proxy.strength
    print(f"  Strength: {strength}")
    agility = proxy.agility
    print(f"  Agility: {agility}\n")
    
    prompt_continue()
    
    print("Executing: proxy.basic_attack()")
    damage = proxy.basic_attack()
    print(f"  Damage: {damage}\n")
    
    prompt_continue()
    
    print("Access Log:")
    print(f"  Total Accesses: {proxy.get_access_count()}")
    print(proxy.get_access_log())
    
    return proxy


def demo_composite():
    header("4. COMPOSITE PATTERN")
    
    print("Creating characters:")
    warrior1 = CharacterCreator.create_character(CharacterClass.WARRIOR, "Aragorn")
    print(f"  [OK] {warrior1.name} (Warrior)")
    
    warrior2 = CharacterCreator.create_character(CharacterClass.WARRIOR, "Gimli")
    print(f"  [OK] {warrior2.name} (Warrior)")
    
    archer = CharacterCreator.create_character(CharacterClass.ARCHER, "Legolas")
    print(f"  [OK] {archer.name} (Archer)")
    
    mage = CharacterCreator.create_character(CharacterClass.MAGE, "Gandalf")
    print(f"  [OK] {mage.name} (Mage)\n")
    
    prompt_continue()
    
    print("Building squad hierarchy:")
    comp_warrior1 = CharacterComponent(warrior1)
    comp_warrior2 = CharacterComponent(warrior2)
    comp_archer = CharacterComponent(archer)
    comp_mage = CharacterComponent(mage)
    
    melee_squad = Squad("Melee Squad")
    melee_squad.add_member(comp_warrior1)
    melee_squad.add_member(comp_warrior2)
    print(f"  [OK] {melee_squad.name} (2 warriors)")
    
    ranged_squad = Squad("Ranged Squad")
    ranged_squad.add_member(comp_archer)
    ranged_squad.add_member(comp_mage)
    print(f"  [OK] {ranged_squad.name} (archer + mage)")
    
    main_squad = Squad("The Fellowship")
    main_squad.add_member(melee_squad)
    main_squad.add_member(ranged_squad)
    print(f"  [OK] {main_squad.name} created\n")
    
    prompt_continue()
    
    print("Hierarchical Structure:")
    print(main_squad.display_info())
    
    prompt_continue()
    
    print("Squad Statistics:")
    print(f"  Total Members: {main_squad.get_members_count()}")
    print(f"  Average Level: {main_squad.get_average_level():.1f}")
    print(f"  Combined Damage: {main_squad.get_total_damage()}")
    print(f"  Combined Health: {main_squad.get_total_health()}\n")
    
    prompt_continue()
    
    print("Melee Squad Stats:")
    print(f"  Members: {melee_squad.get_members_count()}")
    print(f"  Total Damage: {melee_squad.get_total_damage()}\n")
    
    print("Ranged Squad Stats:")
    print(f"  Members: {ranged_squad.get_members_count()}")
    print(f"  Total Damage: {ranged_squad.get_total_damage()}\n")
    
    prompt_continue()
    
    print("Adding new warrior to Melee Squad:")
    new_warrior = CharacterCreator.create_character(CharacterClass.WARRIOR, "Boromir")
    melee_squad.add_member(CharacterComponent(new_warrior))
    print(f"  [OK] {new_warrior.name} added")
    print(f"  Melee Squad Members: {melee_squad.get_members_count()}")
    print(f"  Fellowship Members: {main_squad.get_members_count()}\n")
    
    return main_squad


def main():
    print("""
  Structural Design Patterns - Demo

  1. Decorator   - Stack enhancements dynamically
  2. Facade      - Simplify complex operations
  3. Proxy       - Lazy-load with access tracking
  4. Composite   - Hierarchical squad organization

  Press Enter to navigate through each pattern
    """)
    
    prompt_continue()
    
    party = demo_decorator()
    prompt_continue()
    
    facade = demo_facade(party)
    prompt_continue()
    
    proxy = demo_proxy()
    prompt_continue()
    
    squad = demo_composite()    

if __name__ == "__main__":
    main()
