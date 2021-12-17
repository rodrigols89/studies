########################################################
# Rodrigo Leite - drigols                              #
# Last update: 17/12/2021                              #
########################################################

def create_df(**df):
  my_df = {}
  import pandas as pd
  my_df = pd.DataFrame(df)
  return my_df

if __name__ =='__main__':
  students = {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
    'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000]
  }

  my_df = create_df(**students)
  moda = my_df['Salary'].mode()
  print("O salário mais frequente é: {0}".format(moda))
