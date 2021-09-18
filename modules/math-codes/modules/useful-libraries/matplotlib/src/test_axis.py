import matplotlib.pyplot as plt

plt.plot([-3, -2, 5, 0], [1, 6, 4, 3])

# Eixo "x" = mínimo -4 e máximo 6
# Eixo "y" = mínimo 0 e máximo 7
plt.axis([-4, 6, 0, 7])

plt.savefig('../images/fig-03.png', format='png')
plt.show()
