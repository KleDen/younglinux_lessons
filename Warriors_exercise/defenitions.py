import random


class Warrior:
    def __init__(self, name):
        self.name = name
        self.hp = 100


def rand_hit(unit1: Warrior, unit2: Warrior):
    """Takes 2 units as a parameters and they randomly hit each other"""

    if unit1 == random.choice([unit1, unit2]):
        unit2.hp -= 20
        print(unit1.name, "was luckier and hit", unit2.name, "by 20! he's now at", unit2.hp, "hp")
    else:
        unit1.hp -= 20
        print(unit2.name, "was luckier and hit", unit1.name, "by 20! he's now at", unit1.hp, "hp")


def battle(unit1: Warrior, unit2: Warrior):
    """This func uses rand_hit until someone runs out of hp"""
    while unit1.hp > 0 or unit2.hp > 0:
        rand_hit(unit1, unit2)

        if unit1.hp == 0:
            print(unit2.name, "Win this fight!!!")
            break
        if unit2.hp == 0:
            print(unit1.name, "Win this fight!!!")
            break
