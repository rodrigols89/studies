import pandas as pd

# Cria um dataframe com uma coluna "x" com valores de -10 a 10.
df = pd.DataFrame ({'x': range(-10, 10+1)})

# Cria uma segunda coluna contendo para cada valor de "x" a nossa equação: 3*x - 4 / 2.
df['y'] = (3*df['x'] - 4) / 2

print(df)
