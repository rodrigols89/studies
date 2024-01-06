from math import log

def my_log(x, b):
  e = log(x, b)
  print("O logaritmo de {0} na base {1}: {2}".format(x, b, e))

if __name__ =='__main__':
  x = float(input("Digite o número: "))
  b = float(input("Digite a base do logaritmo: "))

  my_log(x, b)
