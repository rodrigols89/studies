from matplotlib import pyplot as plt

# Uma coleção de 16 fichas poderia ser composta por:
chipsAll10s = [16, 0] # 16 fichas de £10 e nenhuma de £25.
chipsAll25s = [0, 16] # Ou nenhuma de £10 e 16 de £25.

# Da mesma forma, um total de £250 poderia ser composto por:
valueAll10s = [25, 0] # 25 fichas de £10 e nenhuma de £25 - Totalizando £250
valueAll25s = [0, 10] # Ou nenhuma de £10 e 10 de £25 - Totalizando £250;

plt.plot(chipsAll10s, chipsAll25s, color='blue')
plt.plot(valueAll10s, valueAll25s, color="orange")
plt.xlabel('Eixo-x (Fichas de £10)')
plt.ylabel('Eixo-y (Fichas de £25)')
plt.grid()
plt.savefig('../images/plot-01.png', format='png')
plt.show()
