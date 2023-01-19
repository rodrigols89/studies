########################################################
# Rodrigo Leite - drigols                              #
# Last update: 22/09/2021                              #
########################################################

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
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
print('Coefficient of Determination R^2 for Linear Regression Algorithm: {0}'.format(r2))

# Ridge Regression
ridgeModel = Ridge(alpha=1.0) # Alpha = Learning Rate.
ridgeModel.fit(x_train, y_train)
ridgeR2 = ridgeModel.score(x_test, y_test)
print('Coefficient of Determination R^2 for Ridge Regression Algorithm: {0}'.format(ridgeR2))

# Lasso Regression - L1
lassoModel = Lasso(alpha=10, max_iter=1000, tol=0.1)
lassoModel.fit(x_train, y_train)
lassoR2 = lassoModel.score(x_test, y_test)
print('Coefficient of Determination R^2 for Ridge Regression (L1/Lasso) Algorithm: {0}'.format(lassoR2))
