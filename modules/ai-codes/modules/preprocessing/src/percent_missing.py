import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
percentMissing = (data.isnull().sum() / len(data['ID'])) * 100

print(percentMissing)
