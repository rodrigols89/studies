import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
data['Medal'] = data['Medal'].fillna('Nenhuma')

print(data['Medal'].head(10))
