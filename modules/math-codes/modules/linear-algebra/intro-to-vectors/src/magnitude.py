import math
import numpy as np

# Cria um Vetor com a função array do NumPy.
v = np.array([2, 1])

# Tira a Magnitude do Vetor.
vMag = math.sqrt(v[0]**2 + v[1]**2)
print("Magnitude (distância) do meu vetor {0} é {1}".format(v, vMag))
