########################################################
# Rodrigo Leite - drigols                              #
# Last update: 17/12/2021                              #
########################################################

import pandas as pd

df = pd.DataFrame(
  {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
    'Salary':[50000,54000,50000,189000,55000,40000,59000],
    'Hours':[41,40,36,17,35,39,40],
    'Grade':[50,50,46,95,50,5,57]
  }
)

# Passa uma lista com os porcentos % que vão representar cada quartil;
# 0.25 = 25%, 0.5 = 50%, 0.75 = 75%;
# O retorno como nós sabemos vai ser a mediana de cada quartil.
print(df['Hours'].quantile([0.25, 0.5, 0.75]))
