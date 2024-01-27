from matplotlib import pyplot as plt
import pandas as pd

df = pd.DataFrame ({'x': range(-10, 10+1)})
df['y'] = (3*df['x'] - 4) / 2

plt.figure(figsize=(10, 10))
plt.plot(df.x, df.y, color="grey", marker = "o")
plt.xlabel('x')
plt.ylabel('y = 3*x -4 / 2')
plt.title("Relação Linear entre as variáveis x e y = 3*x -4/2")
plt.xticks(range(-10, 10+1, 1))
plt.yticks(range(-20, 20+1, 1))
plt.axhline() # Adiciona uma linda na horizontal (h) - (eixo-x)
plt.axvline() # Adiciona uma linha na vertical (v) - (eixo-y)
plt.annotate('x-intercept',(1.333, 0)) # Adiciona um texto em uma coordenada (x, y) predefinida.
plt.annotate('y-intercept',(0,-2)) # Adiciona um texto em uma coordenada (x, y) predefinida.

m = 1.5 # Salva a inclinação (slope) que nós calculamos.
yInt = -2 # Pega a interceptação no eixo "y" - (Quando x é zero).

# Traçar a inclinação (slope) da interceptação em y para 1x
mx = [0, 1] # Vai começar no x = 0 e aumentar 1 unidade, ou seja, x = 1.
my = [yInt, yInt + m] # y vai começar na interceptação -2, quando x = 0, e vai incrementar inclinação m = 1,5.
plt.plot(mx, my, color='red', lw=5)

plt.grid()
plt.savefig('../images/plot-04.png', format='png')
plt.show()
