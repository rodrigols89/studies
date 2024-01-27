import numpy as np
import matplotlib.pyplot as plt

def create_graph(axes_x, axes_y):
  plt.plot(axes_x, axes_y)
  plt.title("Square Function")
  plt.xlabel("x")
  plt.ylabel("y = x**2")
  plt.grid(True)
  plt.savefig('../images/fig-05.png', format='png')
  plt.show()

if __name__ =='__main__':
  x = np.linspace(-2, 2, 500)
  y = x**2
  create_graph(x, y)
