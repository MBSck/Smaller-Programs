# Exercise 6.1 and 6.2

""" For exercise 6.2 exercise"""
def call_counter(function):
    """Counts the calls of a function and prints it each time its called"""
    counter = 0
    def inner(*args, **kwargs):
        nonlocal counter
        counter += 1
        print("The function", function.__name__, "has been called", counter, "times")
        return function(*args, **kwargs)

    return inner
# ---------------------------------------

import time as t

def execution_time(function):
    """Counts the execution time of a function and prints it each time its called"""
    def inner(*args):
        start_t = t.time()
        result = function(*args)
        end_t = t.time()
        print("The function", function.__name__, "has been executed in", end_t-start_t, "secs.")
        return result

    return inner


# @execution_time
def fibonacci_sequence(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)


# you can force the decorator to only print out the last result, by appending the number of calls to the end.
""" Question to the Tutor: Is there a way to do this for the @execution_time segment as well? Without seperating the
print statement from the decorator?"""
fibonacci_sequence = call_counter(fibonacci_sequence)
"""The call_counter class slows down the function and if needed could also be not used, it is used to show the difference
of the calls in exercise 6.2"""
fibonacci_sequence = execution_time(fibonacci_sequence)(30)


print(fibonacci_sequence)

# Exercise 6.2 for cache

def cache(function):
    """Stores the values of a function and prints it each time its called"""
    call_map = dict()
    def inner(*args, **kwargs):
        if args not in call_map:
            call_map[args] = function(*args, **kwargs)
        return call_map[args]

    return inner


def fibonacci_sequence(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

"""Calling the function with 30 calls takes about 2 seconds without the cache function and approximately zero seconds
with it."""

fibonacci_sequence = call_counter(fibonacci_sequence)
fibonacci_sequence = cache(fibonacci_sequence)
fibonacci_sequence = execution_time(fibonacci_sequence)(30)
print(fibonacci_sequence)
