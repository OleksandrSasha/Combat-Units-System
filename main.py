class Unit:
    def __init__(self, 
                 name: str,
                 health: int,
                 attack_power: int
                 ) -> None:
        
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        if self.health > 0:
            other.take_damage(self.attack_power)
        else:
            print(f"{self.name} is dead and cannot attack.")

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0
            
    def __repr__(self):
        return(
            f"Name {self.name},"
            f"Health {self.health},"
            f"Attack_power {self.attack_power}"
        )
        

class Warrior(Unit):
    def __init__(self, name, health, attack_power, armor: int):
        super().__init__(name, health, attack_power)
        self.armor = armor
    
    def take_damage(self, damage) -> None:
        reduced = max(damage - self.armor, 0)
        self.health -= reduced


class Mage(Unit):
    def __init__(self, name, health, attack_power, mana: int):
        super().__init__(name, health, attack_power)
        self.mana = mana

    def attack(self, other) -> None:
        if not self.is_alive():
            print(f"{self.name} is dead and cannot attack.")
            return

        if self.mana >= 10:
            damage = self.attack_power * 2
            self.mana -= 10
        else:
            damage = self.attack_power

        other.take_damage(damage)


print("\nBattle starts:")
warrior = Warrior("Thor", 120, 15, armor=5)
print(warrior)
mage = Mage("Merlin", 80, 20, mana=30)
print(mage)
units = [warrior, mage]


max_rounds = 5
round_number = 1
    
while warrior.is_alive() and mage.is_alive() and round_number <= max_rounds:
    print(f"\nRound {round_number}")

    warrior.attack(mage)

    if mage.is_alive():
        mage.attack(warrior)
    
    
    round_number += 1


    for unit in units:
        if unit.is_alive():
            print(f"{unit.name} is alive with {unit.health} HP.")
        else:
            print(f"{unit.name} is dead.")
    print(f"{mage.name} mana left: {mage.mana}.")


print("\n--- Final result ---")
if warrior.is_alive():
    print(f"{warrior.name} wins with {warrior.health} HP.")
elif mage.is_alive():
    print(f"{mage.name} wins with {mage.health} HP.")
    print(f"{mage.name} mana left: {mage.mana}.")
else:
    print("Both units are dead.")

