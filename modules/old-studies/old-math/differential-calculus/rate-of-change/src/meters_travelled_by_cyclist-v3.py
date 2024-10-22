def r(x):
  return (x)**2 + x

if __name__ =='__main__':
  from matplotlib import pyplot as plt
  import numpy as np

  x = np.array(range(0, 10+1))

  # Secant representation - 2 to 7.
  s = np.array([2, 7])

  # Slope/Gradient calculus.
  x1 = s[0]
  y1 = r(x1)
  x2 = s[-1]
  y2 = r(x2)
  slope = (y2 - y1)/(x2 - x1)

  plt.figure(figsize=(10, 7))
  plt.plot(x, r(x), color='green', marker='o')
  plt.plot(s, r(s), color='magenta', marker='x') # Add secant line.
  plt.annotate('Average speed = ' + str(slope) + ' m/s',((x2 + x1)/2, (y2 + y1)/2)) # Add notation.
  plt.title("r(x) = x^2 + x")
  plt.xlabel('Seconds')
  plt.ylabel('Meters')
  plt.grid()
  plt.savefig("../images/plot-04.png", format='png')
  plt.show()
