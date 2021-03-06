from math import ceil


class Snow:
    def __init__(self, snowflake: int):
        self.__snowflake = snowflake

    def set_snowflake(self, flakes: int):
        self.__snowflake = flakes

    def get_snowflake(self):
        return self.__snowflake

    def __add__(self, other):
        """Return Snow object with added amount snowflakes"""
        if isinstance(other, int):
            self.set_snowflake(self.get_snowflake() + other)
        else:  # if other == Snow()
            flakes = self.get_snowflake() + other.get_snowflake()
            self.set_snowflake(flakes)

    def __sub__(self, other):
        if isinstance(other, int):
            self.set_snowflake(self.get_snowflake() - other)
            # TODO <0 error фильтр Нужен определённо, но куда лучше его поставить
        else:  # if other == Snow()
            flakes = self.get_snowflake() - other.get_snowflake()
            self.set_snowflake(flakes)

    def __mul__(self, other: int):
        self.set_snowflake(self.get_snowflake() * other)

    def __truediv__(self, other: int):
        self.set_snowflake(ceil(self.get_snowflake() / other))

    def make_snow(self, n):
        rows = round(self.get_snowflake() / n)
        snowfall = ""
        for o in range(rows):
            for i in range(n):
                snowfall += "*"
            snowfall += "\n"
        print(snowfall)
#ask for review  make_snow()


    def __call__(self, snowflake: int):
        self.set_snowflake(snowflake)