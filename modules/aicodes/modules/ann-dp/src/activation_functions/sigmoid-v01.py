import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Hide TensorFlow warnings

from matplotlib import pyplot as plt

import pandas as pd
import tensorflow as tf


def sigmoid(x):
    x = tf.convert_to_tensor(x, dtype=tf.float32)
    return tf.nn.sigmoid(x)


def relu(x):
    return tf.nn.relu(x)


def softmax(x):
    x = tf.convert_to_tensor(x, dtype=tf.float32)
    return tf.nn.softmax(x)


if __name__ == "__main__":

    # Sigmoid Function.
    df_sigmoid = pd.DataFrame({"x": range(-20, 20 + 1)})
    df_sigmoid["y"] = sigmoid(df_sigmoid["x"])

    plt.figure(figsize=(15, 5))  # Width, height.
    plt.title("Sigmoid Function")
    plt.xlabel("X")
    plt.ylabel(r"$y = \frac{1}{1 + e^{-x}}$")
    plt.xticks(range(-20, 20 + 1, 1))
    plt.yticks(range(-20, 20 + 1, 1))
    plt.axhline()
    plt.axvline()
    plt.grid()
    plt.plot(df_sigmoid.x, df_sigmoid.y, color="green", marker="o")
    plt.savefig("../../images/sigmoide-plot-01.png")
    plt.show()

    # ReLU Function.
    df_relu = pd.DataFrame({"x": range(-20, 20 + 1)})
    df_relu["y"] = relu(df_relu["x"])

    plt.figure(figsize=(15, 5))  # Width, height.
    plt.title("ReLU Function")
    plt.xlabel("X")
    plt.ylabel(r"$y = max(0, x)$")
    plt.xticks(range(-20, 20 + 1, 1))
    plt.yticks(range(-20, 20 + 1, 1))
    plt.axhline()
    plt.axvline()
    plt.grid()
    plt.plot(df_relu.x, df_relu.y, color="green", marker="o")
    plt.savefig("../../images/relu-plot-01.png")
    plt.show()

    # Softmax Function.
    df_softmax = pd.DataFrame({"x": range(-20, 20 + 1)})
    df_softmax["y"] = softmax(df_softmax["x"])

    plt.figure(figsize=(15, 5))  # Width, height.
    plt.title("Softmax Function")
    plt.xlabel("X")
    plt.ylabel(r'$S_{i,j} = \frac{e^{z_{i,j}}}{\sum_{l=1}^{L} e^{z_{i,j}}}$')
    plt.xticks(range(-20, 20 + 1, 1))
    plt.yticks(range(-20, 20 + 1, 1))
    plt.axhline()
    plt.axvline()
    plt.grid()
    plt.plot(df_softmax.x, df_softmax.y, color="green", marker="o")
    plt.savefig("../../images/softmax-plot-01.png")
    plt.show()
