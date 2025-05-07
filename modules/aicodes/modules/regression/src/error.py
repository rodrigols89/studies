from matplotlib import pyplot as plt
import pandas as pd

df = pd.DataFrame(
  {
    'Experience': [2, 3, 5, 13, 8, 16, 11, 1, 9],
    'Salary': [15, 28, 42, 64, 50, 90, 58, 8, 54]
  }
)

df['Error'] = df['Salary'] - df['Salary'].mean()
df['Squared Errors'] = df['Error']**2
print(df)
print("Sum of Squared Errors (SSE): ", sum(df['Squared Errors']))
