def create_plot(x, y):
  import matplotlib.pyplot as plt

  # Exibe para cada ano "x" a temperatura média "y".
  for year, average_temp in zip(x, y):
    print("In year {0} the average New York temperature was {1}°".format(year, average_temp))

  plt.plot(x, y, marker='o')
  plt.savefig('../images/plot-03.png', format='png')
  plt.show()


if __name__ =='__main__':
  # Cria uma lista de temperatura de New York durante os anos de 2000-2012.
  nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]

  # Utiliza a função range() para criar uma lista com range predefinido - (2000-2012).
  # OBS: Lembra que a função range() nunca imprime o último elemento? Por isso de 2000-2013
  years = range(2000, 2013)

  # Cria o gráfico/plot com a função create_plot().
  create_plot(years, nyc_temp)
