# Combat Facade - Simplifies the complex combat system
import random
from typing import List
from domain.factory.monster_factories import MonsterCreator


class CombatFacade:
    
    def __init__(self):
        self.battle_log = []
    
    def simulate_battle(self, party: List, monsters: List) -> dict:
        # Handles all combat mechanics internally
        self.battle_log.clear()
        
        self._log(f"\nBATTLE START: {len(party)} Heroes vs {len(monsters)} Monsters\n")
        
        while self._is_battle_ongoing(party, monsters):
            # Hero attacks
            for hero in party:
                if not hero.is_alive():
                    continue
                
                alive_monsters = [m for m in monsters if m.is_alive()]
                if not alive_monsters:
                    break
                
                target = random.choice(alive_monsters)
                damage = hero.basic_attack()
                target.take_damage(damage)
                
                self._log(f"{hero.name} attacks {target.name} for {damage} damage!")
                
                if not target.is_alive():
                    self._log(f"{target.name} has been defeated!")
            
            # Monsters attack
            alive_monsters = [m for m in monsters if m.is_alive()]
            for monster in alive_monsters:
                alive_heroes = [h for h in party if h.is_alive()]
                if not alive_heroes:
                    break
                    
                target = random.choice(alive_heroes)
                damage = monster.basic_attack()
                target.take_damage(damage)
                
                self._log(f"{monster.name} attacks {target.name} for {damage} damage!")
        
        return self._calculate_battle_results(party, monsters)
    
    def quick_battle(self, party: List, monster_count: int) -> dict:
        # Initiates a quick battle with random monsters
        
        avg_level = sum(h.level for h in party) // len(party)
        monsters = MonsterCreator.create_monster_wave(monster_count, avg_level)
        
        return self.simulate_battle(party, monsters)
    
    def heal_party(self, party: List, heal_amount: int = 50):
        for hero in party:
            hero.heal(heal_amount)
        self._log(f"Party healed for {heal_amount} HP each!")
    
    def get_battle_log(self) -> str:
        return '\n'.join(self.battle_log)
    
    def _is_battle_ongoing(self, party: List, monsters: List) -> bool:
        party_alive = any(h.is_alive() for h in party)
        monsters_alive = any(m.is_alive() for m in monsters)
        return party_alive and monsters_alive
    
    def _calculate_battle_results(self, party: List, monsters: List) -> dict:
        party_alive = any(h.is_alive() for h in party)
        monsters_defeated = sum(1 for m in monsters if not m.is_alive())
        total_exp = monsters_defeated * 50
        total_gold = monsters_defeated * 30
        
        if party_alive:
            for hero in party:
                if hero.is_alive():
                    hero.gain_experience(total_exp)
            self._log(f"\nVICTORY! Earned {total_exp} EXP and {total_gold} Gold!")
        else:
            self._log(f"\nDEFEAT! All heroes have fallen...")
        
        return {
            'victory': party_alive,
            'monsters_defeated': monsters_defeated,
            'experience_earned': total_exp,
            'gold_earned': total_gold
        }
    
    def _log(self, message: str):
        self.battle_log.append(message)
