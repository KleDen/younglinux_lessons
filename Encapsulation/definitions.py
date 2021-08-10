from numbers import Number


class Triangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def get_area(self) -> Number:
        return 0.5 * self.__width * self.__height

    def get_height(self) -> Number:
        return self.__height

    def get_width(self) -> Number:
        return self.__width
