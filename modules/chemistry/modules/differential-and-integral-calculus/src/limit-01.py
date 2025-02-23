from matplotlib import pyplot as plt
import numpy as np

# Remove warnings.
import warnings
warnings.filterwarnings(
    "ignore",
    category=RuntimeWarning,
    message="invalid value encountered in divide"
)

def f(x):
    return (2 * x**2 - x - 1) / (x - 1)


def check_indeterminate(x, y):
    indeterminate_indices = []
    for i, (x, y) in enumerate(zip(x_list, y_list)):
        if x == 1 and y == 0:  # Example condition for indeterminate case
            indeterminate_indices.append(i)  # Add index where indeterminate occurs
    return indeterminate_indices


def createGraph(x, y):
    plt.figure(figsize=(7, 5))  # Width, height.
    plt.plot(x, f(x), color='green', marker='o', linewidth=1, label=r"$f(x) = \frac{2x^{2} - x - 1}{x - 1}$")
    plt.title(r"$f(x) = \frac{2x^{2} - x - 1}{x - 1}$")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.legend()
    plt.savefig("../images/limit-fx-01.png")
    plt.show()


if __name__ == '__main__':

    x = np.linspace(-2, 5)  # Generate points to from -2 to 5.
    y = f(x)                # Compute the corresponding y values.

    # Print x and y values.
    for xi, yi in zip(x, y):
        print(f"x: {xi:.4f}, y: {yi:.4f}")

    createGraph(x, y)
