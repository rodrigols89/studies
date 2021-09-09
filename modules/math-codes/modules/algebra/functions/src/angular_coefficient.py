def f(x):
  return 10 * x

def create_plot(x, y):
  import matplotlib.pyplot as plt
  plt.plot(x, y, color='blue', marker='o')
  plt.title('f(x) = ax (Coeficiente Angular)')
  plt.xlabel('Eixo - X')
  plt.ylabel('Eixo - Y')
  plt.axis([0, 50, 0, 50])
  plt.grid()
  plt.savefig('../images/plot-02.png', format='png')
  plt.show()

if __name__ =='__main__':
  x = [1, 2, 3, 4]
  y = []

  for xs in x:
    y.append(f(xs))

  create_plot(x, y)
