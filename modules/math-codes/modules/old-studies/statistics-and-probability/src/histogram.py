########################################################
# Rodrigo Leite - drigols                              #
# Last update: 26/09/2021                              #
########################################################

import statsmodels.api as sm
from matplotlib import pyplot as plt

df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data

df['father'].plot.hist(title='Fathers height')
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.savefig('../images/histogram-ex01.png', format='png')
plt.show()
