def sum_squares(i, n):
  s = []
  p = i
  while p <= n:
    s.append(p ** 2)
    p += 1
  s = sum(s)
  print("O somatório dos quadrados (n²) de {0} até {1} é {2}.".format(i, n, s))

if __name__ =='__main__':
  s = sum_squares(1, 10)
