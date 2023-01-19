########################################################
# Rodrigo Leite - drigols                              #
# Last update: 26/09/2021                              #
########################################################

from matplotlib import pyplot as plt
import statsmodels.api as sm

df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data
genderCounts = df['gender'].value_counts() # Count and take gender values (Male/Female)

genderCounts.plot(kind='pie', title='Gender Counts', figsize=(6,6))
plt.legend()
plt.savefig('../images/pie-chart.png', format='png')
plt.show()
