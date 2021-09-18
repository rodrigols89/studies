import matplotlib.pyplot as plt

def angular_a(x):
  return 2 * x

def linear_b(x):
  return 2 * x + 3

if __name__ =='__main__':
  x = [1, 2, 3, 4]
  y_angular = []
  y_linear  = []

  for xs in x:
    y_angular.append(angular_a(xs))

  for xs in x:
    y_linear.append(linear_b(xs))
  
  plt.plot(x, y_angular, x, y_linear, marker='o')
  plt.legend(['f(x) = 2x', 'f(x) 2x + 3'])
  plt.title('Diferença entre coeficientes Angular & Linear')
  plt.xlabel('Eixo - X')
  plt.ylabel('Eixo - Y')
  plt.axis([0, 15, 0, 15])
  plt.grid()
  plt.savefig('../images/plot-04.png', format='png')
  plt.show()
