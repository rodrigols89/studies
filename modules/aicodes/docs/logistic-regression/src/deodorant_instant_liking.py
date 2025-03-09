########################################################
# Rodrigo Leite - drigols                              #
# Last update: 04/10/2021                              #
########################################################

def missing_data_percent(df):
  missing = df.isna().sum()
  missing_percent = ( missing / len(df['Product']) ) * 100
  print("\nMissing data percent (%): \n", missing_percent)

if __name__=="__main__":

  from sklearn.linear_model import LogisticRegression
  from sklearn.model_selection import cross_val_score
  from sklearn.model_selection import StratifiedKFold

  import pandas as pd
  pd.set_option('display.max_columns', 64)
  pd.set_option('display.max_rows', 64)

  df = pd.read_csv('../datasets/data_train_reduced.csv')
  # print(df.head(10))
  # print(df.shape)
  # print(df.dtypes)

  missing_data_percent(df)

  # Drop Missing data > 20%
  df.drop(['q8.2','q8.8','q8.9','q8.10','q8.17','q8.18','q8.20'], axis=1, inplace=True)

  # Remove others unuseful columns (variables).
  df.drop(['Respondent.ID'], axis=1, inplace=True)
  df.drop('q1_1.personal.opinion.of.this.Deodorant', axis=1, inplace=True) # Remove 100% Accuracy (Personal Opinion).

  # Replace (fill) 20% missing data per median.
  df['q8.12'].fillna(df['q8.12'].median(), inplace=True)
  df['q8.7'].fillna(df['q8.7'].median(), inplace=True)

  missing_data_percent(df)

  df.drop(['Product'], axis=1, inplace=True) # Drop column "product": ERROR Deodorant J 

  y = df['Instant.Liking']
  x = df.drop('Instant.Liking', axis=1)

  Stratified_K_Fold = StratifiedKFold(n_splits=5,)

  model = LogisticRegression(max_iter=2000)
  result= cross_val_score(model, x, y, cv= Stratified_K_Fold, )

  print('Accuracy:', result.mean())
