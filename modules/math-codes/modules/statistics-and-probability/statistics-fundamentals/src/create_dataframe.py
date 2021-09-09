def create_df(**df):
  my_df = {}
  import pandas as pd
  my_df = pd.DataFrame(df)
  return my_df

if __name__ =='__main__':
  students = {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
    'Salary':[50000,54000,50000,189000,55000,40000,59000]
    }

  my_df = create_df(**students)
  print(my_df)
  print("Média salarial: ", my_df['Salary'].mean(), "\n")

  my_df = my_df.sort_values('Salary')
  print("DataFrame Ordenado por salários: \n", my_df)
  print("Mediana dos salarios: ", my_df['Salary'].median())
