def f(x):
  return x**2

if __name__ =='__main__':
  from matplotlib import pyplot as plt
  import pandas as pd

  df = pd.DataFrame ({'x': range(-4, 4+1)}) # x values.
  df['y'] = f(df['x']) # y values.

  print(df)

  plt.figure(figsize=(10, 10))
  plt.plot(df.x, df.y, color="b", marker='o')
  plt.title('f(x) = x^2')
  plt.xlabel('x')
  plt.ylabel('y = x^2')
  plt.grid()
  plt.xticks(range(-16+1, 16+1, 1))
  plt.yticks(range(0, 16+1, 1))
  plt.axhline()
  plt.axvline()
  plt.savefig('../images/plot-01.png', format='png')
  plt.show()
