def k(x):
  import numpy as np
  if x <= 0:
    return x + 20
  else:
    return x - 100

if __name__ =='__main__':
  from matplotlib import pyplot as plt

  x1 = range(-20, 1)
  x2 = range(1, 20)

  y1 = [k(i) for i in x1]
  y2 = [k(i) for i in x2]

  plt.xlabel('x')
  plt.ylabel('k(x)')
  plt.grid()

  plt.plot(x1,y1, color='green')
  plt.plot(x2,y2, color='green')

  # Exibe um circulo no fim dos intervalos
  plt.plot(0, k(0), color='green', marker='o', markerfacecolor='green', markersize=10)
  plt.plot(0, k(0.0001), color='green', marker='o', markerfacecolor='w', markersize=10)

  plt.savefig('../images/plot-07.png', format='png')
  plt.show()
