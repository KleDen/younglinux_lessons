import random


class Warrior:
    def __init__(self, name, hp=100):
        self.hp = hp
        self.name = name

    def is_alive(self):
        return self.hp > 0

    def get_damaged(self, damage: int):
        self.hp -= damage
        print(self.name, "take", damage, "damage, he's now at", self.hp, "hp")


def rand_hit(unit1: Warrior, unit2: Warrior):
    """Takes 2 units as a parameters and they randomly hit each other"""
    units = [unit1, unit2]
    random.shuffle(units)
    attack, defend = units[0], units[1]

    print(attack.name, "hit", defend.name, )
    defend.get_damaged(20)


def battle(unit1: Warrior, unit2: Warrior):
    """This func uses rand_hit until someone runs out of hp"""
    while True:
        rand_hit(unit1, unit2)

        if not unit1.is_alive():
            winner = unit2
        if not unit2.is_alive():
            winner = unit1

            print(winner.name, "Win this fight!!!")
            break
