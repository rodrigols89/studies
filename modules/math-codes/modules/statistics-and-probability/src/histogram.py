import statsmodels.api as sm # Importa a biblioteca statsmodels.
from matplotlib import pyplot as plt # Importa a bibliote pyplot do Matplotlib.

df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data

df['father'].plot.hist(title='Alturas dos Pai')
plt.xlabel('Altura')
plt.ylabel('Frequência')
plt.savefig('../images/plot-03.png', format='png')
plt.show()
