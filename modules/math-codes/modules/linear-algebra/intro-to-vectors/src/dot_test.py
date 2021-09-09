import numpy as np

# Cria os vetores "v" e "s".
v = np.array([2,1]) # Cria o vetor "v".
s = np.array([-3,2]) # Cria o vetor "s".

d = np.dot(v,s) # Aplica o dot().

print("v = {0}\n s = {1}\n Multiplicação (scalar) com Dot(): {2}".format(v, s, d))
