import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({
  'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
  'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000],
  'Hours':[41, 40, 36, 30, 35, 39, 40],
  'Grade':[50, 50, 46, 95, 50, 5,57]
  })

# Cria um plot/gráfico do tipo(kind) "box" a partir das horas trabalhas dos ex-alunos.
df['Hours'].plot(kind='box', title='Weekly Hours Distribution', figsize=(10,8))
plt.savefig('../images/plot-06.png', format='png')
plt.show()
