import numpy as np
import matplotlib.pyplot as plt

v = np.array([2, 1]) # Cria o Vetor "v" com array NumPy.
s = np.array([-3, 2]) # Cria o Vetor "s" com array NumPy.
z = v + s # soma os vetores "v" e "s".
vectors = np.array([v, s, z]) # Adiciona os Vetores "v", "s" e "z" dentro de um terceiro Vetor.

print("v = {0}\n s = {1}\n v + s = {2}\n v + s + z = {3}".format(v, s, z, vectors))

# Cria um plot com quiver() para exibir os 3 vetores.
plt.quiver(0, 0, vectors[:,0], vectors[:,1], color=['r', 'b', 'g'], scale=10)
plt.axis('equal') 
plt.xlabel('Coordenadas - X')
plt.ylabel('Coordenadas - Y')
plt.grid()
plt.savefig('../images/plot-03.png', format='png')
plt.show()
