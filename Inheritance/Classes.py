class Unit:
    """Class Unit have ordered uid and optionally takes argument - name of the team """
    counter = 0

    def __init__(self, team: str = ""):
        self.uid = Unit.counter
        self.team = team
        Unit.counter += 1


class Hero(Unit):

    def __init__(self, team: str = None):
        super().__init__(team)
        self.lvl = 1

    def lvlup(self, lvl=1):
        if not isinstance(lvl, int):
            raise TypeError("It must be a whole number")
        if lvl <= 0:
            raise ValueError("It's not gonna lvldown Hero!")
        """Lvlup's Hero by given int. default set to 1"""
        self.lvl += lvl


class Solder(Unit):
    @staticmethod
    def follow(hero: Hero):
        if hero.team == None:
            hero.team = "Unnamed"
        return f"Иду за героем из команды {hero.team}"
