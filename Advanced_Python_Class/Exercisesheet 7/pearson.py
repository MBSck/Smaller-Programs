import numpy as np
# The pearson correlation coefficient

__name__ = "__pearson__"


def generate_x_y_gaussians(size):
    """Generates two gaussian lists for both x and y coordiantes, respectively"""
    x_list = np.random.normal(0, 1, size=size)
    y_list = np.random.normal(0, 1, size=size)
    return x_list, y_list


def mean(input_list):
    """Calculates the mean function"""
    return np.sum(input_list) / len(input_list)


def correlation_mat(input_list_x, input_list_y):
    """Basic correlation of two variables. This is the correlation matrix"""
    input_list_x, input_list_y = np.array(input_list_x), np.array(input_list_y)
    factor = 1/(len(input_list_x) - 1)
    return factor*(input_list_x-mean(input_list_x))*(input_list_y-mean(input_list_y))


def pearson_coefficient(input_list_x, input_list_y):
    """Describes the correlation between two variables,
    +1 if positive correlation, -1 if negative and 0 if no correlation"""

    input_list_x, input_list_y = np.array(input_list_x), np.array(input_list_y)

    pearson_function = correlation_mat(input_list_x, input_list_y) / \
                       np.sqrt(correlation_mat(input_list_x, input_list_x) * correlation_mat(input_list_y, input_list_y))
    return np.sum(pearson_function)/len(input_list_x)


if __name__ == "__pearson__":
    pass
