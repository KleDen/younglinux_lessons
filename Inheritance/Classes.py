"""Module contains parental class Unit and 2 child class - Hero, Solder"""


class Unit:
    """Class Unit have ordered uid and optionally takes argument - name of the team """
    counter = 0

    def __init__(self, team: str = ""):
        self.uid = Unit.counter
        self.team = team
        Unit.counter += 1


class Hero(Unit):
    """Subclass of Unit. has method to lvlup himself"""
    def __init__(self, team: str = "Unnamed"):
        super().__init__(team)
        self.lvl = 1

    def lvlup(self, lvl: int = 1):
        """Lvlup's Hero by given int. default set to 1"""
        if not isinstance(lvl, int):
            raise TypeError("It must be a whole number")
        if lvl <= 0:
            raise ValueError("It's not gonna lvldown Hero!")
        self.lvl += lvl


class Solder(Unit):
    """Class Solder can be created without arguments"""
    @staticmethod
    def follow(hero: Hero):
        return f"Иду за героем из команды {hero.team}"
