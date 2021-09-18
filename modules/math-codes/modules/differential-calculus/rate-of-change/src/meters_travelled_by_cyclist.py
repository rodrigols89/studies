def q(x):
  return 2 * x + 1

if __name__ =='__main__':
  from matplotlib import pyplot as plt
  import numpy as np

  x = np.array(range(0, 10+1))

  plt.figure(figsize=(10, 7))
  plt.plot(x, q(x), color='green', marker='o')
  plt.title("q(x) = 2x + 1")
  plt.xlabel('Seconds')
  plt.ylabel('Meters')
  plt.xticks(range(0, 10+1, 1))
  plt.yticks(range(0, 21+1, 1))
  plt.grid()
  plt.savefig("../images/plot-01.png", format='png')
  plt.show()
