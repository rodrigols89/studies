from matplotlib import pyplot as plt
from math import e

import pandas as pd
import numpy as np


def sigmoid(x):
    return 1 / (1 + (e**-x))


def relu(inputs):
    return np.maximum(0, inputs)


if __name__ == "__main__":

    # Sigmoid Function.
    df_sigmoid = pd.DataFrame({"x": range(-20, 20 + 1)})
    df_sigmoid["y"] = [sigmoid(x) for x in df_sigmoid.x]

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
    plt.savefig("../docs/ann-dp/images/sigmoide-plot-01.png")
    plt.show()

    # ReLU Function.
    df_relu = pd.DataFrame({"x": range(-20, 20 + 1)})
    df_relu["y"] = [relu(x) for x in df_relu.x]

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
    plt.savefig("../docs/ann-dp/images/relu-plot-01.png")
    plt.show()
