# Exercise 6.1

import time


def execution_time(function):
    is_executing = False

    def inner(*args, **kwargs):
        nonlocal is_executing

        if is_executing:
            return function(*args, **kwargs)
        else:
            start_time = time.time()
            is_executing = True
            result = function(*args, **kwargs)
            is_executing = False
            end_time = time.time()
            print(f"The function {function.__name__} has been executed in {str(end_time - start_time)} seconds.")
            return result

    return inner

@execution_time
def fibonacci_series(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)

print(fibonacci_series(34))