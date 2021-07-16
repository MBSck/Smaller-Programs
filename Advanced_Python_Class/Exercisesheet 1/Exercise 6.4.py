# Exercise 6.4

import inspect


def check_range(function):

    def inner(*args, **kwargs):
        binded_arg_list = []
        annotation_list = []
        binded_args = inspect.signature(function).\
            bind(*args, **kwargs).arguments
        for arg in binded_args:
            binded_arg_list.append(binded_args[arg])
            annotation_list.append(function.__annotations__[arg])
        range_a, range_b = annotation_list[0], annotation_list[1]
        arg_a, arg_b = binded_arg_list[0], binded_arg_list[1]
        if (arg_a in range(range_a[0]), range_a[1] + 1) and\
                (arg_b in range(range_b[0], range_b[1] + 1)):
            return function(*args, **kwargs)
        else:
            raise ValueError("The input values are outside of the boundaries")

    return inner

# range gibt nur integer werte, lieber obere und untere grenze checken, wenn float
# Can be written more cleanily

def check_range(function):

    def inner(*args, **kwargs):

        binded_args = inspect.signature(function).bind(*args, **kwargs).arguments

        for arg in binded_args:

            if not binded_args[arg] in range(f.__annotations__[arg][0], f.__annotations__[arg][1]):
                raise ValueError("Out of input range")

            return function(*args, **kwargs)

    return inner

@check_range
def f(a: (0, 9), b: (3, 12)):
    return a + b

print(f(9, 12))
