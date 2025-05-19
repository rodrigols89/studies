def createRegression(samples, variavel_numbers, n_noise):
  from sklearn.datasets import make_regression
  x, y = make_regression(n_samples=samples, n_features=variavel_numbers, noise=n_noise)
  return x, y

if __name__ =='__main__':
  from matplotlib import pyplot as plt

  reg = createRegression(200, 1, 30)

  plt.figure(figsize=(10, 7))
  plt.scatter(*reg)
  plt.title('Linear Regression Sample with Scikit-Learn')
  plt.savefig('../images/plot-04.png', format='png')
  plt.show()
