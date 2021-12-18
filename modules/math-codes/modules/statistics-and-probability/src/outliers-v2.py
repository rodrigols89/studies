########################################################
# Rodrigo Leite - drigols                              #
# Last update: 17/12/2021                              #
########################################################

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame(
  {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
    'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000],
    'Hours':[41, 40, 36, 17, 35, 39, 40],
    'Grade':[50, 50, 46, 95, 50, 5,57]
  }
)

# Utiliza o atributo showfliers = False - Ou seja, ignora dados discrepantes.
df['Salary'].plot(kind='box', title='Salary Distribution', figsize=(10,8), showfliers=False)
plt.savefig('../images/first-boxplot-03.png', format='png')
plt.show()
