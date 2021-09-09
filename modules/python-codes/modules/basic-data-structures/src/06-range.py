# O retorno é um range(1, 5) não os elementos.
sequencia = range(1, 5)
print(sequencia)
print(type(sequencia))

# Itera pelo os elementos do range().
# O número finalizador não é incluído.
for element in sequencia:
  print(element)

print('')

# Exemplo-02
for n in range(1, 10):
  print(n)

print('')

# Exemplo-03
for n in range(1, 10+1):
  print(n)
