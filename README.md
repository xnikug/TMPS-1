# Structural Design Patterns

## Author: Nicolae Marga, FAF-231

----

## Objectives

- Understand structural design patterns
- Choose a specific domain (Fantasy RPG System)
- Implement at least 3 structural design patterns for the domain
- Demonstrate pattern composition and real-world usage

## Used Design Patterns

- Decorator Pattern
- Facade Pattern
- Proxy Pattern
- Composite Pattern

---

## Implementation

### Domain Context

The structural patterns were implemented in a Fantasy RPG combat system. The domain includes characters (Warriors, Mages, Archers), equipment, monsters, and combat mechanics. Structural patterns address cross-cutting concerns: dynamically enhancing character abilities without inheritance, simplifying complex combat logic, and controlling resource access.

### 1. Decorator Pattern

**Purpose:** Dynamically add enhancements (potions, buffs, enchantments) to characters at runtime without creating exponential subclass combinations.

```python
class CharacterDecorator:
    def __init__(self, character):
        self._character = character
    
    def __getattr__(self, name):
        return getattr(self._character, name)

class StrengthPotionDecorator(CharacterDecorator):
    def __init__(self, character, strength_bonus: int = 8):
        super().__init__(character)
        self._strength_bonus = strength_bonus
    
    @property
    def strength(self):
        return self._character.strength + self._strength_bonus
    
    def basic_attack(self):
        base_damage = self._character.basic_attack()
        bonus = self._strength_bonus // 2
        return base_damage + bonus
```

**Usage:**
```python
warrior = CharacterCreator.create_character(CharacterClass.WARRIOR, "Thorin")
enhanced = StrengthPotionDecorator(warrior, strength_bonus=8)
super_enhanced = ShieldEnchantmentDecorator(enhanced, damage_reduction=0.20)
```

**Benefits:**
- No subclass explosion
- Stack multiple enhancements transparently
- Add/remove behaviors at runtime

---

### 2. Facade Pattern

**Purpose:** Simplify the complex combat system (30+ steps: initialization, turns, damage calculation, rewards, logging) behind a single interface.

```python
class CombatFacade:
    def __init__(self):
        self.battle_log = []
    
    def quick_battle(self, party: List[Character], monster_count: int) -> dict:
        from domain.factory.monster_factories import MonsterCreator
        
        avg_level = sum(h.level for h in party) // len(party)
        monsters = MonsterCreator.create_monster_wave(monster_count, avg_level)
        return self.simulate_battle(party, monsters)
    
    def simulate_battle(self, party: List, monsters: List) -> dict:
        while self._is_battle_ongoing(party, monsters):
            for hero in party:
                if hero.is_alive():
                    target = random.choice([m for m in monsters if m.is_alive()])
                    damage = hero.basic_attack()
                    target.take_damage(damage)
                    self._log(f"{hero.name} attacks {target.name} for {damage}!")
            
            for monster in [m for m in monsters if m.is_alive()]:
                target = random.choice([h for h in party if h.is_alive()])
                damage = monster.basic_attack()
                target.take_damage(damage)
                self._log(f"{monster.name} attacks {target.name}!")
        
        return self._calculate_battle_results(party, monsters)
```

**Usage:**
```python
facade = CombatFacade()
result = facade.quick_battle(party, 2)
print(f"Victory: {result['victory']}")
print(f"XP Earned: {result['experience_earned']}")
```

**Benefits:**
- Single method replaces 30+ manual steps
- Hides complex battle mechanics
- Decouples client from combat subsystem

---

### 3. Proxy Pattern

**Purpose:** Lazy-load expensive character objects on first access and automatically track all attribute accesses for auditing.

```python
class CharacterProxy:
    def __init__(self, character_loader, name: str):
        self._character = None
        self._character_loader = character_loader
        self._name = name
        self._access_log = []
    
    def _ensure_loaded(self):
        if self._character is None:
            self._character = self._character_loader(self._name)
            self._log(f"Character '{self._name}' loaded")
    
    @property
    def strength(self):
        self._ensure_loaded()
        self._log(f"Accessed strength: {self._character.strength}")
        return self._character.strength
    
    def get_access_log(self):
        return self._access_log
```

**Usage:**
```python
proxy = CharacterProxy(
    lambda name: CharacterCreator.create_character(CharacterClass.ARCHER, name),
    "Legolas"
)
# Character NOT loaded yet
name = proxy.name  # NOW loads on first access
print(proxy.get_access_log())
```

**Benefits:**
- Lazy-loading defers expensive operations
- Automatic access logging for auditing
- Transparent to client code
- Resource control and optimization

---

### 4. Composite Pattern

**Purpose:** Build hierarchical squad structures where individual characters and squads can be treated uniformly. Squads contain sub-squads and characters, forming a tree structure that supports operations across entire hierarchies.

```python
class SquadComponent:
    def get_total_damage(self) -> int:
        pass
    
    def get_total_health(self) -> int:
        pass
    
    def get_members_count(self) -> int:
        pass
    
    def display_info(self, indent: int = 0) -> str:
        pass

class CharacterComponent(SquadComponent):
    def __init__(self, character):
        self.character = character
    
    def get_total_damage(self) -> int:
        return self.character.basic_attack()
    
    def get_total_health(self) -> int:
        return self.character.health
    
    def get_members_count(self) -> int:
        return 1
    
    def get_average_level(self) -> float:
        return float(self.character.level)
    
    def display_info(self, indent: int = 0) -> str:
        spacing = "  " * indent
        return (f"{spacing}├─ {self.character.name} "
                f"(Lvl {self.character.level}) | "
                f"HP: {self.character.health}/{self.character.max_health}")

class Squad(SquadComponent):
    def __init__(self, name: str):
        self.name = name
        self.members = []
    
    def add_member(self, component: SquadComponent) -> None:
        self.members.append(component)
    
    def remove_member(self, component: SquadComponent) -> None:
        if component in self.members:
            self.members.remove(component)
    
    def get_total_damage(self) -> int:
        return sum(member.get_total_damage() for member in self.members)
    
    def get_total_health(self) -> int:
        return sum(member.get_total_health() for member in self.members)
    
    def get_members_count(self) -> int:
        return sum(member.get_members_count() for member in self.members)
    
    def display_info(self, indent: int = 0) -> str:
        spacing = "  " * indent
        info = f"{spacing}Squad: {self.name}\n"
        info += f"{spacing}   Members: {self.get_members_count()} | "
        info += f"Avg Level: {self.get_average_level():.1f}\n"
        
        for member in self.members:
            info += member.display_info(indent + 1) + "\n"
        
        return info.rstrip()
```

**Usage:**
```python
warrior1 = CharacterCreator.create_character(CharacterClass.WARRIOR, "Aragorn")
warrior2 = CharacterCreator.create_character(CharacterClass.WARRIOR, "Gimli")
archer = CharacterCreator.create_character(CharacterClass.ARCHER, "Legolas")
mage = CharacterCreator.create_character(CharacterClass.MAGE, "Gandalf")

melee_squad = Squad("Melee Squad")
melee_squad.add_member(CharacterComponent(warrior1))
melee_squad.add_member(CharacterComponent(warrior2))

ranged_squad = Squad("Ranged Squad")
ranged_squad.add_member(CharacterComponent(archer))
ranged_squad.add_member(CharacterComponent(mage))

main_squad = Squad("The Fellowship")
main_squad.add_member(melee_squad)
main_squad.add_member(ranged_squad)

print(main_squad.display_info())
print(f"Total Members: {main_squad.get_members_count()}")
print(f"Total Damage: {main_squad.get_total_damage()}")
print(f"Average Level: {main_squad.get_average_level():.1f}")
```

**Benefits:**
- Treat individual characters and entire squads uniformly
- Build complex hierarchies with simple tree operations
- Easily calculate aggregate statistics across hierarchies
- Add/remove members at any level dynamically

---

## Running the Demo

```bash
cd /home/user1/TMPS-1
PYTHONPATH=/home/user1/TMPS-1:$PYTHONPATH python3 client/structural_demo.py
```

## Project Structure

```
domain/structural/
├── decorators/
│   ├── character_decorator.py
│   ├── strength_potion_decorator.py
│   ├── shield_enchantment_decorator.py
│   └── spell_buff_decorator.py
├── facades/
│   └── combat_facade.py
├── proxies/
│   └── character_proxy.py
└── composites/
    └── squad.py

client/
└── structural_demo.py
```

---

## Output / Results

When running the demo, you will see an interactive demonstration of all four structural patterns:

### 1. Decorator Pattern Output

```
============================================================
  1. DECORATOR PATTERN
============================================================

Creating Warrior: Thorin
[WarriorFactory] Creating a mighty warrior named 'Thorin'
  Base Strength: 20
  Base Attack: 15

Adding Strength Potion (+8 STR)
  New Strength: 28
  New Attack: 23

Adding Shield Enchantment (20% damage reduction)
  Damage taken (50 hit): 40

Creating Mage: Gandalf
[MageFactory] Creating a powerful mage named 'Gandalf'
  Base Intelligence: 25
  Base Mana: 150

Adding Spell Buff (+5 INT, +30 Mana)
  New Intelligence: 30
  New Mana: 180
```

### 2. Facade Pattern Output

```
============================================================
  2. FACADE PATTERN
============================================================

Executing quick_battle(party, 2)...

Battle Result:
  Victory: YES
  Monsters Defeated: 2
  Experience Earned: 100
  Gold Earned: 60

Battle Log:
BATTLE START: 2 Heroes vs 2 Monsters

Thorin attacks Grax for 23 damage!
Gandalf attacks Shadow Cat for 18 damage!
Grax attacks Thorin for 8 damage!
Shadow Cat attacks Gandalf for 12 damage!
Thorin attacks Grax for 25 damage!
Grax has been defeated!
Gandalf attacks Shadow Cat for 21 damage!
Shadow Cat has been defeated!

VICTORY! Earned 100 EXP and 60 Gold!
```

### 3. Proxy Pattern Output

```
============================================================
  3. PROXY PATTERN
============================================================

Creating Archer via Proxy
  [OK] Proxy created (character not loaded yet)

First access: proxy.name
[CharacterProxy] Loading character 'Legolas'...
[ArcherFactory] Creating a skilled archer named 'Legolas'
  [Access #1] Character loaded
  [Access #2] Accessed name: Legolas
  [OK] Character loaded! Name: Legolas

Accessing proxy attributes:
  [Access #3] Accessed strength: 12
  Strength: 12
  [Access #4] Accessed agility: 22
  Agility: 22

Executing: proxy.basic_attack()
  [Access #5] Executed basic attack
  Damage: 8

Access Log:
  Total Accesses: 5
  * [Access #1] Character loaded
  * [Access #2] Accessed name: Legolas
  * [Access #3] Accessed strength: 12
  * [Access #4] Accessed agility: 22
  * [Access #5] Executed basic attack
```

### 4. Composite Pattern Output

```
============================================================
  4. COMPOSITE PATTERN
============================================================

Creating characters:
[WarriorFactory] Creating a mighty warrior named 'Aragorn'
  [OK] Aragorn (Warrior)
[WarriorFactory] Creating a mighty warrior named 'Gimli'
  [OK] Gimli (Warrior)
[ArcherFactory] Creating a skilled archer named 'Legolas'
  [OK] Legolas (Archer)
[MageFactory] Creating a powerful mage named 'Gandalf'
  [OK] Gandalf (Mage)

Building squad hierarchy:
  [OK] Melee Squad (2 warriors)
  [OK] Ranged Squad (archer + mage)
  [OK] The Fellowship created

Hierarchical Structure:
 Squad: The Fellowship
   Members: 4 | Avg Level: 1.0
  Squad: Melee Squad
     Members: 2 | Avg Level: 1.0
    ├─ Aragorn (Lvl 1) | HP: 150/150
    ├─ Gimli (Lvl 1) | HP: 150/150
  Squad: Ranged Squad
     Members: 2 | Avg Level: 1.0
    ├─ Legolas (Lvl 1) | HP: 100/100
    ├─ Gandalf (Lvl 1) | HP: 80/80

Squad Statistics:
  Total Members: 4
  Average Level: 1.0
  Combined Damage: 52
  Combined Health: 480

Melee Squad Stats:
  Members: 2
  Total Damage: 30

Ranged Squad Stats:
  Members: 2
  Total Damage: 22

Adding new warrior to Melee Squad:
[WarriorFactory] Creating a mighty warrior named 'Boromir'
  [OK] Boromir added
  Melee Squad Members: 3
  Fellowship Members: 5
```

### 5. Combined Patterns Output

```
============================================================
  BONUS: All Patterns Combined
============================================================

Step 1: Create character via Proxy
[CharacterProxy] Loading character 'Elite-Warrior'...
[WarriorFactory] Creating a mighty warrior named 'Elite-Warrior'
  [Access #1] Character loaded
  [Access #2] Accessed level: 1
  [OK] Character loaded

Step 2: Stack Decorators
  [OK] Decorators applied

Step 3: Battle via Facade
  Battle: Victory!
  XP Earned: 50

Step 4: Proxy Access Log
  Total accesses: 2
```

---

## Conclusions / Results

Several Design Patterns were implemented in this laboratory work. Decorators let characters stack potions and buffs without creating long chains of subclasses, which is much easier. Facades make big systems simple, so combat can run with just one call and the client code stays clean. Proxies give control and can load characters only when needed, also adding automatic logging. These patterns can work together too. Decorators improve characters, Facades handle battles, Proxies delay loading, and Composites make squads. Overall, they help keep code organized, easy to change, and follow clean principles like single responsibility and open/closed, but without making everything too rigid and complicated.
