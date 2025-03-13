from matplotlib import pyplot as plt

import numpy as np
import math

# Remove warnings.
import warnings
warnings.filterwarnings(
    "ignore",
    category=RuntimeWarning,
    message="invalid value encountered in divide"
)


def f(x):
    return (2 * x**2 - x - 1) / (x - 1)


def checkNanIndices(y_list):
    """
    Checks for NaN values in the list
    and returns the indices where NaN is present.
    
    Parameters:
    y_list (list): List of y values.
    
    Returns:
    list: Indices where NaN values are present.
    """
    nan_indices = []
    for i, y in enumerate(y_list):
        if math.isnan(y):
            nan_indices.append(i)  # Append the index where NaN is found
    return nan_indices


def createGraph(x, y):
    """
    Creates a graph with the given values.

    Parameters:
    x (array-like): X-axis values.
    y (array-like): Y-axis values.
    """
    plt.figure(figsize=(7, 5))  # Width, height.
    plt.plot(
        x,              # X-axis values.
        y,              # Y-axis values.
        color='green',  # Line color.
        marker='o',     # Marker type.
        linewidth=1,    # Line width.
        label=r"$f(x) = \frac{2x^{2} - x - 1}{x - 1}$"
    )
    # Check and plot indeterminate form.
    nan_indices = checkNanIndices(y)
    for index in nan_indices:
        plt.axvline(
            x[index],
            color='red',
            linestyle='dashed',
            label=f"Indeterminate form"
        )
    plt.title(r"$f(x) = \frac{2x^{2} - x - 1}{x - 1}$")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.legend()  # Add "defined" legends.
    plt.savefig("../images/limit-fx-01.png")
    plt.show()


if __name__ == '__main__':

    x = np.linspace(-2, 5)  # Generate points to from -2 to 5.
    y = f(x)                # Compute the corresponding y values.

    # Print x and y values.
    for xi, yi in zip(x, y):
        print(f"x: {xi:.4f}, y: {yi:.4f}")

    createGraph(x, y)
