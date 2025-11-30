# Behavioral Design Patterns

## Author: Nicolae Marga, FAF-231

----

## Objectives

- Understand behavioral design patterns and when to use them
- Choose a specific domain (Fantasy RPG System)
- Implement at least 3 behavioral design patterns for the domain

## Used Design Patterns

- Observer Pattern
- Command Pattern
- Strategy Pattern

---

## Implementation

### Domain Context

The behavioral patterns were implemented in a Fantasy RPG combat system. The domain includes characters (Warriors, Mages, Archers), equipment, monsters, a combat system and game-wide events. Behavioral patterns address responsibilities related to communication, action encapsulation and runtime decision-making.

This lab focuses on three patterns that are particularly useful in games:

- Observer: event broadcasting (game events -> UI, logging, achievements)
- Command: encapsulate actions so they can be queued, executed and undone
- Strategy: pluggable AI/behavior selection for monsters

### 1. Observer Pattern

**Purpose:** Decouple event producers (game systems) from consumers (UI, logger, achievements). Observers register with a subject (GameEventManager) and receive notifications when relevant events occur.

Example implementation highlights:

- GameEventManager: register, unregister, notify
- LoggerObserver: prints events (use logging in production)
- AchievementObserver: composite that delegates to specialized observers:
  - KillMilestoneObserver (cumulative kill milestones)
  - BattleObserver (per-battle milestones)
  - LevelObserver (per-character level achievements)

Usage example:

```python
gm = GameEventManager()
gm.register(LoggerObserver())
gm.register(AchievementObserver())
# Emit events
gm.notify('level_up', {'character': hero, 'previous_level': 1})
gm.notify('victory', {'party': party, 'monsters_defeated': 5})
```

Benefits:
- Loose coupling between producers and consumers
- Easy to add new reactions to game events (analytics, UI, achievements)
- Composition-friendly (specialized observers prevent duplicate unlocks)

---

### 2. Command Pattern

**Purpose:** Encapsulate game actions (heal, attack, add-to-party) as objects. Commands can be queued, logged, executed and optionally undone.

Example implementation highlights:

- Command (abstract) with execute() and optional undo()
- HealCommand, AttackCommand, AddToPartyCommand
- CommandInvoker: executes commands and keeps a history to allow undo

Usage example:

```python
invoker = CommandInvoker()
heal = HealCommand(hero, 30)
invoker.execute_command(heal)
# later
invoker.undo_last()
```

Benefits:
- Decouples the caller from action implementation
- Supports undo/redo, batching and history
- Works well with networked or replay systems (serialize commands)

---

### 3. Strategy Pattern

**Purpose:** Encapsulate algorithms for selecting actions (monster AI) and swap them at runtime. Strategies implement a shared interface and the MonsterAI context chooses or auto-selects an appropriate strategy.

Example implementation highlights:

- CombatStrategy (interface)
- AggressiveStrategy: favors special attacks and targets weak enemies
- DefensiveStrategy: favors defending or healing when low on health
- MonsterAI: can be constructed with a strategy or auto-select one using
  simple heuristics (health ratio, party size, relative levels)

Usage example:

```python
ai = MonsterAI(monster)          # will auto-select a strategy
action = ai.decide(party)        # returns {'type': 'basic'|'special'|'defend', 'target': ...}
ai.set_strategy(AggressiveStrategy())
```

Benefits:
- Swap behavior at runtime without conditional code spread across classes
- Keep AI logic testable and configurable
- Auto-selection heuristics let monsters adapt to the current situation

---

## Running the Demo

The workspace includes a demo that demonstrates the behavioral patterns.

The demo runs three sections:
- Observer demo (composite AchievementObserver and modular shared-state observers)
- Command demo (execute and undo commands)
- Strategy demo (auto-selection heuristics and readable actions)

---

## Output / Results

When running the demo you will see console output that demonstrates event notifications, achievement unlocks, command history and AI decisions. Example lines:

```
...
[GameEventManager] level_up -> {'character': <domain.models.characters.mage.Mage object at 0x76991e0a0190>, 'previous_level': 2}
[Achievement] Unlocked: Golden Mage reached level 5 (Seasoned)
[GameEventManager] victory -> {'party': [<domain.models.characters.warrior.Warrior object at 0x76991e0a0160>, <domain.models.characters.mage.Mage object at 0x76991e0a0190>], 'monsters_defeated': 30}
[Achievement] Unlocked: First Blood: defeated your first monster
[Achievement] Unlocked: Monster Hunter: defeated 20 monsters total
[Achievement] Unlocked: Massacre: defeated 5 monsters in one battle

Composite achievements:
 Dark Knight achieved their first level up
Golden Mage achieved their first level up
Golden Mage reached level 5 (Seasoned)
First Blood: defeated your first monster
Monster Hunter: defeated 20 monsters total
Dark Knight, Golden Mage defeated 30 monsters
Massacre: defeated 5 monsters in one battle
Total monsters defeated (composite): 30

...

Command Pattern - Actions & Undo
[MageFactory] Creating a powerful mage named 'Caster'
Create level 5 monster
Damage the mage
Before heal: 66/80
After heal: 76/80
============================================================
Command logs:
Grax attacked Caster for 14 damage.
Caster was healed for 10 health.

============================================================
Caster health after 1 undo : 66/80
Caster health after one more undo: 80/80

...

Strategy Pattern - Monster AI (auto-selection demo)
[ArcherFactory] Creating a skilled archer named 'Legolas'
[WarriorFactory] Creating a mighty warrior named 'Aragorn'
Auto-selected strategy: DefensiveStrategy
Decided action: type=basic, target=Legolas (HP: 100/100)

Low-health strategy: DefensiveStrategy
Decided action: type=defend, target=None

High-level strategy: AggressiveStrategy
Decided action: type=basic, target=Legolas (HP: 100/100)

[MageFactory] Creating a powerful mage named 'Gandalf'
[RogueFactory] Creating a stealthy rogue named 'Bilbo'
Large-party strategy: AggressiveStrategy
Decided action: type=special, target=Gandalf (HP: 80/80)
```

---

## Conclusions / Results

Behavioral patterns implemented in this laboratory work show how to structure runtime behavior, communication and action in a game. Observers provide event handling for logging and achievements. Commands help to encapsulate game operations and also help with undo functionalities. Strategies provide better AI behaviors for monsters. These patterns help decouple the system in a way that allows flexible choices for UI and UX. Also it helps with maintainability and testability.
