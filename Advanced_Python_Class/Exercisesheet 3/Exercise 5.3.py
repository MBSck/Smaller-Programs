import datetime


class Person:
    def __init__(self, name, day_birth, month_birth, year_birth):
        self.name = name

        self.day_b = day_birth
        self.month_b = month_birth
        self.year_b = year_birth

        self.time = datetime.datetime.now()

    @property
    def age(self):
        self.year_difference = self.time.year - self.year_b
        if self.time.month >= self.month_b:
            if self.time.day >= self.day_b:
                return self.year_difference
            else:
                return self.year_difference - 1
        else:
            return self.year_difference - 1

    def __repr__(self):
        return f"{self.name} is {self.age} years old"

    def __str__(self):
        return f"{self.name} is {self.age} years old"


myself = Person("Marten", 1, 12, 1995)
print(myself)