########################################################
# Rodrigo Leite - drigols                              #
# Last update: 17/12/2021                              #
########################################################

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame(
  {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny'],
    'Grade':[50, 50, 46, 95, 50, 5,57, 42, 26, 72, 78, 60, 40, 17, 85]
  }
)

# Cria um plot/gráfico do tipo (kind) "box" para as notas finais dos alunos.
df['Grade'].plot(kind='box', title='Grade Distribution', figsize=(10,8))
plt.savefig('../images/first-boxplot-05.png', format='png')
plt.show()
