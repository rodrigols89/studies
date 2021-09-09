def f(x):
  return 1 / x

if __name__ =='__main__':
  from matplotlib import pyplot as plt
  import pandas as pd

  df = pd.DataFrame ({'x': range(-10, 10+1)}) # x Values.
  df['y'] = f(df['x']) # y Values.

  print(df)

  plt.figure(figsize=(10, 10))
  plt.plot(df.x, df.y, color="b", marker='o')
  plt.title('f(x) = 1 / x')
  plt.xlabel('x')
  plt.ylabel('y = f(x)')
  plt.grid()
  plt.xticks(range(-10, 10+1, 1))
  plt.yticks(range(-5, 5+1, 1))
  plt.axhline()
  plt.axvline()
  plt.savefig('../images/plot-03.png', format='png')
  plt.show()
