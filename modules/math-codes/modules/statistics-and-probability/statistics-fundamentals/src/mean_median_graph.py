from create_dataframe import create_df

if __name__ =='__main__':
  import matplotlib.pyplot as plt

  sleep_search = {
    'A': [6, 6, 7, 8, 8, 8, 9],
    'B': [6, 7, 8, 8, 12, 12, 15]
  }

  my_df = create_df(**sleep_search)
  print(my_df)

  plt.plot(my_df, marker='o')
  plt.title("Comparação entre as amostras (variáveis) A & B")
  plt.xlabel("Dias da Semana - x")
  plt.ylabel("Horas dormida - x")
  plt.legend(['A', 'B'])
  plt.savefig('../images/plot-01.png', format='png')
  plt.show()
