# Combat Units System
# Simple OOP battle simulation in Python.
Ти розробляєш просту модель бойових юнітів.

## Базовий клас Unit
Атрибути:
name: str
health: int
attack_power: int

Методи:
attack(self, other) — зменшує other.health на attack_power
is_alive(self) — повертає True, якщо health > 0
__repr__() — зручний текстовий вивід


## Клас Warrior(Unit)
Додатково:
має броню armor: int
Перевизначає attack():
завдає повну шкоду
Але додає метод:
take_damage(damage)
зменшує шкоду на armor
здоров’я не може збільшуватися

## Клас Mage(Unit)
Додатково:
має mana: int
Перевизначає attack():
якщо mana >= 10
завдає подвійну шкоду
витрачає 10 mana
якщо mana < 10
завдає звичайну шкоду

# Бойова симуляція
Створи:
warrior = Warrior("Thor", 120, 15, armor=5)
mage = Mage("Merlin", 80, 20, mana=30)
Імітуй 3 раунди бою:
units = [warrior, mage]
Кожен раунд:
кожен живий юніт атакує іншого

# Очікуваний результат
Після 4 раундів вивести:
хто живий
їх поточне здоров’я
залишок mana у мага

# Ускладнення (необов'язково)
Заборонити атаку мертвих юнітів
Якщо health ≤ 0 — вивести повідомлення про смерть
Додати клас Archer, який має шанс 30% на критичний удар

## What I practiced

- Inheritance
- super()
- Method overriding
- Polymorphism
- Object interaction