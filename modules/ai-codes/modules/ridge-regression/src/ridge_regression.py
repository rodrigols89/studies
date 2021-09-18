from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from matplotlib import pyplot as plt
import pandas as pd

# Settings
pd.set_option('display.max_columns', 21)
df = pd.read_csv('../datasets/kc_house_data.csv')
df = df.drop(['id', 'date', 'zipcode', 'lat', 'long'], axis=1)
y = df['price']
x = df.drop(['price'], axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=14)

# Linear Regression
model = LinearRegression()
model.fit(x_train, y_train)
r2 = model.score(x_test, y_test)
print('Coeficiente de Determinação R^2 para o Algoritmos de Regressão Linear: {0}'.format(r2))

# Ridge Regression
ridgeModel = Ridge(alpha=1.0) # Alpha = Learning Rate.
ridgeModel.fit(x_train, y_train)
ridgeR2 = ridgeModel.score(x_test, y_test)
print('Coeficiente de Determinação R^2 para o Algoritmos Ridge Regression: {0}'.format(ridgeR2))
