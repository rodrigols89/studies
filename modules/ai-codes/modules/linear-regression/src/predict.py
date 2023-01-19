########################################################
# Rodrigo Leite - drigols                              #
# Last update: 22/09/2021                              #
########################################################

def predict_salary(dic, x_value):
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

  # Linear Regression formula.
  predict_y = m*x_value + b

  print("\nAngular Coefficient (m): {0}\nLinear Coefficient (b): {1}".format(round(m), round(b)))
  print("Student with grade {0} may have {1} salary approximately".format(round(x_value), round(predict_y)))



if __name__ =="__main__":

  students_dic = {
    'Grade':[50, 50, 46, 95, 50, 5, 57, 42, 26, 72, 78, 60, 40, 17, 85],
    'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000, 42000, 47000, 78000, 119000, 95000, 49000, 29000, 130000]
  }

  predict_salary(students_dic, 85)
