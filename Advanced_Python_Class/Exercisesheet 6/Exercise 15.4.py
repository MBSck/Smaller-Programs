import tensorflow as tf
import numpy as np

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = tf.cast(x_train.reshape(60000, 784), dtype=tf.float32)
x_test = tf.cast(x_test.reshape(10000, 784), dtype=tf.float32)

y_train_softmax = np.zeros(shape=(60000, 10), dtype=np.float32)
y_test_softmax = np.zeros(shape=(10000, 10), dtype=np.float32)

for i in range(10):
    y_train_softmax[np.where(y_train == i), i] = 1
    y_test_softmax[np.where(y_test == i), i] = 1

y_train_softmax = tf.convert_to_tensor(y_train_softmax)
y_test_softmax = tf.convert_to_tensor(y_test_softmax)

# computes the mean
mean_pixels = tf.reduce_mean(x_train)
# computes the standard deviation
std_pixels = tf.math.reduce_std(x_train)
x_train = (x_train-mean_pixels)/std_pixels
x_test = (x_test-mean_pixels)/std_pixels
# Dividing all by max entry (in this case 255) is also acceptable for normalization

# stochastic conjugate gradiant (look up)


def setup_loss_function(X_train, Y_train, batch_size=100):
    W = tf.Variable(initial_value=tf.ones(shape=(784, 10)))
    B = tf.Variable(initial_value=tf.ones(shape=10))

    dataset = tf.data.Dataset.from_tensor_slices(
        (X_train, Y_train)
    ).batch(batch_size).repeat(5000)
    batches = iter(dataset)

    def loss():
        X, Y = next(batches)
        return tf.reduce_sum(
            (tf.nn.softmax(tf.matmul(X, W)+B)-Y)**2
        )

    return loss, [W, B]


loss, variables = setup_loss_function(x_train, y_train_softmax)

'''
opt = tf.keras.optimizers.Adadelta(
    learning_rate=0.25,
    epsilon=0.0005)
)
'''

opt = tf.keras.optimizers.SGD(
    learning_rate=0.001
)

for i in range(5000):
    opt.minimize(loss, var_list=variables)
    if i % 50 == 0:
        print("Loss function at iteration", i, ":",
              loss().numpy())

fitted_W, fitted_B = variables
# argmax returns maximum of output and checks if it is equal to test value
print(tf.reduce_sum(
    tf.cast(
        tf.argmax(
            tf.nn.softmax(
                tf.matmul(x_test, fitted_W)
                + fitted_B),
            1) == y_test,
        tf.int16
    )
))

# output for batch_size = 10000: 28,15%
# output for batch_size = 1000: 36,16%
# output for batch_size = 100: 67,64%

# output for batch_size = 100 and learning rate 0.001: 92,63%

# output for batch_size=100 and SDG-Optimizer: 66,78%



