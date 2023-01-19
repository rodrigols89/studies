########################################################
# Rodrigo Leite - drigols                              #
# Last update: 04/10/2021                              #
########################################################

if __name__=="__main__":

  from sklearn.linear_model import LogisticRegression
  from sklearn.model_selection import GridSearchCV
  import pandas as pd
  import numpy as np

  pd.set_option('display.max_columns', 64)
  pd.set_option('display.max_rows', 64)
  df = pd.read_csv('../datasets/data_train_reduced.csv')

  # Drop Missing data > 20%
  df.drop(['q8.2','q8.8','q8.9','q8.10','q8.17','q8.18','q8.20'], axis=1, inplace=True)

  # Remove others unuseful columns (variables).
  df.drop(['Respondent.ID'], axis=1, inplace=True)
  df.drop('q1_1.personal.opinion.of.this.Deodorant', axis=1, inplace=True) # Remove 100% Accuracy (Personal Opinion).

  # Replace (fill) 20% missing data per median.
  df['q8.12'].fillna(df['q8.12'].median(), inplace=True)
  df['q8.7'].fillna(df['q8.7'].median(), inplace=True)

  df.drop(['Product'], axis=1, inplace=True) # Drop column "product": ERROR Deodorant J 

  y = df['Instant.Liking']
  x = df.drop('Instant.Liking', axis=1)

  C_values = np.array([0.01, 0.1, 0.5, 1, 2, 3, 5, 10, 20, 50, 100])
  regularization = ['l1', 'l2']
  grid_values = {'C': C_values, 'penalty': regularization}

  model = LogisticRegression(max_iter=2000)

  logistic_regression_grid = GridSearchCV(estimator = model, param_grid = grid_values, cv = 5)
  logistic_regression_grid.fit(x, y)

  print("Best Accuracy:", logistic_regression_grid.best_score_)
  print("Best C value:", logistic_regression_grid.best_estimator_.C)
  print("Regularization:", logistic_regression_grid.best_estimator_.penalty)
