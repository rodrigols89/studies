import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
isNullSum = data.isnull().sum()

print(isNullSum)
