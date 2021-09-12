import numpy as np
import math

v = np.array([2, 1])
vTan = v[1] / v[0] # Calculates the tangent.
print ('tan = ' + str(vTan)) # Prints the tangent.

vAtan = math.atan(vTan) 
print('inverse-tan = ' + str(math.degrees(vAtan)))
