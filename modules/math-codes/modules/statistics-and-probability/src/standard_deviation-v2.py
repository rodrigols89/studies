########################################################
# Rodrigo Leite - drigols                              #
# Last update: 17/12/2021                              #
########################################################

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Cria uma distribuição normal padrão aleatória com np.random.randn() e salva no DataFrame - df:
# - Os argumentos para a função random.randn() são as dimensões: (100000, 1) = 100.000 linhas por 1 coluna.
# - columns=['Grade'] é onde armazenar os dados no df. Se não específicar o df não vai ter uma label específico.
df = pd.DataFrame(np.random.randn(100000, 1), columns=['Grade'])

grade = df['Grade'] # Pega a distribuição criada no label/coluna "Grade".
density = stats.gaussian_kde(grade) # Pega a densidade da distribuição.

n, x, _ = plt.hist(grade, color='lightgrey', density=True, bins=100) # Cria o Histograma. 
plt.plot(x, density(x)) # Adiciona a densidade/linha de densidade no plot/gráfico.

s = df['Grade'].std() # Pega o Desvio Padrão da distribuição normal padrão criada.
m = df['Grade'].mean() # Pega a média da distribuição normal padrão criada.

# Annotate 1 stdev
x1 = [m-s, m+s]
y1 = [0.25, 0.25]
plt.plot(x1,y1, color='magenta')
plt.annotate('1s (68.26%)', (x1[1],y1[1]))

# Annotate 2 stdevs
x2 = [m-(s*2), m+(s*2)]
y2 = [0.05, 0.05]
plt.plot(x2,y2, color='green')
plt.annotate('2s (95.45%)', (x2[1],y2[1]))

# Annotate 3 stdevs
x3 = [m-(s*3), m+(s*3)]
y3 = [0.005, 0.005]
plt.plot(x3,y3, color='orange')
plt.annotate('3s (99.73%)', (x3[1],y3[1]))

# Adiciona a média(mean) no plot/gráfico.
plt.axvline(grade.mean(), color='grey', linestyle='dashed', linewidth=1)
plt.show()
