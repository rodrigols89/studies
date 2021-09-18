from matplotlib import pyplot as plt
import pandas as pd

df = pd.DataFrame(
  {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny'],
    'Grade':[50,50,46,95,50,5,57,42,26,72,78,60,40,17,85]
  })

print(df.describe())
print('median: ' + str(df['Grade'].median()))

# Cria um gráfico de caixa/box plot.
plt.figure()
df['Grade'].plot( kind='box', title='Grade Distribution')
plt.savefig('../images/plot-01.png', format='png')

# Cria um histograma.
plt.figure()
df['Grade'].hist(bins=9)
plt.savefig('../images/plot-02.png', format='png')

plt.show() # Exibe o plotgráfico/.
