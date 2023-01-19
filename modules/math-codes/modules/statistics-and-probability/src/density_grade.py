########################################################
# Rodrigo Leite - drigols                              #
# Last update: 17/12/2021                              #
########################################################

def create_df(**df):
  my_df = {}
  import pandas as pd
  my_df = pd.DataFrame(df)
  return my_df

if __name__ =='__main__':

  import matplotlib.pyplot as plt
  import scipy.stats as stats

  students = {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
    'Grade': [50, 50, 46, 95, 50, 5,57]
  }

  my_df = create_df(**students)
  grade = my_df['Grade'] # Pega as notas/grades de todos os alunos.
  density = stats.gaussian_kde(grade) # Pega a densidade das notas.

  # Cria o plot/gráfico.
  n, x, _ = plt.hist(grade, histtype='step', density=True, bins=25) # Cria o Histograma.
  plt.plot(x, density(x)*7.5) # Cria a linha de densidade no plot.
  plt.axvline(grade.mean(), color='magenta', linestyle='dashed', linewidth=2) # Adiciona mean() lane no plot.
  plt.axvline(grade.median(), color='green', linestyle='dashed', linewidth=2) # Adiciona median() lane no plot.
  plt.savefig('../images/density-04.png', format='png')
  plt.show()
