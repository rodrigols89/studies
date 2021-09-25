from matplotlib import pyplot as plt
import statsmodels.api as sm

df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data
genderCounts = df['gender'].value_counts() # Conta e pega os valores de gêneros - male/female

genderCounts.plot(kind='pie', title='Gender Counts', figsize=(6,6))
plt.legend()
plt.savefig('../images/plot-04.png', format='png')
plt.show()
