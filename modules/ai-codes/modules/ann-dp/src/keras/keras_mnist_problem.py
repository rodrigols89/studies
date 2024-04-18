import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from keras.datasets import mnist
from keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = mnist.load_data()

"""
The "X" independents variables are Matrices of pixels 28x28.
28 = height (Altura).
28 = width (Largura).
"""
# print(x_train.shape)  # (60000, 28, 28) = 60000 images (matrices) 28x28 pixels.
# print(x_test.shape)   # (10000, 28, 28) = 10000 images (matrices) 28x28 pixels.


"""
The "y" dependent variables are the labels of 10 classes (0 to 9).
"""
# print(y_train.shape)  # (60000,) = 60000 samples.
# print(y_test.shape)   # (10000,) = 10000 samples.


"""
Apply One-Hot Encoding to the dependent (y target) variable.
"""
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
# print("------------------------------")
# print("|0, 1, 2, 3, 4, 5, 6, 7, 8, 9|")
# print("------------------------------")
# for i in range(50):
#    print(y_train[i])


"""
Reshape the independent (x) variables.

This is because the Conv2D layer expects:
 - The input (x): Independent Variables.
 - The image dimensions:
   - height = 28.
   - width = 28.
   - Color pattern (channels) = 1 (Gray Scale).

That is, we just add a new dimension to the Matrix
with the value of 1.
"""
x_train = x_train.reshape(60000, 28, 28, 1)
x_test = x_test.reshape(10000, 28, 28, 1)
# print(x_train.shape)  # (60000, 28, 28, 1).
# print(x_test.shape)   # (10000, 28, 28, 1).
