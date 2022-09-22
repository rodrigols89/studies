import pandas as pd
pd.set_option('display.max_columns', 42)

data = pd.read_csv('../datasets/2015-building-energy-benchmarking.csv')

# Exibe a média de cada coluna.
print((data.isnull().sum() / len(data['OSEBuildingID'])) * 100, '\n')

data['ENERGYSTARScore'] = data['ENERGYSTARScore'].fillna(data['ENERGYSTARScore'].median())

# Exibe a média de cada coluna depois de substituir os NaN da coluna - ENERGYSTARScore
print((data.isnull().sum() / len(data['OSEBuildingID'])) * 100)
