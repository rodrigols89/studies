import numpy as np

p = np.array([2,3,1]) # Cria o vetor "p" do nosso exemplo.
q = np.array([1,2,-2]) # Cria o vetor "q" do nosso exemplo.

# Aplica a multiplicação cruzada com a função cross().
r = np.cross(p,q)

print(r)
