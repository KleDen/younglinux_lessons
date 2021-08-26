import random
import uuid


class Unit:
    def __init__(self, team: str = ""):
        self.uid = uuid.uuid4()
        self.team = team


class Hero(Unit):

    def __init__(self, team: str = ""):
        super().__init__(team)
        self.lvl = 1

    def lvlup(self):
        self.lvl += 1


class Solder(Unit):

    @staticmethod
    def follow(hero: Hero):
        print(f"Иду за героем из команды {hero.team}")
