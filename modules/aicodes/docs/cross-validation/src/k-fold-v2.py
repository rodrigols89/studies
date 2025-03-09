def ApplyesKFold(x_axis, y_axis):

  from sklearn.linear_model import LinearRegression, ElasticNet, Ridge, Lasso
  from sklearn.model_selection import cross_val_score, KFold

  # KFold instance and settings - shuffle=True, Shuffle (embaralhar) the data.
  kfold  = KFold(n_splits=10, shuffle=True)

  # Models instances.
  linearRegression = LinearRegression()
  elasticNet       = ElasticNet()
  ridge            = Ridge()
  lasso            = Lasso()

  # Set the axes.
  x = x_axis
  y = y_axis

  # Applyes KFold to the models.
  linearRegression_result = cross_val_score(linearRegression, x, y, cv = kfold)
  elasticNet_result       = cross_val_score(elasticNet, x, y, cv = kfold)
  ridge_result            = cross_val_score(ridge, x, y, cv = kfold)
  lasso_result            = cross_val_score(lasso, x, y, cv = kfold)

  # Creates a dictionary to store Linear Models.
  dic_models = {
    "LinearRegression": linearRegression_result.mean(),
    "ElasticNet": elasticNet_result.mean(),
    "Ridge": ridge_result.mean(),
    "Lasso": lasso_result.mean()
  }
  # Select the best model.
  bestModel = max(dic_models, key=dic_models.get)
  
  # Print models scores and the best model.
  models_cores = f'''
  Mean of the R² for : {linearRegression_result.mean()}
  Mean of the R² for Elastic Net Mean (R^2): {elasticNet_result.mean()}
  Mean of the R² for Ridge Mean: {ridge_result.mean()}
  Mean of the R² for Lasso Mean: {lasso_result.mean()}
  The best model is: {bestModel} with R² value: {dic_models[bestModel]}
  '''
  print(models_cores)


if __name__ =='__main__':

  import pandas as pd

  df = pd.read_csv("../datasets/Admission_Predict.csv")
  df.drop('Serial No.', axis = 1, inplace = True)

  x = df.drop('Chance of Admit ', axis = 1)
  y = df['Chance of Admit ']

  ApplyesKFold(x, y)
