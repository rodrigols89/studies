########################################################
# Rodrigo Leite - drigols                              #
# Last update: 27/09/2021                              #
########################################################

def create_df(**df):
  my_df = {}
  import pandas as pd
  my_df = pd.DataFrame(df)
  return my_df

if __name__ =='__main__':

  import matplotlib.pyplot as plt

  sleep_search = {
    'A': [6, 6, 7, 8, 8, 8, 9],
    'B': [6, 7, 8, 8, 12, 12, 15]
  }

  my_df = create_df(**sleep_search)
  print(my_df)

  plt.plot(my_df, marker='o')
  plt.title("A vs B")
  plt.xlabel("Days of the week - x")
  plt.ylabel("Sleeped hours - y")
  plt.legend(['A', 'B'])
  plt.grid()
  plt.savefig('../images/mean-median.png', format='png')
  plt.show()
