import random
import time
from typing import List
from domain.models.character_base import Character
from domain.models.monsters import Monster
from domain.factory.monster_factories import MonsterCreator


class CombatSystem:
    def __init__(self, party: List[Character]):
        self.party = party
        self.round_number = 1
        self.total_experience_gained = 0
        self.total_gold_gained = 0
        self.monsters_defeated = 0
    
    def start_adventure(self, max_rounds: int = 5):
        print(f"Party of {len(self.party)} heroes prepares for battle!")
        self._display_party_status()
        
        for round_num in range(1, max_rounds + 1):
            self.round_number = round_num
            print(f"\n{'='*60}")
            print(f"Round {round_num}/{max_rounds}")
            print(f"{'='*60}")
            
            if not self._party_alive():
                print("Your party has been defeated! Adventure ends.")
                break
            
            # Create monster wave based on round
            monsters = self._generate_monster_wave(round_num)
            
            # Start combat
            if self._combat_encounter(monsters):
                print(f"Round {round_num} victory!")
            else:
                print("Your party was defeated in combat!")
                break
            
        
        self._show_final_summary()
    
    def _generate_monster_wave(self, round_num: int) -> List[Monster]:
        # Increase difficulty with each round
        monster_count = min(2 + (round_num // 2), 4)  # 2-4 monsters
        monster_level = max(1, round_num - 1)
        
        monsters = MonsterCreator.create_monster_wave(monster_count, monster_level)
        
        print(f"\n{monster_count} monsters appear!")
        for monster in monsters:
            print(f"   • {monster.name} (Level {monster.level})")
        
        return monsters
    
    def _combat_encounter(self, monsters: List[Monster]) -> bool:
        turn = 1
        
        while self._party_alive() and self._monsters_alive(monsters):
            print(f"\n--- Combat Turn {turn} ---")
            
            # Party attacks
            for character in self.party:
                if character.is_alive() and self._monsters_alive(monsters):
                    self._character_turn(character, monsters)
            
            # Monsters attack
            for monster in monsters:
                if monster.is_alive() and self._party_alive():
                    self._monster_turn(monster, self.party)
            
            turn += 1
            if turn > 50:  # Prevent infinite loops
                print("Combat timeout - calling it a draw!")
                break
        
        # Handle combat results
        if self._party_alive():
            self._victory_rewards(monsters)
            return True
        else:
            return False
    
    def _character_turn(self, character: Character, monsters: List[Monster]):
        """Handle a character's turn in combat"""
        # Find a living monster to attack
        alive_monsters = [m for m in monsters if m.is_alive()]
        if not alive_monsters:
            return
        
        target = random.choice(alive_monsters)
        
        # Decide between basic and special attack (70% basic, 30% special)
        use_special = random.random() < 0.3
        
        if use_special:
            attack_info = character.special_attack()
            damage = attack_info['damage']
            print(f"{attack_info['description']}")
        else:
            damage = character.basic_attack()
            weapon_name = character.weapon.name if character.weapon else "bare hands"
            print(f"{character.name} attacks {target.name} with {weapon_name}!")
        
        # Apply damage
        target.take_damage(damage)
        print(f"{damage} damage dealt to {target.name}!")
        
        if not target.is_alive():
            print(f"{target.name} has been defeated!")
            self.monsters_defeated += 1
    
    def _monster_turn(self, monster: Monster, party: List[Character]):
        """Handle a monster's turn in combat"""
        # Find a living party member to attack
        alive_party = [c for c in party if c.is_alive()]
        if not alive_party:
            return
        
        target = random.choice(alive_party)
        
        # Monsters use special attack 40% of the time
        use_special = random.random() < 0.4
        
        if use_special:
            attack_info = monster.special_attack()
            damage = attack_info['damage']
            print(f"{attack_info['description']}")
        else:
            damage = monster.basic_attack()
            print(f"{monster.name} attacks {target.name}!")
        
        # Apply damage
        armor_defense = target.armor.defense if target.armor else 0
        actual_damage = max(1, damage - armor_defense)
        target.take_damage(damage)
        
        if armor_defense > 0:
            print(f"Armor absorbs {armor_defense} damage!")
        print(f"{actual_damage} damage dealt to {target.name}!")
        
        if not target.is_alive():
            print(f"{target.name} has fallen!")
    
    def _victory_rewards(self, monsters: List[Monster]):

        total_exp = sum(monster.experience_reward for monster in monsters)
        total_gold = sum(monster.gold_reward for monster in monsters)
        
        self.total_experience_gained += total_exp
        self.total_gold_gained += total_gold
        
        print(f"\n Victory! Rewards earned:")
        print(f"{total_exp} Experience")
        print(f"{total_gold} Gold")
        
        # Distribute experience to living party members
        living_members = [c for c in self.party if c.is_alive()]
        exp_per_member = total_exp // len(living_members) if living_members else 0
        
        for character in living_members:
            character.gain_experience(exp_per_member)
    
    def _rest_party(self):
        for character in self.party:
            if character.is_alive():
                heal_amount = character.max_health // 20  # Heal 5%
                character.heal(heal_amount)
                print(f"   {character.name} recovers {heal_amount} health")
    
    def _party_alive(self) -> bool:
        """Check if any party member is alive"""
        return any(character.is_alive() for character in self.party)
    
    def _monsters_alive(self, monsters: List[Monster]) -> bool:
        """Check if any monster is alive"""
        return any(monster.is_alive() for monster in monsters)
    
    def _display_party_status(self):
        """Display current party status"""
        print(f"\n👥 Party Status:")
        for character in self.party:
            status = "[Alive]" if character.is_alive() else "[Dead]"
            print(f"   {status} {character.name} - {character.get_health_bar()}")
    
    def _show_final_summary(self):
        """Show final adventure summary"""
        print(f"\n{'='*60}")
        print(f"Adventure is complete! 🏆")
        print(f"{'='*60}")
        
        print(f"   Rounds Completed: {self.round_number}")
        print(f"   Monsters Defeated: {self.monsters_defeated}")
        print(f"   Total Experience Gained: {self.total_experience_gained}")
        print(f"   Total Gold Earned: {self.total_gold_gained}")
        
        print(f"\nFinal Party Status:")
        for character in self.party:
            status = "[Alive]" if character.is_alive() else "[Dead]"
            print(f"   {status}: {character.name} (Level {character.level})")
            if character.is_alive():
                print(f"      {character.get_health_bar()}")
                print(f"      EXP: {character.experience}/{character.experience_to_next_level}")