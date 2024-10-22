from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(
  {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny'],
    'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000, 42000, 47000, 78000, 119000, 95000, 49000, 29000, 130000],
    'Hours':[41, 40, 36, 17, 35, 39, 40, 45, 41, 35, 30, 33, 38, 47, 24],
    'Grade':[50, 50, 46, 95, 50, 5, 57, 42, 26, 72, 78, 60, 40, 17, 85]
  })

# Cria um gráfico de dispersão/Scatter Plot para comparar as Notas e os Salários.
df.plot(kind='scatter', title='Grade vs Salary', x='Grade', y='Salary')
plt.savefig('../images/plot-05.png', format='png')

# Adicione uma linha de melhor ajuste no plot/gráfico
plt.plot(np.unique(df['Grade']), np.poly1d(np.polyfit(df['Grade'], df['Salary'], 1))(np.unique(df['Grade'])))
plt.savefig('../images/plot-06.png', format='png')
plt.show()
