import numpy as np

# Newton method
def derive(f, x):
    eps = 10e-09
    return (f(x + eps) - f(x - eps))/(2 * eps)


def newton_method(function, x0, n):
    global x_list
    global y_list
    counter = 0
    x_list = []
    y_list = []
    while counter < n:
        # in this case x1 would be x0 and vice versa
        x1 = x0
        x0 = x0 - function(x0)/derive(function, x0)
        y = function(x1) + (x0 - x1) * derive(function, x0)
        counter += 1
        x_list.append(x0)
        y_list.append(y)
    return x0

# 42069 function - meme


def f(x):
    return x**2 - 489 * x + 28980


N69 = newton_method(f, 1, 20)
N420 = newton_method(f, 1000, 20)

print(N69, N420)

