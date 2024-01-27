from matplotlib import pyplot as plt
import pandas as pd

# Importa a objeto MinMaxScale da biblioteca Scikit-Learn.
from sklearn.preprocessing import MinMaxScaler

df = pd.DataFrame(
  {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny'],
    'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000, 42000, 47000, 78000, 119000, 95000, 49000, 29000, 130000],
    'Hours':[41, 40, 36, 17, 35, 39, 40, 45, 41, 35, 30, 33, 38, 47, 24],
    'Grade':[50, 50, 46, 95, 50, 5, 57, 42, 26, 72, 78, 60, 40, 17, 85]
  })

# Cria uma instância do objeto MinMaxScaler()
scaler = MinMaxScaler()

# Normaliza os dados com o método fit_transform().
df[['Salary', 'Hours', 'Grade']] = scaler.fit_transform(df[['Salary', 'Hours', 'Grade']])

# Cria o plot/gráfico para exibir os dados normalizados.
df.plot(kind='box', title='Distribution', figsize = (10,8))
plt.savefig('../images/plot-04.png', format='png')
plt.show()
