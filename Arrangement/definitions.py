"""Module contains class Room and class WinDoor for inner calculations"""

from math import ceil


class WinDoor:
    """Class for objects that take usable space and will not be covered with wallpapers"""
    def __init__(self, x, y):
        self.__square = x * y

    def get_square(self) -> float:
        return self.__square


class Room:
    """Class Room
    constructor takes 3 argument and returns Room object """

    def __init__(self, width: float, length: float, height: float):
        self.height = height
        self.length = length
        self.width = width
        self.wd = []

    def get_square(self) -> float:
        square = 2 * self.height * (self.width + self.length)
        return square

    def addWD(self, w: float, h: float) -> None:
        """Method for adding Win-Door elements to a Room"""
        self.wd.append(WinDoor(w, h))

    def workSurface(self) -> float:
        """Method for calculating __area without Win-Door elements"""
        new_square = self.get_square()
        for i in self.wd:
            new_square -= i.get_square()
        if new_square <= 0:
            raise ValueError("Area can not be negative!")
        return round(new_square, 1)

    def wallpapers(self, width: float, length: float) -> int:
        """Method for calculating required amount rolls of wallpapers"""
        roll_area = width * length
        rolls_of_wallpapers = self.workSurface() / roll_area
        return ceil(rolls_of_wallpapers)

    def __add__(self, other) -> float:
        """By adding 2 Room objects, you'll get sum of they square __area  """
        return self.get_square() + other.get_square()
