class WinDoor:
    def __init__(self, x, y):
        self.square = x * y


class Room:
    def __init__(self, width, length, height):
        self.height = height
        self.length = length
        self.width = width
        self.wd = []

    def get_square(self):
        square = 2 * self.height * (self.width + self.length)
        print("Square area is:", square)
        return square

    def addWD(self, w, h):
        self.wd.append(WinDoor(w, h))

    def workSurface(self):
        new_square = self.get_square()
        for i in self.wd:
            new_square -= i.square
        return round(new_square, 1)

    def wallpapers(self, width, length):
        roll_S = width * length
        rolls_of_wallpapers = self.get_square() / roll_S
# Закончить метод
