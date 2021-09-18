# Importa a biblioteca statsmodels como "sm".
import statsmodels.api as sm

# Pega o dataset de estudos de "Francis Galton" e salva no objeto "df".
df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data
print(df.head(10)) # Imprime as 10 primeiras amostras.
