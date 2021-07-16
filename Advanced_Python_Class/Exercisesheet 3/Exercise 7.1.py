# One Way
class SingletonMeta(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super(SingletonMeta, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)

        return cls.__instance

class Person(metaclass=SingletonMeta):
    def __init__(self, name):
        self.name = name

myself = Person("Peter")
you = Person("Joseph")

myself.age = 24

# Deep
print(myself is you)
print(you.name, you.age)
