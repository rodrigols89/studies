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

print(df)

m = (sum(df['(x_i - x_mean)'] * df['(y_i - y_mean)'])) / sum(df['(x_i - x_mean)^2'])
b = df['Salary'].mean() - (m * df['Experience'].mean())

print("Angular Coefficient (m): {0}\nLinear Coefficient (b): {1}".format(m, b))
