frutas = {'Laranja', 'Pera', 'Uva', 'Laranja', 'Banana', 'Pera', 'Banana'}
print(frutas)
print(type(frutas))

print('')

# Cria conjuntos com a função set()
a = set('abacate')
print(type(a))
b = set('abacaxi')
print(type(b))

print('')

print(a) # Imprime o conjunto "a"
print(b) # Imprime o conjunto "b"
print(a - b) # Diferença dos conjuntos "a" e "b"
print(a | b) # União dos conjuntos "a" e "b"
print(a & b) # Interseção dos conjuntos "a" e "b"
print(a ^ b) # Diferença simétrica dos conjuntos "a" e "b"
