########################################################
# Rodrigo Leite - drigols                              #
# Last update: 21/09/2021                              #
########################################################

def OLS(dic):
  from matplotlib import pyplot as plt
  import pandas as pd

  df = pd.DataFrame(dic)

  df['(x_i - x_mean)'] = df['Grade'] - df['Grade'].mean()
  df['(y_i - y_mean)'] = df['Salary'] - df['Salary'].mean()
  df['(x_i - x_mean)(y_i - y_mean)'] = df['(x_i - x_mean)'] * df['(y_i - y_mean)']
  df['(x_i - x_mean)^2'] = (df['Grade'] - df['Grade'].mean())**2

  m = (sum(df['(x_i - x_mean)'] * df['(y_i - y_mean)'])) / sum(df['(x_i - x_mean)^2'])
  b = df['Salary'].mean() - (m * df['Grade'].mean())

  print("Angular Coefficient (m): {0}\nLinear Coefficient (b): {1}".format(round(m), round(b)))

  regression_line = [(m*x) + b for x in df['Grade']]

  plt.figure(figsize=(10, 7))
  plt.scatter(df.Grade, df.Salary, color='g')
  plt.plot(df.Grade, regression_line, color='b')
  plt.title('Grades vs Salaries | Ordinary Least Squares: OLS')
  plt.xlabel('Grade')
  plt.ylabel('Salary')
  plt.grid()
  plt.savefig('../images/plot-02.png', format='png')
  plt.show()

if __name__ =="__main__":

  students_dic = {
    'Grade':[50, 50, 46, 95, 50, 5, 57, 42, 26, 72, 78, 60, 40, 17, 85],
    'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000, 42000, 47000, 78000, 119000, 95000, 49000, 29000, 130000]
  }

  OLS(students_dic)
