# Abstract Shape Math Engine with Operator Overloading
from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

# Vector class
class Vector(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return math.sqrt(self.x**2 + self.y**2)  # Vector magnitude

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.area() < other.area()

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return f"Circle(radius={self.radius}, area={self.area():.2f})"

v1 = Vector(3, 4)
v2 = Vector(2, 5)

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Vector Addition:", v1 + v2)
print("Vectors Equal:", v1 == v2)
print("Vector 1 Smaller:", v1 < v2)

c1 = Circle(5)
c2 = Circle(3)

print("\nCircle 1:", c1)
print("Circle 2:", c2)
print("Circle 1 Area:", round(c1.area(), 2))
print("Circle 2 Area:", round(c2.area(), 2))
print("Circle 1 Smaller:", c1.area() < c2.area())