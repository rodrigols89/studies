########################################################
# Rodrigo Leite - drigols                              #
# Last update: 30/09/2021                              #
########################################################

import pandas as pd

df = pd.read_csv("../datasets/Admission_Predict.csv")
df.drop('Serial No.', axis = 1, inplace = True)
print(df.head(10))
