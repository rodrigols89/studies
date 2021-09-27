from create_dataframe import create_df

if __name__ =='__main__':
  students = {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
    'Salary':[50000,54000,50000,189000,59000,40000,59000]
  }

  my_df = create_df(**students)
  print ('Min: ' + str(my_df['Salary'].min())) # Pega o menor salário/elmento da lista.
  print ('Mode: ' + str(my_df['Salary'].mode()[0])) # Encontra o mode (o/os mais frequente(s)).
  print ('Median: ' + str(my_df['Salary'].median())) # Encontra a mediana (median).
  print ('Mean: ' + str(my_df['Salary'].mean())) # Encontra a média (mean)
  print ('Max: ' + str(my_df['Salary'].max())) # Pega o maior salário/elemento da lista.
