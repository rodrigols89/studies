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
plt.grid()
plt.savefig('../images/plot-01.png', format='png')
plt.show()
