########################################################
# Rodrigo Leite - drigols                              #
# Last update: 04/10/2021                              #
########################################################

from sklearn.datasets import load_breast_cancer
import pandas as pd

pd.set_option('display.max_columns', 30)

df = load_breast_cancer() # Dataset instance.

x = pd.DataFrame(df.data, columns=[df.feature_names])
y = pd.Series(df.target)

print(x.head(10))
print("Target values:\n", y.head(50))
print("Dataframe shape: {0}\nTarget variable shape: {1}".format(x.shape, y.shape))
