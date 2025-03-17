from matplotlib import pyplot as plt
from math import e

import pandas as pd


class ActivationFunctions:

    @staticmethod
    def sigmoid(x):
        """
        Compute the sigmoid activation function using the mathematical constant "e".

        The sigmoid function is defined as:
            sigmoid(x) = 1 / (1 + e^(-x))
        It maps any real-valued number into a value between 0 and 1 and is widely used as an
        activation function in neural networks.

        The '@staticmethod' decorator indicates that this method does not rely on any instance-specific
        data. It can be called directly from the class without needing to create an instance.
        Use a static method when the function’s behavior is independent of the class's state.

        Example usage:
            result = ActivationFunctions.sigmoid(x)

        Parameters:
            x (float): The input value for which the sigmoid function is computed.

        Returns:
            float: The sigmoid of x.

        Examples:
            >>> print(ActivationFunctions.sigmoid(0))
            0.5
            >>> print(ActivationFunctions.sigmoid(1))
            0.7310585786300049
            >>> print(ActivationFunctions.sigmoid(-1))
            0.2689414213699951
        """
        return 1 / (1 + (e**-x))


if __name__ == "__main__":

    df = pd.DataFrame({"x": range(-20, 20 + 1)})
    df["y"] = [ActivationFunctions.sigmoid(n) for n in df.x]

    plt.figure(figsize=(15, 5))  # Width, height.
    plt.title("Sigmoid Function")
    plt.xlabel("X")
    plt.ylabel(r"$y = \frac{1}{1 + e^{-x}}$")
    plt.xticks(range(-20, 20 + 1, 1))
    plt.yticks(range(-20, 20 + 1, 1))
    plt.axhline()
    plt.axvline()
    plt.grid()
    plt.plot(df.x, df.y, color="green", marker="o")
    plt.savefig("../docs/ann-dp/images/sigmoide-plot-01.png")
    plt.show()
