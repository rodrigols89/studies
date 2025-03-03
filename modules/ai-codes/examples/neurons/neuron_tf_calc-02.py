import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf

inputs = tf.constant([1.0, 2.0, 3.0, 2.5])

weights = tf.constant([
    [0.2, 0.8, -0.5, 1],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
])

biases = tf.constant([2.0, 3.0, 0.5])

layer_outputs = tf.tensordot(weights, inputs, axes=1) + biases

print(layer_outputs)
print(layer_outputs.numpy())
