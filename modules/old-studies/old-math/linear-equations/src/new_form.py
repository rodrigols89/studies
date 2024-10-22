from matplotlib import pyplot as plt
import pandas as pd

df = pd.DataFrame ({'x': range(-10, 10+1)})

# Define slope and y-intercept
m = 1.5 # Inclinação (Slope)
yInt = -2 # Interceptação "y" - (Quando X = 0)

# Adiciona a coluna "y" seguindo a nossa nova fórmula - y = m*x + b (b = ponto de interceptação y)
df['y'] = m*df['x'] + yInt

plt.figure(figsize=(10, 10))
plt.plot(df.x, df.y, color="grey")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.xticks(range(-10, 10+1, 1))
plt.yticks(range(-20, 20+1, 1))
plt.axhline()
plt.axvline()

# Adiciona notação na interceptação "y" quando x = 0.
plt.annotate('y-intercept',(0, yInt))

# plota a inclinação da interceptçaão em y para 1x
mx = [0, 1]
my = [yInt, yInt + m]
plt.plot(mx,my, color='red', lw=5)
plt.savefig('../images/plot-05.png', format='png')
plt.show()
