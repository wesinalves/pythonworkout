import random
import time

class Gladiator:
    def __init__(self, name, strength, skill, health, weapons):
        self.name = name
        self.max_health = health
        self.current_health = health
        self.strength = strength
        self.skill = skill
        self.weapons = weapons
        self.is_alive = True
    
    def attack(self, opponent):
        """Perform an attack on the opponent"""
        # Calculate base damage
        base_damage = self.strength * random.uniform(0.7, 1.3)
        
        # Factor in skill and weapon bonus
        weapon = random.choice(self.weapons)
        skill_modifier = self.skill / 10
        weapon_bonus = weapon['damage_bonus']
        
        total_damage = base_damage * (1 + skill_modifier) * weapon_bonus
        
        # Apply damage to opponent
        opponent.take_damage(total_damage)
        
        return {
            'attacker': self.name,
            'weapon': weapon['name'],
            'damage': round(total_damage, 2)
        }
    
    def take_damage(self, damage):
        """Receive damage and update health"""
        self.current_health -= damage
        
        if self.current_health <= 0:
            self.current_health = 0
            self.is_alive = False
    
    def heal(self, amount):
        """Heal the gladiator"""
        self.current_health = min(self.max_health, self.current_health + amount)
    
    def status(self):
        """Return current status of the gladiator"""
        return {
            'name': self.name,
            'health': round(self.current_health, 2),
            'max_health': self.max_health,
            'is_alive': self.is_alive
        }

class Arena:
    def __init__(self, name):
        self.name = name
        self.spectators = random.randint(500, 5000)
    
    def battle(self, gladiator1, gladiator2):
        """Simulate a battle between two gladiators"""
        print(f"\n🏛️ Battle in the {self.name} Arena! 🏛️")
        print(f"Spectators: {self.spectators}")
        print(f"{gladiator1.name} vs {gladiator2.name}\n")
        
        round_number = 1
        battle_log = []
        
        while gladiator1.is_alive and gladiator2.is_alive:
            print(f"--- Round {round_number} ---")
            
            # Alternate attacks
            if round_number % 2 == 1:
                attack_result = gladiator1.attack(gladiator2)
            else:
                attack_result = gladiator2.attack(gladiator1)
            
            battle_log.append(attack_result)
            
            # Print attack details
            print(f"{attack_result['attacker']} strikes with {attack_result['weapon']} for {attack_result['damage']} damage!")
            print(f"{gladiator1.name} Health: {gladiator1.current_health}")
            print(f"{gladiator2.name} Health: {gladiator2.current_health}\n")
            
            round_number += 1
            time.sleep(1)  # Dramatic pause between rounds
        
        # Determine winner
        winner = gladiator1 if gladiator1.is_alive else gladiator2
        loser = gladiator2 if gladiator1.is_alive else gladiator1
        
        print(f"🏆 {winner.name} VICTORIES! 🏆")
        print(f"{loser.name} falls in battle...")
        
        return {
            'winner': winner.name,
            'loser': loser.name,
            'rounds': round_number - 1,
            'battle_log': battle_log
        }

def main():
    # Define weapons with damage bonuses
    weapons = [
        {'name': 'Gladius', 'damage_bonus': 1.2},
        {'name': 'Trident', 'damage_bonus': 1.1},
        {'name': 'Battle Axe', 'damage_bonus': 1.3},
        {'name': 'Mace', 'damage_bonus': 1.0}
    ]

    # Create gladiators
    maximus = Gladiator(
        name="Maximus", 
        strength=90, 
        skill=85, 
        health=100, 
        weapons=weapons
    )

    commodus = Gladiator(
        name="Commodus", 
        strength=75, 
        skill=60, 
        health=100, 
        weapons=weapons
    )

    # Create arena
    colosseum = Arena("Colosseum")

    # Battle!
    result = colosseum.battle(commodus, maximus)
    
    # Print detailed battle report
    print("\n--- Battle Report ---")
    for entry in result['battle_log']:
        print(f"{entry['attacker']} used {entry['weapon']} for {entry['damage']} damage")

if __name__ == "__main__":
    main()