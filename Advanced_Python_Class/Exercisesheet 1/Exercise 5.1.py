# Exercise 5.1

import math


class Sphere:
    def __init__(self, radius, position):
        """Initializes the class with the position and radius
        originating at the center of the sphere."""
        self.radius = radius
        self.position = position

    def area_surface(self):
        """Returns the surface area of the sphere."""
        return 4 * math.pi * self.radius**2

    def volume(self):
        """Returns the volume of the sphere."""
        return (4/3) * math.pi * self.radius**3

    def is_intersecting(self, other):
        """Returns a boolean corresponding to the status of the intersection,
        true for intersect and false for not intersecting."""
        if (math.sqrt((self.position - other.position)**2) <= other.radius or
                math.sqrt((self.position - other.position)**2) <= self.radius):
            return True
        else:
            return False


sphere_1 = Sphere(3,3)
sphere_2 = Sphere(3,0)
print(sphere_1.is_intersecting(sphere_2))

# The intersecting function should return a boolean (True or False)

