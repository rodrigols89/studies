import pandas as pd
import numpy as np

def create_dataframe(data_items, rows, cols):
  return pd.DataFrame(data=data_items, index=rows, columns=cols)

if __name__ =='__main__':

  data = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
  data = np.array(data)

  rows = ['A', 'B', 'C']
  cols = ['X', 'Y', 'Z']

  mydf = create_dataframe(data, rows, cols)
  print(mydf)
