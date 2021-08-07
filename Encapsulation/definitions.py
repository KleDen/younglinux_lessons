# Конструктор принимает высоту и длину основания.
# Метод get_area() возвращает площадь фигуры. Поля сделать приватными.
# Модифицировать прошлые проекты в соответствии с изученным.
# S = 0,5 * b * h, где b — основание, h — высота, проведенная к основанию.

class Triangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def get_area(self) -> int:
        return 0.5 * self.__width * self.__height

    def get_height(self) -> int:
        return self.__height

    def get_width(self) -> int:
        return self.__width
