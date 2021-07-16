# Exercise 5.2
import math


class Square:
    def __init__(self, length):
        self.length = length

    def get_area(self):
        return self.length**2

    def set_area(self, area):
        self.length = math.sqrt(area)

    area = property(get_area, set_area)


my_square = Square(5)
print(my_square.area)
my_square.area = 144
print(my_square.length)

