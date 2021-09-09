import pandas as pd
import numpy as np

def create_dataframe(data_items, row, col):
  return pd.DataFrame(data=data_items, index=row, columns=col)

if __name__ =='__main__':

  arr = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
  arr = np.array(arr)

  row = ['A', 'B', 'C']
  col = ['X', 'Y', 'Z']

  mydf = create_dataframe(arr, row, col)
  print(mydf)
