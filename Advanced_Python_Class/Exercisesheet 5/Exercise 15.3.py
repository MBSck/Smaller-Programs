import tensorflow as tf
import matplotlib.pyplot as plt


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

number_list = [1239, 1314, 1326, 22062, 23136, 37059, 37118, 43089, 43136]

for number in number_list:
    plt.imshow(x_train[number], cmap=plt.get_cmap("Greys"))
    plt.show()

my_guesses = [8, 7, 7, 2, 0, 0, 3, 1, 5]
counter = 0
number_correct = 0


for number in number_list:
    print(y_train[number], end=", ")
    if y_train[number] == my_guesses[counter]:
        number_correct += 1

    counter += 1


def accuracy_rate(number_of_predictions, total_number):
    return round(100 * (number_of_predictions/total_number), 2)


print(accuracy_rate(number_correct, len(number_list)))


