import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

(x_train, y_train), (x_test, y_test) = \
    tf.keras.datasets.mnist.load_data()

# Convert integer into floats
x_train = tf.convert_to_tensor(x_train, dtype=tf.float32)

# Substract the mean
mn = tf.reduce_mean(x_train, axis=0)
V = x_train-mn

# Flatten each picture as a single array
V = tf.reshape(V, shape=(60000, 28*28))

sigma = tf.matmul(tf.transpose(V), V)

# We extract the eigenvalues and eigenvectors
eigs, O = tf.linalg.eigh(sigma)

# The eigenvectors are stored as columns of the matrix O
eigv = tf.transpose(O)

# The dominant eigenvectors are stored in the reverse order
eigv = tf.reverse(eigv, axis=[0])

for i in range(8):
    plt.imshow(
        eigv[i].numpy().reshape(28, 28),
        cmap="Greys")
    plt.show()

projections = tf.matmul(eigv[:50], tf.transpose(V))

# The projections are effectively the compressed pictures, the original information 60000*28*28
# Is now compressed in 60000*50
# We can see how wellthe pictures are compressed by projecting them back in the original 28*28 subspace

projected_pictures = tf.matmul(tf.transpose(projections), eigv[:50])

# and by adding back the mean to them that we originally subtracted

projected_pictures = mn + tf.reshape(projected_pictures, (60000, 28, 28))

# Plot the pictures

for i in range(8):
    plt.imshow(projected_pictures[i].numpy(), cmap="Greys")
    plt.show()
    plt.imshow(x_train[i].numpy(), cmap="Greys")
    plt.show()


