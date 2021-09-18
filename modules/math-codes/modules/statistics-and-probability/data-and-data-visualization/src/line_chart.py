from matplotlib import pyplot as plt
import statsmodels.api as sm

df = sm.datasets.elnino.load_pandas().data # Pega o dataset elnino das temperaturas.

# Adiciona uma coluna ao df com as médias por ano - "AVGSEATEMP".
# - Soma de todos os meses - Janeiro à Dezembro;
# - Divida por o número de meses - 12.
df['AVGSEATEMP'] = df.mean(1) # A média(mean) inicia a partir do índice 1(janeiro).

# Exibe o DataFrame com a nova amostra.
print(df.head(10))

# Cria o plot/gráfico com pyplot.plot - plt.
df.plot(title='Average Sea Temperature', x='YEAR', y='AVGSEATEMP')
plt.xlabel('Year')
plt.ylabel('Average Sea Temp')
plt.savefig('../images/plot-06.png', format='png')
plt.show()
