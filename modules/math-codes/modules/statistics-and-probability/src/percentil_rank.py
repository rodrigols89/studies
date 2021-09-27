import pandas as pd
from scipy import stats

df = pd.DataFrame({
  'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
  'Salary':[50000,54000,50000,189000,55000,40000,59000],
  'Hours':[41,40,36,30,35,39,40],
  'Grade':[50,50,46,95,50,5,57]
  })

print(stats.percentileofscore(df['Grade'], 50, 'rank'))
