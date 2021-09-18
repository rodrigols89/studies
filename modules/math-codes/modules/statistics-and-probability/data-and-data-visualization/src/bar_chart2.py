from matplotlib import pyplot as plt
import statsmodels.api as sm

df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data
families = df[['family', 'children']].drop_duplicates() # Pega family/children e remova duplicadas.
childCounts = families['children'].value_counts().sort_index() # Conta e ordena os valores de "children".

# Cria o plot/gráfico com pyplot - plt.
childCounts.plot(kind='bar', title='Tamanho da Família')
plt.xlabel('Número de Crianças')
plt.ylabel('Famílias')
plt.savefig('../images/plot-02.png', format='png')
plt.show()
