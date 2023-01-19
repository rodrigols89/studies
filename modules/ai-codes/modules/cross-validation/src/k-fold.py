from sklearn.model_selection import cross_val_score # Cross Validation Function.
from sklearn.model_selection import KFold # K-Fold Class.
from sklearn.linear_model import LinearRegression # Linear Regression class.

import pandas as pd


df = pd.read_csv("../datasets/Admission_Predict.csv")
df.drop('Serial No.', axis = 1, inplace = True)

x = df.drop('Chance of Admit ', axis = 1)
y = df['Chance of Admit ']

model  = LinearRegression()
kfold  = KFold(n_splits=5, shuffle=True) # shuffle=True, Shuffle (embaralhar) the data.
result = cross_val_score(model, x, y, cv = kfold)

print("K-Fold (R²) Scores: {0}".format(result))
print("Mean R² for Cross-Validation K-Fold: {0}".format(result.mean()))
