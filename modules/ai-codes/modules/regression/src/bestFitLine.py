from matplotlib import pyplot as plt
import pandas as pd

df = pd.DataFrame(
  {
    'Experience': [2, 3, 5, 13, 8, 16, 11, 1, 9],
    'Salary': [15, 28, 42, 64, 50, 90, 58, 8, 54]
  }
)

df['(x_i - x_mean)'] = df['Experience'] - df['Experience'].mean()
df['(y_i - y_mean)'] = df['Salary'] - df['Salary'].mean()
df['(x_i - x_mean)(y_i - y_mean)'] = df['(x_i - x_mean)'] * df['(y_i - y_mean)']
df['(x_i - x_mean)^2'] = (df['Experience'] - df['Experience'].mean())**2


m = (sum(df['(x_i - x_mean)'] * df['(y_i - y_mean)'])) / sum(df['(x_i - x_mean)^2'])
b = df['Salary'].mean() - (m * df['Experience'].mean())

regression_line = [(m*x) + b for x in df['Experience']]

plt.figure(figsize=(10, 7))
plt.scatter(df.Experience, df.Salary, color='g')
plt.plot(df.Experience, regression_line, color='b')
plt.title('Years of Experience vs Salary in $1000')
plt.xlabel('Years of Experience')
plt.ylabel('Salary in $1000')
plt.grid()
plt.savefig('../images/plot-02.png', format='png')
plt.show()
