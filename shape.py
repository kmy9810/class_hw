class Shape:
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, **kwargs):
        self.radius = kwargs['radius']

    def get_area(self):
        return self.radius ** 2 * 3.14


class Rectangle(Shape):
    def __init__(self, **kwargs):
        self.length = kwargs['length']
        self.width = kwargs['width']

    def get_area(self):
        return self.length * self.width


my_circle = Circle(radius=10)
print(my_circle.get_area())

my_rectangle = Rectangle(length=20, width=10)
print(my_rectangle.get_area())