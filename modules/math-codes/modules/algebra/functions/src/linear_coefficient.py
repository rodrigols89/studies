def f(x):
  return 2 * x + 3

def create_plot(x, y):
  import matplotlib.pyplot as plt
  plt.plot(x, y, color='blue', marker='o')
  plt.title('f(x) = ax + b (Coeficiente Linear)')
  plt.xlabel('Eixo - X')
  plt.ylabel('Eixo - Y')
  plt.axis([0, 15, 0, 15])
  plt.grid()
  plt.savefig('../images/plot-03.png', format='png')
  plt.show()

if __name__ =='__main__':
  x = [1, 2, 3, 4]
  y = []

  for xs in x:
    y.append(f(xs))

  create_plot(x, y)
