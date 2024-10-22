def r(x):
    return x**2 + x

if __name__ =='__main__':
  from matplotlib import pyplot as plt
  import pandas as pd

  df = pd.DataFrame({'x': range(0, 10+1)})
  df['y'] = [r(x) for x in df.x]

  # Define os valores para x1 e x2 seguindo a fórmula.
  x1 = 4
  x2 = 6

  # Pega os valores correspondentes y1 e y2 da nossa função r(x)
  y1 = r(x1)
  y2 = r(x2)

  # Calcula a fórmula.
  m = (y2 - y1)/(x2 - x1)

  # Crie uma listas de valores "x" para a linha secante.
  sx = [x1, x2]

  # Use a função r(x) para obter os valores "y".
  sy = [r(y) for y in sx]

  # Exibe o DataFrame
  print(df)

  plt.figure(figsize=(10, 10))
  plt.xlabel('x')
  plt.ylabel('f(x)')
  plt.grid()
  plt.xticks(range(-10, 10+1, 1))
  plt.yticks(range(0, 120, 10))
  plt.plot(df.x, df.y, color='green')
  plt.scatter([x1,x2], [y1,y2], c='red') # Traçar os pontos do intervalo.
  plt.plot(sx, sy, color='magenta') # Plot a linha secante.
  plt.annotate('Variação média = ' + str(m),(x2, (y2+y1)/2)) # Exibir a taxa média de alteração calculada
  plt.savefig("../images/plot-04.png", format='png')
  plt.show()
