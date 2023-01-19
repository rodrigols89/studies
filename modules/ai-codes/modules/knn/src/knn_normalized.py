########################################################
# Rodrigo Leite - drigols                              #
# Last update: 25/10/2021                              #
########################################################

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

pd.set_option('display.max_columns', 30)

df = load_breast_cancer() # Dataset instance.

x = pd.DataFrame(df.data, columns=[df.feature_names])
y = pd.Series(df.target)

# Normalize predict variables.
normalized = MinMaxScaler(feature_range = (0 , 1))
x_norm = normalized.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_norm, y, test_size=0.3, random_state=16)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)

result = model.score(x_test, y_test)
print("Accuracy:", result)
