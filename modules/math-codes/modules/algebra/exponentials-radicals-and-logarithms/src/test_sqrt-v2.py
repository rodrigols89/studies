def my_sqrt(x, e):
  b = round(x ** (1. / e))
  print("A raiz de {0} elevado {1}ª potência: {2}".format(x, round(e), b))

if __name__ =='__main__':
  x = float(input("Digite a raiz que você deseja saber: "))
  e = float(input("Elevado a qual potência essa raiz? "))

  my_sqrt(x, e)
