def h(x):
  if x >= 0:
    import numpy as np
    return 2 * np.sqrt(x)

if __name__ =='__main__':
  from matplotlib import pyplot as plt
  import pandas as pd

  df = pd.DataFrame({'x': range(-20, 21)})
  df['y'] = [h(a) for a in df['x']]

  print(df)

  plt.title('h(x) = 2 • sqrt(x), x >= 0')
  plt.xlabel('x')
  plt.ylabel('h(x)')
  plt.grid()
  plt.plot(df.x, df.y, color='green')
  plt.plot(0, h(0), color='green', marker='o', markerfacecolor='green', markersize=10)
  plt.savefig('../images/plot-06.png', format='png')
  plt.show()
