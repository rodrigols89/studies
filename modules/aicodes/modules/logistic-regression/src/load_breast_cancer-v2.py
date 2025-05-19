########################################################
# Rodrigo Leite - drigols                              #
# Last update: 04/10/2021                              #
########################################################

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_breast_cancer
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 30)

df = load_breast_cancer() # Dataset instance.
x = pd.DataFrame(df.data, columns=[df.feature_names])
y = pd.Series(df.target)

C_value = np.array([0.01, 0.1, 0.5, 1, 2, 3, 5, 10, 20, 50, 100])
regularization = ['l1', 'l2']
grid_values = {'C': C_value, 'penalty': regularization}

model = LogisticRegression(max_iter=2000)

logistic_regression_grid = GridSearchCV(estimator = model, param_grid = grid_values, cv = 5)
logistic_regression_grid.fit(x, y)

print("Best Accuracy:", logistic_regression_grid.best_score_)
print("Best C value:", logistic_regression_grid.best_estimator_.C)
print("Regularization:", logistic_regression_grid.best_estimator_.penalty)

