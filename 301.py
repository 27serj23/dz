#-----------------------------Задача 2:------------------------------#
# Работа с геометрическими фигурами
# Реализуйте класс Rectangle, представляющий прямоугольник.
# В классе должны быть атрибуты width и height,
# а также методы calculate_area (вычисление площади) и
# calculate_perimeter (вычисление периметра).
# Создайте собственный класс исключения InvalidDimensionsError,
# который будет возбуждаться при создании прямоугольника с неположительной шириной или высотой.

class InvalidDimensionsError(Exception):
    pass

class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise InvalidDimensionsError("Ширина и высота прямоугольника должны быть положительными числами.")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

# Пример использования
try:
    rectangle = Rectangle(10, 5)
    print("Площадь прямоугольника:", rectangle.calculate_area())
    print("Периметр прямоугольника:", rectangle.calculate_perimeter())
except InvalidDimensionsError as e:
    print(f"Ошибка: {e}")

















