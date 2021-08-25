class Unit:
    def __init__(self, team: str):
        self.team = team
        # self.uid = uuid4()
        # Easy way
        self.uid = 0
        # self.uid += 1
# TODO посмотреть на счётчик UID


class Hero:
    def __init__(self, name):
        self.name = name
        self.__lvl = 1

    def lvl_up(self):
        self.__lvl += 1

    def get_lvl(self):
        return self.__lvl


class Solder:
    @staticmethod
    def follow(hero: Hero):
        print(f"иду за героем {hero.name}")


a = Solder()
b = Solder()
s = Hero("Nans")

a.follow(s)

