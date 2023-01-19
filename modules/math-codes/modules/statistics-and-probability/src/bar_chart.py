########################################################
# Rodrigo Leite - drigols                              #
# Last update: 23/09/2021                              #
########################################################

from matplotlib import pyplot as plt
import statsmodels.api as sm

df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data
genderCounts = df['gender'].value_counts()

genderCounts.plot(kind='bar', title='Gender count')
plt.xlabel('Gender')
plt.ylabel('Child numbers')
plt.savefig('../images/bar_chart_childs.png', format='png')
plt.show()
