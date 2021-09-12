import matplotlib.pyplot as plt
import numpy as np

# Create a Vector with the NumPy array function. 
v = np.array([2,1])

# Utiliza a função quiver() do Matplotlib para criar o plot/gráfico.
# A função quiver() recebe 4 argumentos principais:
# - As coordenadas iniciais do vetor - x = 0 e y = 0, no nosso caso
# - Quantas posições o vetor vai andar - x = 1 e y =1, nosso caso - *v


# Use Matplotlib quiver() function to create the plot/graph. 
# The quiver() function takes 4 main arguments: 
# - The initial coordinates of the vector - x = 0 and y = 0, in our case 
# - How many positions the vector will move: x = 2 and y = 1, our case - *v 
plt.quiver(0, 0, *v, scale=10, color='r')
plt.axis('equal') # Sets the plot size as "equal".

plt.grid()
plt.title('v = (2, 1)')
plt.xlabel('Coordinates - X')
plt.ylabel('Coordinates - Y')
plt.savefig('../images/first_vector.png', format='png')
plt.show()
