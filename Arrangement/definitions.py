from math import ceil


class WinDoor:
    def __init__(self, x, y):
        self.__square = x * y

    def get_square(self) -> float:
        return self.__square


class Room:
    def __init__(self, width: float, length: float, height: float):
        self.height = height
        self.length = length
        self.width = width
        self.wd = []

    def get_square(self) -> float:
        square = 2 * self.height * (self.width + self.length)
        return square

    def addWD(self, w: float, h: float) -> None:
        self.wd.append(WinDoor(w, h))

    def workSurface(self) -> float:
        new_square = self.get_square()
        for i in self.wd:
            new_square -= i.get_square()
        if new_square <= 0:
            raise ValueError("Area can not be negative!")
        return round(new_square, 1)

    def wallpapers(self, width: float, length: float) -> int:
        roll_area = width * length
        rolls_of_wallpapers = self.workSurface() / roll_area
        return ceil(rolls_of_wallpapers)

    def __add__(self, other) -> float:
        return self.get_square() + other.get_square()
    # return area of apartment walls
