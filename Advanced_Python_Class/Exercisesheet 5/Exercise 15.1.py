"""The function will stay positive as exp always returns a positive value
That doesn't change for 0 or infinity, so we will only look at the positive cases, as we divide by all exp as well.
It will return some value between zero and one in all cases"""

"""converges against 1/n"""

"""Can be used for the temperature in thermodynamics, especially laser"""

"""You can calculate 'temperature' of finance market, f_n money for one person. If temp goes to infinity
it is the same liklyhood that you pick the richest and the poorest person with the same.

At zero it is the maxima you find"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.01)


def f(x):
    sum_exp = 0
    for i in x:
        sum_exp += np.exp(x)
    return np.exp(x)/sum_exp


plt.plot(x, f(x))
plt.show()
