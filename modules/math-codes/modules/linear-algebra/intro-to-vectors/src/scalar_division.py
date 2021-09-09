import numpy as np
import matplotlib.pyplot as plt

v = np.array([2,1]) # Cria o Vetor do nosso exemplo.
b = v / 2 # Divide o Vetor "v" por 2 - Scale.
print(b) # Imprime o Vetor dividido.

# Cria um plot/gráfico com quiver() para exibir o vetor multiplicado.
plt.quiver(0, 0, *b, scale=10)
plt.axis('equal')
plt.grid()
plt.savefig('../images/plot-05.png', format='png')
plt.show()
