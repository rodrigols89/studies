########################################################
# Rodrigo Leite - drigols                              #
# Last update: 23/09/2021                              #
########################################################

from matplotlib import pyplot as plt
import statsmodels.api as sm

df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data
families = df[['family', 'children']].drop_duplicates()
childCounts = families['children'].value_counts().sort_index()

childCounts.plot(kind='bar', title='Family size')
plt.xlabel('Child numbers')
plt.ylabel('Families')
plt.savefig('../images/bar_chart_childs_families.png', format='png')
plt.show()
