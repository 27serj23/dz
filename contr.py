# 

import time


class Castle:
    def __init__(self, strength, satisfaction):
        self.strength = strength
        self.satisfaction = satisfaction

    def restore_strength(self, amount):
        self.strength = min(100, self.strength + amount)

    def restore_satisfaction(self, amount):
        self.satisfaction = min(100, self.satisfaction + amount)

class Counterattack:
    def __init__(self):
        self.used_special_attack = False
        self.last_regular_attack_time = 0

    def restore_castle(self, castle, restore_type, amount):
        if restore_type == "strength":
            castle.restore_strength(amount)
        elif restore_type == "satisfaction":
            castle.restore_satisfaction(amount)

    def perform_regular_attack(self, castle):
        current_time = time.time()
        if current_time - self.last_regular_attack_time > 10:  # 10 seconds interval
            castle.strength -= 10
            self.last_regular_attack_time = current_time
            return "Regular attack performed, Castle strength decreased by 10"
        else:
            return "You can't perform another regular attack yet"

    def perform_special_attack(self, castle):
        if not self.used_special_attack:
            castle.strength += 20
            castle.satisfaction += 20
            self.used_special_attack = True
            return "Special attack performed, Castle strength and satisfaction increased by 20"
        else:
            return "You've already used the special attack"


# Теперь добавим интерфейс управления системой:

castle = Castle(100,100)
counterattack = Counterattack()

while castle.strength > 0:
    print("Castle Stats - Strength: {}, Satisfaction: {}".format(castle.strength, castle.satisfaction))
    choice = input("Enter 'r' to perform regular attack, 's' for special attack, 'q' to quit: ")

    if choice == 'r':
        result = counterattack.perform_regular_attack(castle)
        print(result)
    elif choice == 's':
        result = counterattack.perform_special_attack(castle)
        print(result)
    elif choice == 'q':
        print("You quit the game")
        break
    else:
        print("Invalid choice, try again")

print("Game over")