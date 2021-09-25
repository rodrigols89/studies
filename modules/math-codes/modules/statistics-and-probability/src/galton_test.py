########################################################
# Rodrigo Leite - drigols                              #
# Last update: 23/09/2021                              #
########################################################

import statsmodels.api as sm

df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data
print(df.head(10))
