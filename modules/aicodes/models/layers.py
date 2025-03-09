import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import numpy as np
import tensorflow as tf

from modules.ai_codes.datasets import spiral_data

class Layer_np_Dense:

    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))


    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases




class Layer_tf_Dense:

    def __init__(self, n_inputs, n_neurons):
        self.weights = tf.Variable(0.01 * tf.random.normal((n_inputs, n_neurons)))
        self.biases = tf.Variable(tf.zeros((1, n_neurons)))


    def forward(self, inputs):
        self.output = tf.tensordot(selfinputs, tf.transpose(self.weights), axes=1) + self.biases




if __name__ == "__main__":

    X, y = spiral_data(samples=100, classes=3)

    NPLayer = Layer_np_Dense(2, 3)
    print("Weights:\n", NPLayer.weights)
    print("\nBiases:\n", NPLayer.biases)
    print("\nLayer Output:\n", NPLayer.output)

    TFLayer = Layer_tf_Dense(2, 3)
    print("\nWeights:\n", TFLayer.weights.numpy())
    print("\nBiases:\n", TFLayer.biases.numpy())
    print("\nLayer Output:\n", TFLayer.output.numpy())
