import matplotlib.pyplot as plt
import numpy as np


def derive(f, x):
    eps = 10e-09
    return (f(x + eps) - f(x - eps))/(2 * eps)


def newton_method(function, x0, n):
    counter = 0
    x_list = []
    y_list = []
    while counter < n:
        x1 = x0
        x0 = x0 - function(x0)/derive(function, x0)
        y = function(x1) + (x0 - x1) * derive(function, x0)
        counter += 1
        x_list.append(x0)
        y_list.append(y)
    return x0, x_list, y_list


if __name__ == "__main__":
    def f(x):
        return x * np.exp(-x**2) + 1/4


    new = newton_method(f, -0, 30)
    print(new[1][-1])

    x = new[1]
    f_list = []
    for i in new[1]:
        f_list.append(f(i))
    y1 = new[2]
    y2 = f_list

    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.show()

# The newton method fails to converge is that if the tangent line on the guess point doesnt cut the x-axis, then
# no new guess will be made and at no point the x-axis will be cut and a solution won't be found.
