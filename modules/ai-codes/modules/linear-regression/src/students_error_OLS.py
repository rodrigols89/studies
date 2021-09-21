from matplotlib import pyplot as plt
import pandas as pd

df = pd.DataFrame(
  {
    'Grade':[50, 50, 46, 95, 50, 5, 57, 42, 26, 72, 78, 60, 40, 17, 85],
    'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000, 42000, 47000, 78000, 119000, 95000, 49000, 29000, 130000]
  }
)

df['(x_i - x_mean)'] = df['Grade'] - df['Grade'].mean()
df['(y_i - y_mean)'] = df['Salary'] - df['Salary'].mean()
df['(x_i - x_mean)(y_i - y_mean)'] = df['(x_i - x_mean)'] * df['(y_i - y_mean)']
df['(x_i - x_mean)^2'] = (df['Grade'] - df['Grade'].mean())**2

m = (sum(df['(x_i - x_mean)'] * df['(y_i - y_mean)'])) / sum(df['(x_i - x_mean)^2'])
b = df['Salary'].mean() - (m * df['Grade'].mean())

df['y = mx + b'] = [(m*x) + b for x in df['Grade']]
df['y_i - y = mx + b'] = df['Salary'] - df['y = mx + b']
df['(y_i - y = mx + b)^2'] = df['y_i - y = mx + b'] ** 2

newDF = df[['Grade', 'Salary', 'y = mx + b', 'y_i - y = mx + b', '(y_i - y = mx + b)^2']]

print(newDF)
print("Sum of Squared Errors (OLS): ", round(sum(newDF['(y_i - y = mx + b)^2'])))
