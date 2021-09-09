from matplotlib import pyplot as plt
import pandas as pd

df = pd.DataFrame(
  {
    'Grade':[50, 50, 46, 95, 50, 5, 57, 42, 26, 72, 78, 60, 40, 17, 85],
    'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000, 42000, 47000, 78000, 119000, 95000, 49000, 29000, 130000]
  }
)

plt.figure(figsize=(10, 7))
plt.scatter(df.Grade, df.Salary, color='g')
plt.title('Grades vs Salaries')
plt.xlabel('Grade')
plt.ylabel('Salary')
plt.savefig('../images/plot-01.png', format='png')
plt.show()
