from create_dataframe import create_df
import matplotlib.pyplot as plt

if __name__ =='__main__':


  students = {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
    'Salary':[50000,54000,50000,189000,59000,40000,59000]
  }

  my_df = create_df(**students)
  salary = my_df['Salary'] # Pega os salários do DataFrame e salva no objeto "salary".

  # Cria o plot/gráfico.
  salary.plot.hist(title='Salary Distribution', color='lightblue', bins=25) # Cria o Histogram a partir de "salary".
  plt.axvline(salary.mean(), color='magenta', linestyle='dashed', linewidth=2) # Adiciona mean() lane no plot.
  plt.axvline(salary.median(), color='green', linestyle='dashed', linewidth=2) # Adiciona median() lane no plot.
  plt.savefig('../images/plot-02.png', format='png')
  plt.show()


