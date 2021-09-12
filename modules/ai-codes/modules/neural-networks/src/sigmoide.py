def f(x):
  from math import e
  return (1)/(1 + (e**-x))

if __name__ =='__main__':
  from matplotlib import pyplot as plt
  import pandas as pd

  df = pd.DataFrame({'x': range(-20, 20+1)})
  df['y'] = [f(n) for n in df.x]

  print(df)

  plt.figure(figsize=(15, 10))
  plt.title('Sigmoid Function')
  plt.xlabel('X')
  plt.ylabel('y = (1)/(1 + (e**-x))')
  plt.xticks(range(-20, 20+1, 1))
  plt.yticks(range(-20, 20+1, 1))
  plt.axhline()
  plt.axvline()
  plt.grid()
  plt.plot(df.x, df.y, color='green', marker='o')
  plt.savefig('../images/sigmoid-01.png', format='png')
  plt.show()
