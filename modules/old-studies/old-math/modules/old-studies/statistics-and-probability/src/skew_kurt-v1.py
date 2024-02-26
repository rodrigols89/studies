########################################################
# Rodrigo Leite - drigols                              #
# Last update: 17/12/2021                              #
########################################################

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as stats

df = pd.DataFrame({
  'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
  'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000],
  'Hours':[41, 40, 36, 30, 35, 39, 40],
  'Grade':[50, 50, 46, 95, 50, 5, 57]
})

# Cria uma lista que vai representar os labels do nosso DataFrame:
# - Salary;
# - Hours;
# - Grade.
numcols = ['Salary', 'Hours', 'Grade'] 

# O laço for vai passar por cada item na nosssa lista de labels(numcols) fazendo o seguinte:
# - Imprimindo a assimétria (skewness);
# - Imprimindo a curtose (kurtosis);
# - Pegando a densidade da label;
# - Criando um Histograma para a label;
# - Adicionando a densidade/linha de densidade no plot/histograma.
for col in numcols:
  print(df[col].name + ' skewness: ' + str(df[col].skew())) # Imprime a Assimetria do label/coluna no laço for.
  print(df[col].name + ' kurtosis: ' + str(df[col].kurt())) # Imprime a Curtose do label/coluna no laço for.
  density = stats.gaussian_kde(df[col]) # Pega a densidade do label/coluna no laço for.
  n, x, _ = plt.hist(df[col], histtype='step', density=True, bins=25) # Cria o plot do label/coluna no laço for.
  plt.plot(x, density(x)*6) # Cria a linha de densidade do label no laço for.
  plt.show()
  print('\n')
