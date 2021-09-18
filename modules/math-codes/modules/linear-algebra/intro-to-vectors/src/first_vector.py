import numpy as np
import matplotlib.pyplot as plt

# Cria um Vetor com a função array do NumPy.
v = np.array([2,1])

# Utiliza a função quiver() do Matplotlib para criar o plot/gráfico.
# A função quiver() recebe 4 argumentos principais:
# - As coordenadas iniciais do vetor - x = 0 e y = 0, no nosso caso
# - Quantas posições o vetor vai andar - x = 1 e y =1, nosso caso - *v
plt.quiver(0, 0, *v, scale=10, color='r')
plt.axis('equal') # Define o dimensionamento do plot igual.

plt.grid()
plt.title('v = (2, 1)')
plt.xlabel('Coordenadas - X')
plt.ylabel('Coordenadas - Y')
plt.savefig('../images/plot-01.png', format='png')
plt.show()
