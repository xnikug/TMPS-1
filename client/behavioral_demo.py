from domain.behavioral.observer import GameEventManager, LoggerObserver, AchievementObserver
from domain.behavioral.command import CommandInvoker, HealCommand, AddToPartyCommand, AttackCommand
from domain.behavioral.strategy import MonsterAI, AggressiveStrategy, DefensiveStrategy
from domain.factory.character_factories.character_creator import CharacterCreator
from domain.models.character_class import CharacterClass
from domain.factory.monster_factories import MonsterCreator
from domain.models.monsters import MonsterType
from domain.behavioral.observers import (
        GameEventManager,
        LoggerObserver,
        AchievementObserver,
        KillMilestoneObserver,
        BattleObserver,
        LevelObserver,
)

def prompt_continue():
    input("\n[Press Enter to continue]")

def demo_observer():
    print("Observer Pattern - Game Events")

    gm = GameEventManager()
    logger = LoggerObserver()
    composite = AchievementObserver()

    gm.register(logger)
    gm.register(composite)

    # Create a small party and simulate events that trigger many achievements
    party = [
        CharacterCreator.create_character(CharacterClass.WARRIOR, "Dark Knight"),
        CharacterCreator.create_character(CharacterClass.MAGE, "Golden Mage"),
    ]

    gm.notify('spawn', {'party': [p.name for p in party]})

    # Level-up notifications (composite will delegate to LevelObserver)
    party[0].level_up()
    gm.notify('level_up', {'character': party[0], 'previous_level': 1})
    party[1].level_up()
    gm.notify('level_up', {'character': party[1], 'previous_level': 1})

    for _ in range(5):
        party[1].level_up()
    gm.notify('level_up', {'character': party[1], 'previous_level': 2})

    # A big victory to exercise KillMilestoneObserver and BattleObserver
    gm.notify('victory', {'party': party, 'monsters_defeated': 30})

    print("\nComposite achievements:\n", '\n'.join(composite.achievements))
    print(f"Total monsters defeated (composite): {composite.total_monsters_defeated}\n")

    # Unregister
    gm.unregister(composite)

    return gm, composite


def demo_command():
    print("Command Pattern - Actions & Undo")
    invoker = CommandInvoker()

    # Heal + Attack command demo (attacker is monster, target is a hero)
    hero = CharacterCreator.create_character(CharacterClass.MAGE, "Caster")
    print("Create level 5 monster")
    monster = MonsterCreator.create_monster(MonsterType.GOBLIN, "Grax", level=5)
    print("Damage the mage")
    damage_cmd = AttackCommand(monster, hero)
    invoker.execute_command(damage_cmd)
    print(f"Before heal: {hero.health}/{hero.max_health}")

    heal_cmd = HealCommand(hero, 10)
    invoker.execute_command(heal_cmd)
    print(f"After heal: {hero.health}/{hero.max_health}")

    print(f"\n{'='*60}")
    print(f"Command logs:")
    invoker.show_command_history()
    print(f"\n{'='*60}")

    # Undo heal
    invoker.undo_last()
    print(f"Caster health after 1 undo : {hero.health}/{hero.max_health}")
    invoker.undo_last()
    print(f"Caster health after one more undo: {hero.health}/{hero.max_health}")
    # Add to party using singleton via command
    add_cmd = AddToPartyCommand(hero)
    invoker.execute_command(add_cmd)
    # Undo add
    invoker.undo_last()

    # Attack command demo (attacker is hero, target is a monster)
    monster = MonsterCreator.create_monster(MonsterType.UNDEAD, "Thrax", level=1)
    atk_cmd = AttackCommand(hero, monster)
    invoker.execute_command(atk_cmd)
    print(f"Monster HP after attack: {monster.health}/{monster.max_health}")

    return invoker

def _format_action(act):
    if not isinstance(act, dict):
        return str(act)
    tgt = act.get('target')
    tdesc = None
    if tgt is not None:
        name = getattr(tgt, 'name', None) or getattr(tgt, '__class__', type(tgt)).__name__
        hp = getattr(tgt, 'health', None)
        mhp = getattr(tgt, 'max_health', None)
        if hp is not None and mhp is not None:
            tdesc = f"{name} (HP: {hp}/{mhp})"
        else:
            tdesc = f"{name}"
    return f"type={act.get('type')}, target={tdesc}"

def demo_strategy():
    print("Strategy Pattern - Monster AI (auto-selection demo)")

    # Create base party and monster
    party = [
        CharacterCreator.create_character(CharacterClass.ARCHER, "Legolas"),
        CharacterCreator.create_character(CharacterClass.WARRIOR, "Aragorn"),
    ]

    monster = MonsterCreator.create_monster(MonsterType.DEMON, "Bael", level=2)

    # default auto-selection
    ai = MonsterAI(monster)  # no explicit strategy -> will auto-select
    action = ai.decide(party)
    print(f"Auto-selected strategy: {ai.current_strategy_name}")
    print(f"Decided action: {_format_action(action)}\n")

    # monster low health -> should prefer Defensive
    monster.health = 1
    ai = MonsterAI(monster)  # re-create to reset strategy
    action = ai.decide(party)
    print(f"Low-health strategy: {ai.current_strategy_name}")
    print(f"Decided action: {_format_action(action)}\n")

    # monster higher level than party -> aggressive ambusher
    monster.health = monster.max_health
    monster.level = max(getattr(p, 'level', 1) for p in party) + 3
    ai = MonsterAI(monster)
    action = ai.decide(party)
    print(f"High-level strategy: {ai.current_strategy_name}")
    print(f"Decided action: {_format_action(action)}\n")

    # large party -> aggressive due to party size
    big_party = party + [CharacterCreator.create_character(CharacterClass.MAGE, "Gandalf"),
                         CharacterCreator.create_character(CharacterClass.ROGUE, "Bilbo")]
    monster.level = 2
    monster.health = monster.max_health
    ai = MonsterAI(monster)
    action = ai.decide(big_party)
    print(f"Large-party strategy: {ai.current_strategy_name}")
    print(f"Decided action: {_format_action(action)}\n")

    return ai


def main():
    demo_observer()
    prompt_continue()
    demo_command()
    prompt_continue()
    demo_strategy()
    print("\nProgram completed execution!")

if __name__ == '__main__':
    main()
