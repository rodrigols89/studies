def f(x):
  return 2 * x

def create_plot(x, y):
  import matplotlib.pyplot as plt
  plt.plot(x, y, color='blue', marker='o') # marker='o' marca o ponto de intersecção da função
  plt.title('Relação entre Laranjas & Copos de suco de Laranja')
  plt.xlabel('Quantidade de Laranjas')
  plt.ylabel('Quantidade de copos de suco de Laranja')
  plt.axis([0, 10, 0, 10])
  plt.grid()
  plt.savefig('../images/plot-01.png', format='png')
  plt.show()

if __name__ =='__main__':
  oranges = [1, 2, 3, 4] # Vamos testar apenas com até 4 laranjas.
  y = [] # Copos de suco vai começar vazio

  for orange in oranges:
    # Para cada laranja adicionamos quantos copos de suco será.
    y.append(f(orange))

  create_plot(oranges, y)
