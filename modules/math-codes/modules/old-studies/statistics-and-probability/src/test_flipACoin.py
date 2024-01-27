from matplotlib import pyplot as plt
import random

# Cria uma lista com 2 elementos (para Cara(0) e Coroa(1)).
# Nós vamos adicionar elementos nessa lista pelo os índices Cara(0) e Coroa(1).
heads_tails = [0, 0]

# Variáveis para controlar o loop de 0(trial) até 10000(trials).
trials = 10000
trial = 0

while trial < trials:
  trial = trial + 1 # Incrementa +1 n a variável trial.
  toss = random.randint(0,1) # Cria um sorteio(toss) de números aleatórios entre 0(cara) e 1 (coroa).
  heads_tails[toss] = heads_tails[toss] + 1 # Adiciona o número sorteado Cara(0) ou Coroa(1) pelo índice.

# Imprime o número de Caras e Coroas na lista.
print(heads_tails)

# Cria um plot/gráfico do tipo Pie Chart (Gráfico de Pizza).
plt.figure(figsize=(5, 5))
plt.pie(heads_tails, labels=['Cara', 'Coroa'])
plt.legend()
plt.savefig('../images/plot-01.png', format='png')
plt.show()
