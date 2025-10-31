# Creational Design Patterns

## Author: Nicolae Marga, FAF-231

----

## Objectives:

* Get familiar with the Creational DPs;
* Choose a specific domain;
* Implement at least 3 CDPs for the specific domain;


## Used Design Patterns: 

* **Factory Method Pattern**
* **Abstract Factory Pattern**
* **Builder Pattern**
* **Singleton Pattern**


## Implementation

### Overview

This project implements a fantasy RPG character, monster, and equipment management system with a combat adventure feature using five creational design patterns. The domain focuses on creating different character classes (Warrior, Mage, Archer, Rogue), monster types (Goblin, Undead, Beast, Demon), and themed equipment sets (Fire, Ice, Shadow, Holy). The implementation demonstrates how creational patterns solve object instantiation challenges in a game context, extended with a combat system for dynamic gameplay.

### 1. Factory Method Pattern

The Factory Method pattern is used to create different character types and monster types through dedicated factory classes. Each factory (WarriorFactory, MageFactory, ArcherFactory, RogueFactory for characters; GoblinFactory, UndeadFactory, BeastFactory, DemonFactory for monsters) implements the respective interface and knows how to instantiate its specific class with appropriate base stats.

**Character Factory Interface:**
```python
class ICharacterFactory(ABC):
    @abstractmethod
    def create_character(self, name: str) -> Character:
        pass
    
    def create_with_defaults(self) -> Character:
        return self.create_character(f"Default{self.__class__.__name__.replace('Factory', '')}")
```

**Concrete Factory Example (Warrior):**
```python
class WarriorFactory(ICharacterFactory):
    def create_character(self, name: str) -> Character:
        print(f"[WarriorFactory] Creating a mighty warrior named '{name}'")
        return Warrior(name)
```

**Monster Factory Interface:**
```python
class IMonsterFactory(ABC):
    @abstractmethod
    def create_monster(self, name: str, level: int) -> Monster:
        pass
```

**Concrete Factory Example (Goblin):**
```python
class GoblinFactory(IMonsterFactory):
    def create_monster(self, name: str, level: int) -> Monster:
        print(f"[GoblinFactory] Creating a goblin named '{name}' at level {level}")
        return Goblin(name, level)
```

**Usage:**
```python
warrior = CharacterCreator.create_character(CharacterClass.WARRIOR, "Thorin")
goblin = MonsterCreator.create_monster(MonsterType.GOBLIN, "Grax", 2)
```

### 2. Abstract Factory Pattern

The Abstract Factory pattern creates families of related equipment objects (weapon, armor, accessory) that share a common theme. Each factory (FireEquipmentFactory, IceEquipmentFactory, etc.) produces a complete equipment set with matching aesthetics and bonuses.

**Equipment Factory Interface:**
```python
class IEquipmentFactory(ABC):
    @abstractmethod
    def create_weapon(self) -> Weapon:
        pass
    
    @abstractmethod
    def create_armor(self) -> Armor:
        pass
    
    @abstractmethod
    def create_accessory(self) -> Accessory:
        pass
    
    def create_full_set(self) -> dict:
        return {
            'weapon': self.create_weapon(),
            'armor': self.create_armor(),
            'accessory': self.create_accessory()
        }
```

**Concrete Factory Example (Fire Theme):**
```python
class FireEquipmentFactory(IEquipmentFactory):
    def create_weapon(self) -> Weapon:
        return Weapon("Flamebrand Sword", 42, "Longsword")
    
    def create_armor(self) -> Armor:
        return Armor("Inferno Plate", 35, "Heavy Armor")
    
    def create_accessory(self) -> Accessory:
        return Accessory("Phoenix Amulet", "+20% Fire Damage")
```

**Usage:**
```python
fire_factory = FireEquipmentFactory()
equipment_set = fire_factory.create_full_set()
```

### 3. Builder Pattern

The Builder pattern provides a flexible way to construct complex character objects step-by-step. It includes a CharacterBuilder class with a fluent interface and a CharacterDirector that encapsulates preset character configurations.

**Builder Implementation:**
```python
class CharacterBuilder:
    def __init__(self):
        self._character = None
        self._name = "Unknown Hero"
        self._base_class = "warrior"
    
    def set_base_class(self, class_type: str):
        self._base_class = class_type.lower()
        return self
    
    def set_name(self, name: str):
        self._name = name
        return self
    
    def set_level(self, level: int):
        if not self._character:
            self._create_base_character()
        self._character.level = level
        return self
    
    def build(self) -> Character:
        if not self._character:
            self._create_base_character()
        result = self._character
        self.reset()
        return result
```

**Director for Preset Builds:**
```python
class CharacterDirector:
    def create_tank_warrior(self, name: str) -> Character:
        return (self._builder
                .set_base_class("warrior")
                .set_name(name)
                .set_level(10)
                .set_health(250)
                .set_strength(30)
                .build())
```

**Usage:**
```python
# Manual building
builder = CharacterBuilder()
hero = (builder
        .set_base_class("warrior")
        .set_name("Custom Hero")
        .set_level(15)
        .set_health(300)
        .set_strength(35)
        .set_intelligence(8)
        .set_agility(12)
        .build())

# Using director
director = CharacterDirector()
tank = director.create_tank_warrior("Iron Wall")
```

### 4. Singleton Pattern

The Singleton pattern ensures only one GameManager instance exists throughout the application, managing global game state, party members, and configuration settings.

**Singleton Implementation:**
```python
class GameManager:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            print("[GameManager] Creating new GameManager instance (Singleton)")
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not GameManager._initialized:
            self.game_name = "Fantasy Quest"
            self.version = "1.0.0"
            self.difficulty = "Normal"
            self.max_party_size = 4
            self.current_party = []
            GameManager._initialized = True
```

**Usage:**
```python
game_manager1 = GameManager()  # Creates instance
game_manager2 = GameManager()  # Returns same instance
print(game_manager1 is game_manager2)  # True
```

### 5. Combat System

The Combat System integrates the created characters, monsters, and equipment into dynamic turn-based battles. It manages adventures with increasing difficulty, experience gain, leveling up, and party management.

**Combat System Overview:**
```python
class CombatSystem:
    def __init__(self, party: List[Character]):
        self.party = party
        # ... initialization
    
    def start_adventure(self, max_rounds: int = 5):
        # Manages rounds of combat with monster waves
        # Handles experience distribution and leveling
```

**Usage:**
```python
combat_system = CombatSystem(party)
combat_system.start_adventure(15)  # 15-round adventure
```



## Conclusions

### Key Achievements

1. **Separation of Concerns**: Each class is in its own file, making the codebase modular and maintainable.

2. **Pattern Integration**: Successfully integrated four creational patterns that work together cohesively in a fantasy game context, extended with a combat system.

3. **Extensibility**: Adding new character types, monster types, or equipment themes requires minimal code changes due to the factory patterns.

4. **Flexibility**: The Builder pattern provides fine-grained control over character creation while maintaining clean code.

5. **Global State Management**: The Singleton pattern ensures consistent game state across the application.

6. **Dynamic Gameplay**: The Combat System enables engaging adventures with leveling and progression.

### Running the Project

```bash
cd /home/user1/TMPS-1
PYTHONPATH=/home/user1/TMPS-1:$PYTHONPATH python3 client/main.py
```

### Output Example

```
===========================================
                    Fantasy Quest
===========================================

============================================================
  Singleton pattern - Game Manager
============================================================

[GameManager] Creating new GameManager instance (Singleton)
[GameManager] Initialized: Fantasy Quest

==================================================
  Fantasy Quest
  Difficulty: Normal
  Party Size: 0/4
==================================================

============================================================
  Factory Pattern - Character Creation
============================================================

[WarriorFactory] Creating a mighty warrior named 'Thorin'
[MageFactory] Creating a powerful mage named 'Gandalf'
[ArcherFactory] Creating a skilled archer named 'Legolas'
[RogueFactory] Creating a stealthy rogue named 'Assassin'

Warrior 'Thorin' (Level 1)
  HP: [██████████] 150/150
  Mana: 50 | EXP: 0/100
  STR: 20 | INT: 5 | AGI: 8
Special: Thorin uses SHIELD BASH! Stuns enemy and deals massive damage!

============================================================
  Monster Creation
============================================================

--- Creating specific monsters ---
Goblin 'Grax the Nasty' (Level 2)
Special: Grax the Nasty performs a DIRTY STRIKE!

--- Creating random monster wave ---
• Storm Eagle - Beast (Level 2)
• Zak - Goblin (Level 2)
• Iron Bear - Beast (Level 2)

============================================================
  Abstract Factory Pattern - Equipment Sets
============================================================

--- Fire Equipment Set ---
Weapon: Flamebrand Sword (Longsword) - Damage: 42
Armor: Inferno Plate (Heavy Armor) - Defense: 35
Accessory: Phoenix Amulet - Bonus: +20% Fire Damage

============================================================
  Builder Pattern - Custom Character Creation
============================================================

Warrior 'Custom Hero' (Level 15)
  HP: [████████████████████] 300/150
  STR: 35 | INT: 8 | AGI: 12

Warrior 'Iron Wall' (Level 10)
  HP: [████████████████] 250/150
  STR: 30 | INT: 5 | AGI: 10

============================================================
  EQUIPPING CHARACTERS
============================================================

Thorin equipped with Fire set!
  Flamebrand Sword (Longsword) - Damage: 42
  Inferno Plate (Heavy Armor) - Defense: 35
  Phoenix Amulet - Bonus: +20% Fire Damage

============================================================
  PARTY MANAGEMENT (Singleton)
============================================================

[GameManager] Added Thorin to the party

=== Current Party (4/4) ===
1. Thorin - Warrior (Level 1)
2. Gandalf - Mage (Level 1)
3. Legolas - Archer (Level 1)
4. Assassin - Rogue (Level 1)

============================================================
  COMBAT SYSTEM - Monster Battles & Leveling
============================================================

Welcome to the Arena!
Your Party:
   • Thorin (Level 1) - [██████████] 150/150
   • Gandalf (Level 1) - [██████████] 80/80
   • Legolas (Level 1) - [██████████] 100/100
   • Assassin (Level 1) - [██████████] 90/90

Party of 4 heroes prepares for battle!

============================================================
Round 1/15
============================================================

2 monsters appear!
   • Zak (Level 1)
   • Iron Bear (Level 1)

--- Combat Turn 1 ---
Thorin attacks Iron Bear with Flamebrand Sword!
55 damage dealt to Iron Bear!
...
Iron Bear has been defeated!

 Victory! Rewards earned:
40 Experience
30 Gold

... [Combat continues through 15 rounds with increasing difficulty] ...

============================================================
Adventure is complete! 🏆
============================================================
   Rounds Completed: 15
   Monsters Defeated: 56
   Total Experience Gained: 8380
   Total Gold Earned: 2655

Final Party Status:
   [Alive]: Thorin (Level 7)
      [████████░░] 231/270
      EXP: 21/1135
   [Alive]: Gandalf (Level 7)
      [██░░░░░░░░] 46/200
      EXP: 21/1135
   [Alive]: Legolas (Level 7)
      [████░░░░░░] 106/220
      EXP: 21/1135
   [Alive]: Assassin (Level 7)
      [█████░░░░░] 107/210
      EXP: 21/1135

============================================================
  FINAL SUMMARY
============================================================

==================================================
  Fantasy Quest
  Difficulty: Normal
  Party Size: 4/4
==================================================

=== Current Party (4/4) ===
1. Thorin - Warrior (Level 7)
2. Gandalf - Mage (Level 7)
3. Legolas - Archer (Level 7)
4. Assassin - Rogue (Level 7)

Warrior 'Thorin' (Level 7)
  HP: [████████░░] 231/270
  Mana: 110 | EXP: 21/1135
  STR: 32 | INT: 17 | AGI: 20
  Weapon: Flamebrand Sword
  Armor: Inferno Plate
```

### Conclusions

This laboratory work successfully demonstrates the practical application of creational design patterns in a fantasy RPG game context, enhanced with a comprehensive combat system. The implementation shows how these patterns solve real-world software design challenges:

- **Factory Method** eliminates tight coupling between creation and specific classes for both characters and monsters
- **Abstract Factory** ensures consistency in themed equipment sets
- **Builder** simplifies complex object construction with multiple optional parameters
- **Singleton** provides centralized game state management
- **Combat System** integrates all components into engaging gameplay with progression mechanics

The modular architecture with separated class files promotes code reusability, maintainability, and scalability, making it easy to extend the game with new features without modifying existing code.
