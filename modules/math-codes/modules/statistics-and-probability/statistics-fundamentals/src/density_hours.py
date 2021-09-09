from create_dataframe import create_df
import matplotlib.pyplot as plt
import scipy.stats as stats

if __name__ =='__main__':

  students = {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
    'Hours':[41, 40, 36, 30, 35, 39, 40]
  }

  my_df = create_df(**students)
  hours = my_df['Hours'] # Pega as horas trabalhadas por semana de cada aluno.
  density = stats.gaussian_kde(hours) # Pega a densidade das horas.

  # Cria o plot/gráfico.
  n, x, _ = plt.hist(hours, histtype='step', density=True, bins=25) # Cria o Histograma.
  plt.plot(x, density(x)*7) # Cria a linha de densidade no plot.
  plt.axvline(hours.mean(), color='magenta', linestyle='dashed', linewidth=2) # Adiciona mean() lane no plot.
  plt.axvline(hours.median(), color='green', linestyle='dashed', linewidth=2) # Adiciona median() lane no plot.
  plt.savefig('../images/plot-04.png', format='png')
  plt.show()
