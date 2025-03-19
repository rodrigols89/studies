import os
import sys

# Add the root directory 'aicodes' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Hide TensorFlow warnings

import numpy as np
import tensorflow as tf

from datasets.synthetic import spiral_data
from algorithms.activations import sigmoid


class LayerDenseNP:

    def __init__(self, n_inputs, n_neurons, activation=None):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
        self.activation = activation

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
        # Aplica ativação, se houver.
        if self.activation:
            self.output = self.activation(self.output)

class LayerDenseTF:

    def __init__(self, n_inputs, n_neurons, activation=None):
        self.layer = (tf.keras.layers.Input(shape=(n_inputs,)),)
        self.layer = tf.keras.layers.Dense(n_neurons, activation=activation)
        self.activation = activation

    def forward(self, inputs):
        self.output = self.layer(inputs)


if __name__ == "__main__":

    X, y = spiral_data(samples=100, classes=3)

    # Create Dense Layer with 2 input features and 3 output values.
    np_layer = LayerDenseNP(2, 3, activation=sigmoid)
    np_layer.forward(X)
    print("---------- ( NumPy ) ----------")
    print("Weights:\n", np_layer.weights)
    print("\nBiases:\n", np_layer.biases)
    print("\nLayer Output (0-5):\n", np_layer.output[:5])

    # Create Dense Layer with 2 input features and 3 output values.
    tf_layer = LayerDenseTF(2, 3, activation=sigmoid)
    tf_layer.forward(X)
    print("\n---------- ( TensorFlow ) ----------")
    print("Weights:\n", tf_layer.layer.get_weights()[0])
    print("\nBiases:\n", tf_layer.layer.get_weights()[1])
    print("\nLayer Output (0-5):\n", tf_layer.output.numpy()[:5])
