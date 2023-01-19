########################################################
# Rodrigo Leite da Silva - drigols                     #
# Last update: 2022/12/22                              #
########################################################

import pandas as pd

df = pd.DataFrame(
    {
        'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
        'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000],
        'Hours':[41, 40, 36, 30, 35, 39, 40],
        'Grade':[50, 50, 46, 95, 50, 5,57]
    }
)

# Create a list to represents the DataFrame columns/labels.
numcols = ['Salary', 'Hours', 'Grade']

# Iterate for each DataFrame column/label and print the range.
for col in numcols:
    print(df[col].name + ' range: ' + str(df[col].max() - df[col].min()))
