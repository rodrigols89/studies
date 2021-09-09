def createRegression(samples, variavel_numbers, n_noise):
  from sklearn.datasets import make_regression
  x, y = make_regression(n_samples=samples, n_features=variavel_numbers, noise=n_noise)
  return x, y

if __name__ =='__main__':

  from sklearn.linear_model import LinearRegression
  from matplotlib import pyplot as plt

  reg = createRegression(200, 1, 30)
  model = LinearRegression() # Linear Regression Instance.

  model.fit(*reg)

  a_coeff = model.coef_ # Angular Coefficient - m
  l_coeff = model.intercept_ # Linear Coefficient - b
  print('Angular Coefficient (m): {0}\nLinear Coefficient (b): {1}'.format(a_coeff, l_coeff))

  plt.figure(figsize=(10, 7))
  plt.scatter(*reg)
  plt.plot(reg[0], a_coeff*reg[0] + l_coeff,color='red')
  plt.title('Linear Regression Sample with Scikit-Learn & Line Of Best Fit')
  plt.savefig('../images/plot-05.png', format='png')
  plt.show()
