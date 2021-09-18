# Remove Warnings.
import warnings
warnings.filterwarnings('ignore')

# Useful Libraries.
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
x = pd.DataFrame(iris.data, columns=[iris.feature_names])
y = pd.Series(iris.target)

# print(x.head(10))
# print(y.value_counts())
# print(y.head(150))

import keras
from keras.utils import np_utils

y_one_hot_encoded = np_utils.to_categorical(y) # Apply One Hot Encoding.
# print(y_one_hot_encoded)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y_one_hot_encoded, test_size=0.3)

from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential()

model.add(Dense(10, input_dim=4, kernel_initializer='normal', activation='relu'))
model.add(Dense(3, kernel_initializer='normal', activation='softmax'))

from keras.optimizers import SGD
optmizer_nn = SGD()

model.compile(loss='categorical_crossentropy', optimizer=optmizer_nn, metrics=['acc']) # "acc" is accuracy metrics.
model.fit(x_train, y_train, epochs=1000, batch_size=105, validation_data=(x_test, y_test), verbose=0)

predict = model.predict(x_test)
# print(x_test.shape)
# print(predict)

import numpy as np
np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
print(x_test.shape)
print(predict)
