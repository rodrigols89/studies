def r(x):
  return x**2 + x

if __name__ =='__main__':
  from matplotlib import pyplot as plt
  import numpy as np

  x = np.array(range(0, 10+1))

  plt.figure(figsize=(10, 7))
  plt.plot(x, r(x), color='blue', marker='o')
  plt.title("r(x) = x^2 + x")
  plt.xlabel('Seconds')
  plt.ylabel('Meters')
  plt.grid()
  plt.savefig("../images/plot-02.png", format='png')
  plt.show()
