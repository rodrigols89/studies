def f(x):
  return x**2

if __name__ =='__main__':
  from matplotlib import pyplot as plt
  import pandas as pd

  df = pd.DataFrame({'x': range(-10, 10+1)}) # x Values.
  df['y'] = [f(x) for x in df.x] # y Values.

  print(df)

  plt.figure(figsize=(10, 10))
  plt.plot(df.x, df.y, color='blue', marker='o')
  plt.title("f(x) = x^2")
  plt.xlabel('x')
  plt.ylabel('x^2')
  plt.xticks(range(-10, 10+1, 1))
  plt.yticks(range(0, 100+1, 5))
  plt.grid()
  plt.savefig("../images/plot-01.png", format='png')
  plt.show()
