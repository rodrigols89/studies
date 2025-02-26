########################################################
# Rodrigo Leite - drigols                              #
# Last update: 30/09/2021                              #
########################################################

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import ElasticNet
import pandas as pd

df = pd.read_csv("../datasets/Admission_Predict.csv")
df.drop('Serial No.', axis = 1, inplace = True)
print(df.head(10))

x = df.drop('Chance of Admit ', axis=1)
y = df['Chance of Admit ']

# [Dictionary]
# - Alpha = All values I want to testing.
# - l1_ratio = All values L1 Ratio a want to testing.
values = {
  'alpha': [0.1, 0.5, 1, 2, 5 ,10, 25, 50, 100],
  'l1_ratio': [0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.8]
}

# Create ElasticNet instance.
model = ElasticNet()

# [RandomizedSearchCV function params]
# - estimator = What Machine Learning Algorithm we are using (ElasticNet,Lasso, Ridge, Linear Regression... );
# - param_grid = Receive a dictionary (alway); 
# - cv=5 = Cross-Validation + K-Fold=5 (When is a classification problem automatically is used Stratified K-Fold).
search = GridSearchCV(estimator = model, param_grid=values, cv=5)
search.fit(x, y) # Train the model.

print('Best score:', search.best_score_) # Best R².
print('Best alpha:', search.best_estimator_.alpha) # Use "." to select the "alpha" value and display the best.
print('Best L1_Ratio:', search.best_estimator_.l1_ratio) # Use "." to select the "l1_ratio" value and display the best.
