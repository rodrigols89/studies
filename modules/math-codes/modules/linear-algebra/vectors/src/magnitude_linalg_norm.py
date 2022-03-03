import numpy as np

# Cria um Vetor com a função array do NumPy.
v = np.array([2, 1])

# Tira a Magnitude do Vetor.
vMag = np.linalg.norm(v)
print("Magnitude (distância) do meu vetor {0} é {1}".format(v, vMag))
