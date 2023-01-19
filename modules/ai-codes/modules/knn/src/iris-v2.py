########################################################
# Rodrigo Leite - drigols                              #
# Last update: 31/10/2021                              #
########################################################

from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()

x = pd.DataFrame(iris.data, columns=[iris.feature_names])
y = pd.Series(iris.target)

print("Load Iris dataset:\n", iris)
