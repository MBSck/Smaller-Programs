import pearson as p
import matplotlib.pyplot as plt


x_list = [-1.6, -1.2, -0.6, 0.8, 0.2, 0.6, 2., -1.1,
          -0.9, -0.7, 0.2, 1.5, 1.2, -1.3, 7., 8.3]
y_list = [1.2, 1.4, -1.2, 0.2, 1.8, -0.2, 0.5, 1.9,
          -0.4, 0.2, 1.5, -0.7, 0.9, 1.4, 12.9, 14.1]


plt.scatter(x_list, y_list)
plt.show()

print(p.pearson_coefficient(x_list, y_list))

# Explanation: The coefficient shows a positive correlation in its value
# If you draw a line from the two spots on the top right hand corner to the left bottom hand one, you can see that
# the points at 2 and -2 lie outside of the line, which explains the not perfect correlation

# Also the dimensions of x and y are different, so it may be harder to find a fittign subset.