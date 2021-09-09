from matplotlib import pyplot as plt
import statsmodels.api as sm


df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data
parentHeights = df[['midparentHeight', 'childHeight']] # Pega os dados "midparentHeight" e "childHeight"

parentHeights.plot(kind='scatter', title='Parent vs Child Heights', x='midparentHeight', y='childHeight')
plt.xlabel('Avg Parent Height')
plt.ylabel('Child Height')
plt.savefig('../images/plot-05.png', format='png')
plt.show()
