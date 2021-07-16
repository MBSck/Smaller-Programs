# Exercise 6.3

def logger(cls):

    class Inner(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for attr in self.__dict__:
                print(attr, "initialized to", self.__dict__[attr])

        def __setattr__(self, attr, value):
            print("setting", attr, "to", value)
            self.__dict__[attr] = value

        def __getattribute__(self, attr):
            attribute_value = cls.__getattribute__(self, attr)
            # attribute_value = super().__getattribute__(attr) -> also works
            print(f"access {attr} with value {attribute_value}")
            return attribute_value
        '''
        def __getattribute__(self, attr):
            """I have not found a way to access the attributes name in the __dict__ without
            causing a never ending loop, as __dict__ is being accessed by the getattribute function. I would be glad
            if you could help me here"""
            print("accessing class attribute", attr)
            return super().__getattribute__(attr)
        '''

    return Inner

@logger
class Test:
    def __init__(self, test):
        self.test = test

test_123 = Test(3)
test_123.test = 10
