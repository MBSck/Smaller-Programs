class FinalMeta(type):
    endcls_list = []

    def __init__(cls, *args, **kwargs):
        cls.endcls_list.append(cls)
        super().__init__(*args, **kwargs)

        for i in cls.endcls_list:
            if issubclass(cls, i) and (cls.__name__ != i.__name__):
                raise Exception("This class cannot be inherited!")

    def __call__(cls, *args, **kwargs):
        pass

        return super().__call__(*args, **kwargs)


class Base(metaclass=FinalMeta):
    pass

# yields error as it is inherited


class Derived(Base):
    pass


# Does not yield error as there can be multiple final classes!

class Test(metaclass=FinalMeta):
    pass

# The relevant part is the __init__ function as we are not instancing any classes, e.g. setting their values and
# therefore they are not using the __call__ function