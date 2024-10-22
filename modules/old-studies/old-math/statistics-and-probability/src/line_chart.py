########################################################
# Rodrigo Leite - drigols                              #
# Last update: 26/09/2021                              #
########################################################

from matplotlib import pyplot as plt
import statsmodels.api as sm

df = sm.datasets.elnino.load_pandas().data # Take Elnino Temperature dataset.

# Add a column with average per year - "AVGSEATEMP".
# - Sum all months - January to December;
# - Divide by month numbers (12).
df['AVGSEATEMP'] = df.mean(1) # The mean start into indice 1 (January).

print(df.head(10))

df.plot(title='Average Sea Temperature', x='YEAR', y='AVGSEATEMP')
plt.xlabel('Year')
plt.ylabel('Average Sea Temp')
plt.savefig('../images/line-chart.png', format='png')
plt.show()
