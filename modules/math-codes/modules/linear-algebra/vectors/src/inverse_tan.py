import math
import numpy as np

v = np.array([2,1]) # Cria uma representação do nosso Vetor.
vTan = v[1] / v[0] # Calcula a tangente.
print ('tan = ' + str(vTan)) # Imprime a tangente.

vAtan = math.atan(vTan) 
print('inverse-tan = ' + str(math.degrees(vAtan)))
