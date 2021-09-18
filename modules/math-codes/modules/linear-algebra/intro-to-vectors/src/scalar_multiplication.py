import numpy as np
import matplotlib.pyplot as plt

v = np.array([2,1]) # Cria o Vetor do nosso exemplo.
w = 2 * v # Faz uma multiplicação Escalar - Por 2.
print('Vetor v: {0}\n Vetor multiplicado w: {1}\n'.format(v, w))

# Cria um plot/gráfico com quiver() para exibir o vetor multiplicado.
plt.quiver(0, 0, *w, scale=10)
plt.axis('equal')
plt.grid()
plt.savefig('../images/plot-04.png', format='png')
plt.show()
