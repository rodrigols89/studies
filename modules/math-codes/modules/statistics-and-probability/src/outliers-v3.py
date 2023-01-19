########################################################
# Rodrigo Leite - drigols                              #
# Last update: 17/12/2021                              #
########################################################

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame(
  {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
    'Salary':[50000,54000,50000,189000,55000,40000,59000],
    'Hours':[41,40,36,17,35,39,40],
    'Grade':[50,50,46,95,50,5,57]
  }
)

# Cria um plot/gráfico do tipo (kind) "box" para as notas finais dos alunos.
df['Grade'].plot(kind='box', title='Grade Distribution', figsize=(10,8))
plt.savefig('../images/first-boxplot-04.png', format='png')
plt.show()
