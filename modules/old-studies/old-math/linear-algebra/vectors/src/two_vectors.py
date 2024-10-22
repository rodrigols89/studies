import math
import numpy as np
import matplotlib.pyplot as plt

v = np.array([2, 1]) # Cria o Vetor "v" com array NumPy.
s = np.array([-3, 2]) # Cria o Vetor "s" com array NumPy.
vectors = np.array([v, s]) # Adiciona os Vetores "v" e "s" dentro de um terceiro Vetor.

print("A soma dos vetores v = {0} e s = {1}:\n {2}".format(v, s, vectors))

# Cria um plot com quiver() e passa como argumento:
# - Os pontos inicias - x = 0 e y = 0;
# - Todo o Vetor "v" - vectors[:, 0];
# - Todo o Vetor "s" - vectors[:, 1];
# - as cores para cada Vetor, respectivamente;
# - Scale - é uma forma de dimensionar dentro do plot.
plt.quiver(0, 0, vectors[:,0], vectors[:,1], color=['r', 'b'], scale=10)
plt.axis('equal') # Define o dimensionamento do plot igual.
plt.title('v = (2, 1), s = (-3, 2)')
plt.xlabel('Coordenadas - X')
plt.ylabel('Coordenadas - Y')
plt.grid()
plt.savefig('../images/plot-02.png', format='png')
plt.show()
