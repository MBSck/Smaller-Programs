import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

coord_list = [[10, 20], [17, 5], [-13, -15], [2, -2], [-18, -4],
              [3, -5], [-3, 9], [-8, 5], [-9, -9], [-2, 3]]
x_list = []
y_list = []

for i in coord_list:
    x_list.append(i[0])
    y_list.append(i[1])

# Entries are sorted for -20 to 20 in positive numbers, so that 40
# Entries can only be between 0 and 1
y_list_softmax = np.zeros(shape=(10, 40), dtype=np.float32)

for i in range(-20, 20):
    y_list_softmax[np.where(y_list == i), i+20] = 1

help(np.where)

y_list_softmax[9, 23] = 1
print(y_list_softmax[9])

y_list_softmax = tf.convert_to_tensor(y_list_softmax)


def f(x):
    return 2 - (x**2)/16


def p(x):
    return x

'''
x_list = np.array(x_list)
y_list = np.array(y_list)

plt.scatter(x_list, y_list)
plt.plot(x_list, f(x_list))
plt.plot(x_list, p(x_list))
plt.show()
'''