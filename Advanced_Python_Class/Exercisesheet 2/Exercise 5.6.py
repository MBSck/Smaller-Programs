# Exercise 5.6
import math


class Shape2D:
    sides = 0

    def __init__(self, pos_x, pos_y, *args):
        self.pos = [pos_x, pos_y]
        self.distance_x_to_object = 0
        self.distance_y_to_object = 0

        self.number_of_args = 0
        if len(args) == 1:
            self.attr = args[0]
            self.attr = [self.attr]
        else:
            self.attr = []
            for i in args:
                self.attr.append(i)

        self.attr_from_center = []
        for i in args:
            self.attr_from_center.append(i/2)

    def get_center_distance(self, other):
        """Gets the distance of two objects in x and y coordinates (point of origin is their respective center)"""
        for i in range(2):
            res = math.sqrt((self.pos[i] - other.pos[i]) ** 2)
            if i == 0:
                self.distance_x_to_object = res
            else:
                self.distance_y_to_object = res

        return self.distance_x_to_object, self.distance_y_to_object

    def is_intersecting(self, other):
        """Checks basic intersection. Values of attributes always from the center."""
        for i in range(2):
            if self.get_center_distance(other)[i] > self.attr_from_center[i] + other.attr_from_center[i]:
                return False
            elif self.get_center_distance(other)[i] <= other.attr_from_center[i]:
                return True


class Square(Shape2D):
    sides = 4

    def __init__(self, pos_x, pos_y, *args):
        super().__init__(pos_x, pos_y, *args)
        for i in args:
            self.attr_from_center.append(i/2)


class Rectangle(Shape2D):
    sides = 4

    def __init__(self, pos_x, pos_y, *args):
        super().__init__(pos_x, pos_y, *args)


class Circle(Shape2D):
    def __init__(self, pos_x, pos_y, *args):
        super().__init__(pos_x, pos_y, *args)
        self.attr_from_center = self.attr
        for i in args:
            self.attr_from_center.append(i)


class Pentagon(Shape2D):
    sides = 6

    """Regular Pentagon (all sides have the same length)"""
    def __init__(self, pos_x, pos_y, *args):
        super().__init__(pos_x, pos_y, *args)
        """Calculates the Width and the Height of the Pentagon, pick one side"""
        self.attr_from_center[0] = ((1 + math.sqrt(5))/2) * self.attr[0]
        self.attr_from_center.append(((math.sqrt(5 + 2*math.sqrt(5)))/2) * self.attr[0])


# Module test
if __name__ == "__main__":
    circle1 = Circle(0, 0, 1)
    circle2 = Circle(0, 2, 2)
    square1 = Square(2, 0, 2)
    square2 = Square(4, 0, 2)
    rectangle1 = Rectangle(4, 0, 2, 1)
    rectangle2 = Rectangle(1, 0, 4, 1)
    pentagon1 = Pentagon(0, 0, 4)
    pentagon2 = Pentagon(3, 4, 2)

    print(square1.is_intersecting(rectangle2))
    print(rectangle1.is_intersecting(circle2))
    print(pentagon2.is_intersecting(square2))


# Lösungsvorschlag, Tuple aus Schlüsselobjekten und Decorator added es in der Shape classe.
# Dreiecke und Kreise unterscheiden ist das einfachste, da dreiecke jede andere eckige form darstellen können.
# Quader = 2 Dreiecke, Pentagon sind 4 Dreiecke. Gute Lösung hängt von Umgebung ab, muss es oft erweitert werden?
# -> Dann Dreiecke. Bei benötigter sehr schneller Ausführung jedes Teil hardcoden.
# Vorteil hier jede Form möglich, Nachteil laufzeitprobleme
