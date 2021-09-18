import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
dt = data.dropna()

print("Full sample: {0}".format(data.shape))
print("Sample without NaN: {0}".format(dt.shape))
