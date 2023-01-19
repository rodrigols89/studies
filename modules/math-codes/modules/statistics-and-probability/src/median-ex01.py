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

  students = {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
    'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000]
  }

  # Create a DataFrame with create_df() function.
  my_df = create_df(**students)

  my_df = my_df.sort_values('Salary') # Order "Salary" column
  print("DataFrame ordered by salaries: \n", my_df)
  print("Salary median: ", my_df['Salary'].median())
