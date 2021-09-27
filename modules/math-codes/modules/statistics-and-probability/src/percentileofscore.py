import pandas as pd
from scipy import stats

df = pd.DataFrame({
  'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
  'Salary':[50000,54000,50000,189000,55000,40000,59000],
  'Hours':[41,40,36,30,35,39,40],
  'Grade':[50,50,46,95,50,5,57]
  })

# função percentileofscore() recebe como argumento:
# - A label/coluna/lista em que vamos trabalhar;
# - A nota do aluno Frederic;
# - Define a função como 'strict' - Ou seja, compara apenas com os valores menores;
# - E retorna a classificação n° percentil do valor/dado/aluno.
print(stats.percentileofscore(df['Grade'], 57, 'strict'))
