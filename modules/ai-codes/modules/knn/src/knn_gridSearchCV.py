########################################################
# Rodrigo Leite - drigols                              #
# Last update: 26/10/2021                              #
########################################################

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 30)

df = load_breast_cancer() # Dataset instance.

x = pd.DataFrame(df.data, columns=[df.feature_names])
y = pd.Series(df.target)

# Normalize predict variables.
normalized = MinMaxScaler(feature_range = (0 , 1))
x_norm = normalized.fit_transform(x)

# Defining values for KNN testing (K, Math method, and "p" values for math mathods = minkowski).
k_values = np.array([3, 5, 7, 9, 11]) # K Values.
math_method = ['minkowski', 'chebyshev'] # Math methods.
p_values = np.array([1, 2, 3, 4]) # p values for math methods.
grid_values = {'n_neighbors': k_values, 'metric': math_method, 'p':p_values}

model = KNeighborsClassifier() # Instance.

knnGrid = GridSearchCV(estimator = model, param_grid = grid_values, cv=5)
knnGrid.fit(x_norm, y)

print("Best accuracy:", knnGrid.best_score_)
print("Best K value:", knnGrid.best_estimator_.n_neighbors)
print("Best Math method:", knnGrid.best_estimator_.metric)
print("Best p value:", knnGrid.best_estimator_.p)
