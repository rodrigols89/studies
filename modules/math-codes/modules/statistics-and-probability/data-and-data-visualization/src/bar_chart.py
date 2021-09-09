from matplotlib import pyplot as plt
import statsmodels.api as sm

df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data # Pega o dataset de Galton.
genderCounts = df['gender'].value_counts() # Conta e pega os valores de gênero - male/female

genderCounts.plot(kind='bar', title='Contagens de Gênero')
plt.xlabel('Gênero')
plt.ylabel('Número de Crianças')
plt.savefig('../images/plot-01.png', format='png')
plt.show()
