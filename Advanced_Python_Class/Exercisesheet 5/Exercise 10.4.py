import numpy as np
import math
import matplotlib.pyplot as plt


def gradient_descent(x0, df, steps, tolerance=1e-07):
    iteration_counter = 0
    gradient_value = math.fabs(df(x0))

    while gradient_value > tolerance:
        iteration_counter += 1
        x0 = x0 - steps * df(x0)
        gradient_value = math.fabs(df(x0))

    return x0, gradient_value, iteration_counter


def f(x):
    return x*np.exp(-x**2)+1/4


def df(x):
    return (1-2*(x**2))*np.exp(-x**2)


x = np.arange(-3, 3, 0.01)

plt.plot(x, f(x))
plt.plot(x, df(x))
plt.show()

print(gradient_descent(0.1, df, 1.0))
print(gradient_descent(0.1, df, 0.3))
print(gradient_descent(0.1, df, 0.05))

