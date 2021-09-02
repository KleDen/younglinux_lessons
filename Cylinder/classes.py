from math import pi


class Cylinder:
    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle * 2 + side, 2)

    def __init__(self, diameter, high):
        self.dia = diameter
        self.h = high

    def get_area(self):
        return self.make_area(self.dia, self.h)

    def __setattr__(self, key, value):
        if key == "dia" or "h":
            self.__dict__[key] = value
        else:
            raise AttributeError

