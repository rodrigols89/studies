########################################################
# Rodrigo Leite - drigols                              #
# Last update: 21/09/2021                              #
########################################################

def GD(dic):
  from matplotlib import pyplot as plt
  import pandas as pd

  df = pd.DataFrame(dic)

  # Start coefficients (Angular and Linear).
  m = 7
  b = 1

  # Learning rate
  learning_rate = 0.000001

  # Search best value for coefficients m and b.
  for i in range(1, 1000+1, 1):
    y_pred = m*df['Grade'] + b
    m_derivative = sum(2*df['Grade']*(y_pred - df['Salary']))
    b_derivative = sum(2*(y_pred - df['Salary']))
    m = m - (learning_rate * m_derivative)
    b = b - (learning_rate * b_derivative)
    # print(m, b) # Remove comments to view step-by-step.

  print("\nAngular Coefficient (m): {0}\nLinear Coefficient (b): {1}".format(round(m), round(b)))

  regression_line = [(m*x) + b for x in df['Grade']]

  plt.figure(figsize=(10, 7))
  plt.scatter(df.Grade, df.Salary, color='g')
  plt.plot(df.Grade, regression_line, color='b')
  plt.title('Grades vs Salaries | Gradient descent Approach')
  plt.xlabel('Grade')
  plt.ylabel('Salary')
  plt.grid()
  plt.savefig('../images/plot-03.png', format='png')
  plt.show()

if __name__ =="__main__":

  students_dic = {
    'Grade':[50, 50, 46, 95, 50, 5, 57, 42, 26, 72, 78, 60, 40, 17, 85],
    'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000, 42000, 47000, 78000, 119000, 95000, 49000, 29000, 130000]
  }

  GD(students_dic)
