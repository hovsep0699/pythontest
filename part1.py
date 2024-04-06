from abc import ABC, abstractmethod
import math
import unittest

class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return math.pi * self.radius ** 2

class Triangle(Shape):
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def area(self):
		s = (self.a + self.b + self.c) / 2
		return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


# when need new type we just inherit from shape and implement area method

class TestShapeCalculator(unittest.TestCase):
	def test_circle_area(self):
		circle = Circle(5)
		self.assertAlmostEqual(circle.area(), math.pi * 25)
		circle.radius = 3
		self.assertAlmostEqual(circle.area(), 9 * math.pi)

	def test_triangle_area(self):
		tr = Triangle(3, 4, 5)
		self.assertAlmostEqual(tr.area(), 6)
		tr = Triangle(5, 4, 7)
		self.assertAlmostEqual(round(tr.area(), 3), 9.798)

if __name__ == "__main__":
	unittest.main()