# also possible as class

# x0 can be zero of the derivative and then can be dividing by zero
# am besten ableitung hardcoden falls möglich in Anwendungen, bzw. optimierte varianten verwenden
# Analytische Genauigkeit ist mathematische Genauigkeit


'''
class Derivative:
    def __init__(self, function, epsilon=10e-09):
        self.f = function
        self.eps = epsilon
    def __call__(self, x):
        return (self.f(x + self.eps) -
                self.f(x + self.eps))/(2 * self.eps)
'''


# newton converges quadratically to the root faster than the bisection method


import matplotlib.pyplot as plt


def derive(f, x):
    eps = 10e-09
    return (f(x + eps) - f(x - eps))/(2 * eps)


def newton_method(function, x0, n):
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
    return x0, x_list, y_list


if __name__ == "__main__":
    def f(x):
        return x**2 - 3.*(x**3) + 5.*x - 1
        # return x**3 - 2. * (x**2) - 11. * x + 12


    new = newton_method(f, 0.65, 20)

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
