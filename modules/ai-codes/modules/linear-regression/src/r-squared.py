"""
R-Squared or Coefficient of Determination
"""

def createRegression(samples,variavel_numbers, n_noise):
  from sklearn.datasets import make_regression
  x, y = make_regression(n_samples=samples, n_features=variavel_numbers, noise=n_noise)
  return x, y

if __name__ =='__main__':

  from sklearn.linear_model import LinearRegression
  from sklearn.model_selection import train_test_split
  from matplotlib import pyplot as plt

  reg = createRegression(200, 1, 30)
  model = LinearRegression()

  x_train, x_test, y_train, y_test = train_test_split(reg[0], reg[1], test_size=0.30)
  model.fit(x_train, y_train)

  # Coefficient of Determination: R^2 / R-Squared.
  r2 = model.score(x_test, y_test)
  print('Coefficient of Determination: R^2: {0}'.format(r2))
