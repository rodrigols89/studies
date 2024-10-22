def r(x):
  return (x)**2 + x

if __name__ =='__main__':
  from matplotlib import pyplot as plt
  import numpy as np

  x = np.array(range(0, 10+1))

  # Secant representation.
  s = np.array([0, 10])

  plt.figure(figsize=(10, 7))
  plt.plot(x, r(x), color='green', marker='o')
  plt.plot(s, r(s), color='magenta', marker='x') # Add secant line.
  plt.title("r(x) = x^2 + x")
  plt.xlabel('Seconds')
  plt.ylabel('Meters')
  plt.grid()
  plt.savefig("../images/plot-03.png", format='png')
  plt.show()
