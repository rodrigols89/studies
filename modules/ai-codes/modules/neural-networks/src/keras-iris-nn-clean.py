# Remove Warnings.
import warnings
warnings.filterwarnings('ignore')

# Imports - Useful Libraries.
from sklearn.model_selection import train_test_split
from keras.layers import Dense, Activation
from sklearn.datasets import load_iris
from keras.models import Sequential
from keras.optimizers import SGD
from keras.utils import np_utils
import pandas as pd
import numpy as np
import keras

# Dataset Preprocessing.
iris = load_iris()
x = pd.DataFrame(iris.data, columns=[iris.feature_names])
y = pd.Series(iris.target)
y_one_hot_encoded = np_utils.to_categorical(y) # Apply One Hot Encoding.
x_train, x_test, y_train, y_test = train_test_split(x, y_one_hot_encoded, test_size=0.3)

# Create Neural Network/+Layers
model = Sequential()
model.add(Dense(10, input_dim=4, kernel_initializer='normal', activation='relu'))
model.add(Dense(3, kernel_initializer='normal', activation='softmax'))

# Optimizes the Neural Network | Stochastic Gradient Descent (SGD)
optmizer_nn = SGD()

# Training Model.
model.compile(loss='categorical_crossentropy', optimizer=optmizer_nn, metrics=['acc']) # "acc" is accuracy metrics.
model.fit(x_train, y_train, epochs=1000, batch_size=105, validation_data=(x_test, y_test), verbose=1)

# Predict with testing data.
predict = model.predict(x_test)
np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
print(x_test.shape)
print(predict)
