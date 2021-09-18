import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('../datasets/datasets_228_482_diabetes.csv')

# Plot.
plt.figure(figsize=(10, 10))
sns.heatmap(data.corr(), annot=True, linewidths=.5)
plt.savefig('../images/plot-01.png', format='png')
plt.show()
