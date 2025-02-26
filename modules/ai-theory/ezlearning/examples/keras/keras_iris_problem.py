import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

from keras.models import Sequential
from keras.optimizers import SGD
from keras.utils import to_categorical
from keras.layers import Dense

import pandas as pd
import numpy as np

# Dataset Preprocessing.
iris = load_iris()
x = pd.DataFrame(iris.data, columns=[iris.feature_names])
y = pd.Series(iris.target)
y_one_hot_encoded = to_categorical(y)  # Apply One Hot Encoding.
x_train, x_test, y_train, y_test = train_test_split(x, y_one_hot_encoded, test_size=0.3)

model = Sequential()

# Add Dense Layers to the Sequential model.
model.add(Dense(units=10, input_dim=4, kernel_initializer="normal", activation="relu"))
model.add(Dense(units=3, kernel_initializer="normal", activation="softmax"))

optmizer_nn = SGD()  # Stochastic Gradient Descent Optimizer.

model.compile(
    loss="categorical_crossentropy",
    optimizer=optmizer_nn,
    metrics=["acc"],  # "acc" is accuracy metrics.
)

# Training the model.
model.fit(
    x_train,
    y_train,
    epochs=1000,
    batch_size=105,
    validation_data=(x_test, y_test),
    verbose=1,
    shuffle=True,
)

# Predict with testing data.
predict = model.predict(x_test)
np.set_printoptions(formatter={"float": lambda x: "{0:0.2f}".format(x)})
print(x_test.shape)
print(predict)
