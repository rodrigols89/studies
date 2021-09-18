from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import ElasticNet
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
linearRegressionModel = LinearRegression()
linearRegressionModel.fit(x_train, y_train)
r2 = linearRegressionModel.score(x_test, y_test)
print('Coeficiente de Determinação R^2 para o Algoritmos de Regressão Linear: {0}'.format(r2))

# Lasso Regression - L1
lassoModel = Lasso(alpha=10, max_iter=1000, tol=0.1)
lassoModel.fit(x_train, y_train)
lassoR2 = lassoModel.score(x_test, y_test)
print('Coeficiente de Determinação R^2 para o Algoritmos Ridge Regression - L1/Lasso: {0}'.format(lassoR2))

# Ridge Regression - L2
ridgeModel = Ridge(alpha=10)
ridgeModel.fit(x_train, y_train)
ridgeR2 = ridgeModel.score(x_test, y_test)
print('Coeficiente de Determinação R^2 para o Algoritmos Ridge Regression - L2: {0}'.format(ridgeR2))

# Elastic Net
elasticNetModel = ElasticNet(alpha=1, l1_ratio=0.5, tol=0.3)
elasticNetModel.fit(x_train, y_train)
elasticNetR2 = elasticNetModel.score(x_test, y_test)
print('Coeficiente de Determinação R^2 para o Algoritmos Elastic Net: {0}'.format(elasticNetR2))
