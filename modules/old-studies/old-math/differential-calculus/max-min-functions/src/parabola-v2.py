def y(x):
  return -x**2

if __name__ =='__main__':
  from matplotlib import pyplot as plt
  import pandas as pd

  df = pd.DataFrame({'x': range(-10, 10+1)})
  df['y'] = [y(x) for x in df.x]

  print(df)

  plt.figure(figsize=(10, 7))
  plt.plot(df.x, df.y, color='blue', marker='o')
  plt.title('y = -x^2')
  plt.xlabel('x')
  plt.ylabel('-x^2')
  plt.grid()
  plt.savefig("../images/plot-02.png", format='png')
  plt.show()
