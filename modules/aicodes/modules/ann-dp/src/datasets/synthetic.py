#####################################################################
# Programmatically generated data (Dados gerados programaticamente) #
#####################################################################

import matplotlib.pyplot as plt
import numpy as np


def spiral_data(samples, classes):
    X = np.zeros((samples*classes, 2))
    y = np.zeros(samples*classes, dtype='uint8')
    for class_number in range(classes):
        ix = range(samples*class_number, samples*(class_number+1))
        r = np.linspace(0.0, 1, samples)
        t = np.linspace(
            class_number*4,
            (class_number+1)*4,
            samples
        ) + np.random.randn(samples)*0.2
        X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
        y[ix] = class_number
    return X, y



if __name__ == '__main__':

    X, y = spiral_data(samples=100, classes=3)
    plt.scatter(X[:,0], X[:,1])
    plt.show()
