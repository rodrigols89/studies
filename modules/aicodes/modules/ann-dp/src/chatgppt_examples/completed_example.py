import sys
import os

# Adiciona o caminho do diretório datasets ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tensorflow as tf

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Hide TensorFlow warnings

from datasets.synthetic import spiral_data

# Create a dataset with:
# 100 samples (amostras).
# 3 classes (output classes).
X, y = spiral_data(samples=100, classes=3)

# Input layer.
inputs = tf.keras.Input(shape=(2,), name="input_layer")

# Hidden layers.
hidden1 = tf.keras.layers.Dense(4, activation='sigmoid', name="hidden_layer_1")(inputs)
hidden2 = tf.keras.layers.Dense(4, activation='sigmoid', name="hidden_layer_2")(hidden1)
hidden3 = tf.keras.layers.Dense(4, activation='sigmoid', name="hidden_layer_3")(hidden2)

# Output layer size (3 classes: 0, 1, 2).
output = tf.keras.layers.Dense(3, activation='sigmoid', name="output_layer")(hidden3)

# Make the model (connect the layers).
model = tf.keras.Model(inputs=inputs, outputs=output)
