# Exercise 5.4

class Rational:
    """This class implements the rational numbers given in a format
    so that Rational(8,6) will yield (4/3)."""
    def __init__(self, numerator=0, denominator=1, modulo=0):
        """Initializes the values and checks for any value errors as well as
        simplifies the fractions. It does this by first checking which denominator
        is bigger and then looking for a number that devides both with rest zero"""
        self.num = numerator
        self.denom = denominator
        self.mod = modulo
        if self.denom == 0:
            raise ValueError("Division by zero is forbidden")

        if self.num > self.denom:
            for i in reversed(range(1, self.num + 1)):
                if (self.num % i == 0) and   (self.denom % i == 0):
                    self.num = self.num // i
                    self.denom = self.denom // i

        elif self.num < self.denom:
            for i in reversed(range(1, self.denom + 1)):
                if (self.num % i == 0) and (self.denom % i == 0):
                    self.num = self.num // i
                    self.denom = self.denom // i

    def __add__(self, other):
        """Returns self + other"""
        if self.denom == other.denom:
            return Rational(self.num + other.num, self.denom)
        else:
            self.denom_mul = self.denom * other.denom
            return Rational((self.num * other.denom) + (other.num * self.denom), self.denom_mul)

    def __sub__(self, other):
        """Returns self - other"""
        if self.denom == other.denom:
            return Rational(self.num - other.num, self.denom)
        else:
            self.denom_mul = self.denom * other.denom
            return Rational((self.num * other.denom) - (other.num * self.denom), self.denom_mul)

    def __mul__(self, other):
        """Returns self * other"""
        return Rational(self.num * other.num, self.denom * other.denom)

    def __divmod__(self, other):
        """Returns the Product of the Division and also the modulo"""
        self.a = self.num / self.denom
        self.b = other.num / other.denom
        return Rational(self.num // other.num, self.denom // other.denom, self.a % self.b)

    def __floordiv__(self, other):
        """Returns the rounded div of self and other"""
        return Rational(self.num // other.num, self.denom // other.denom)

    def __eq__(self, other):
        """Returns a boolean for equality check"""
        if (self.num == other.num) and (self.denom == other.denom):
            return True
        else:
            return False

    def norm(self):
        """Returns self to the power of two"""
        return Rational(self.num ** 2, self.denom ** 2)

    def __str__(self):
        """Returns the output as a string"""
        if self.mod != 0:
            return str(self.num // self.denom) + " with modulo of " + str(round(self.mod, 2))
        elif self.num % self.denom == 0:
            return str(self.num // self.denom)
        else:
            return str(self.num) + "/" + str(self.denom)

frac1 = Rational(3,6)
frac2 = Rational(4,5)
print(frac1)
print(frac2)
print(frac1 - frac2)
print(frac2.__divmod__(frac1))
