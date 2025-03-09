import pandas as pd

with open('../datasets/Galton_Dataset.txt', 'r') as f:
  data = pd.read_table(f, sep='\s+')

print(data.head(10))
