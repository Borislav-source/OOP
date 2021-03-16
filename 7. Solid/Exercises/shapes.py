from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def shape_area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def shape_area(self):
        return self.width * self.height


class Triangle(Shape):

    def __init__(self, height, base):
        self.height = height
        self.base = base

    def shape_area(self):
        return (self.height * self.base) / 2


class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.shape_area()

        return total


shapes = [Rectangle(2, 3), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
