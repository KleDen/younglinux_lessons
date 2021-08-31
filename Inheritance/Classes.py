import uuid


class Unit:
    """Class Unit has complete random uid and optionally takes argument - name of the team """

    def __init__(self, team: str = ""):
        self.uid = uuid.uuid4()
        self.team = team


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
