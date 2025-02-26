import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('../datasets/2015-building-energy-benchmarking.csv')

# Plot.
plt.figure(figsize=(10, 10))
sns.heatmap(data.corr(), linewidths=.2)
plt.savefig('../images/plot-02.png', format='png')
plt.show()
