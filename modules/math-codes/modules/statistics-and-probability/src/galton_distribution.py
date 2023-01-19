########################################################
# Rodrigo Leite - drigols                              #
# Last update: 17/12/2021                              #
########################################################

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

import statsmodels.api as sm

# Importa o dataset de Galton.
df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data

fathers = df['father'] # Pega a label/coluna que contém ás altuas dos pais.
density = stats.gaussian_kde(fathers) # Pega a densidade de altura dos pais.

n, x, _ = plt.hist(fathers, histtype='step', density=True, bins=50) # Cria o Histograma.
plt.plot(x, density(x)*2.5) # Adiciona a densidade/linha de densidade no plot/Histograma.
plt.axvline(fathers.mean(), color='magenta', linestyle='dashed', linewidth=2) # Adiciona a mean() lane no plot.
plt.axvline(fathers.median(), color='green', linestyle='dashed', linewidth=2) # Adiciona a median() lane no plot.
plt.show()
