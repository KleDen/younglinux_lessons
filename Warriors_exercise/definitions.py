import random


class Warrior:
    def __init__(self, name, hp=100, damage=20):
        if hp < 0:
            raise ValueError("Hp can't be negative!")
        self.damage = damage
        self.name = name
        self.hp = hp


    def is_alive(self):
        return self.hp > 0

    def get_damaged(self, damage: int):
        if damage < 0:
            raise ValueError("Damage can't be negative!")
        self.hp -= damage
        print(self.name, "take", damage, "damage, he's now at", self.hp, "hp")


def define_roles(units: list) -> tuple:
    """
    randomly selects attacker and target
    """
    random.shuffle(units)
    lucky, target = units[0], units[1]
    return lucky, target


def battle(unit1: Warrior, unit2: Warrior):
    """
    Takes 2 units as a parameters and they randomly hit each other
    """
    units = [unit1, unit2]
    lucky, target = define_roles(units)

    while target.is_alive():
        lucky, target = define_roles(units)

        print(lucky.name, "hit", target.name, )
        target.get_damaged(lucky.damage)

    print(lucky.name, "Win this fight!!!")
