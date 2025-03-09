########################################################
# Rodrigo Leite - drigols                              #
# Last update: 30/09/2021                              #
########################################################

from sklearn.model_selection import RandomizedSearchCV
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
  'alpha': [0.1, 0.5, 1, 2, 5 ,10, 25, 50, 100, 150, 200, 300, 500, 750, 1000, 1500, 2000, 3000, 5000],
  'l1_ratio': [0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 6.6, 0.7, 0.8, 0.9]
}

# Create ElasticNet instance.
model = ElasticNet()

# [RandomizedSearchCV function params]
# - estimator = What Machine Learning Algorithm we are using (ElasticNet,Lasso, Ridge, Linear Regression... );
# - param_distributions = Receive a dictionary (alway); 
# - n_iter = Iterations number = Possible combinations alpha x l1_ration = 19x11 = 209 combinations
# - cv=5 = Cross-Validation + K-Fold=5 (When is a classification problem automatically is used Stratified K-Fold).
search = RandomizedSearchCV(estimator = model, param_distributions=values, n_iter=150, cv=5, random_state=15)
search.fit(x, y) # Train the model.

print('Best score:', search.best_score_) # Best R².
print('Best alpha:', search.best_estimator_.alpha) # Use "." to select the "alpha" value and display the best.
print('Best L1_Ratio:', search.best_estimator_.l1_ratio) # Use "." to select the "l1_ratio" value and display the best.
