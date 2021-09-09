import pandas as pd

df = pd.DataFrame({
  'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
  'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000],
  'Hours':[41, 40, 36, 30, 35, 39, 40],
  'Grade':[50, 50, 46, 95, 50, 5,57]
  })

# Cria uma lista para representar as labels/colunas do DataFrame.
numcols = ['Salary', 'Hours', 'Grade']

# Itera pelo for e para cada label/coluna do DataFrame
# imprime os intervalos(ranges).
for col in numcols:
  print(df[col].name + ' range: ' + str(df[col].max() - df[col].min()))
