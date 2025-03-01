from matplotlib import pyplot as plt
import pandas as pd

df = pd.DataFrame(
  {
    'Experience': [2, 3, 5, 13, 8, 16, 11, 1, 9],
    'Salary': [15, 28, 42, 64, 50, 90, 58, 8, 54]
  }
)

print(df)

plt.figure(figsize=(10, 7))
plt.scatter(df.Experience, df.Salary, color='g')
plt.title('Years of Experience vs Salary in $1000')
plt.xlabel('Years of Experience')
plt.ylabel('Salary in $1000')
plt.grid()
plt.savefig('../images/plot-01.png', format='png')
plt.show()
