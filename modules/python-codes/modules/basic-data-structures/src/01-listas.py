# Cria uma lista vazia.
empty_list = []
print(empty_list)
print('A sua estrutura de dados é: {}'.format(type(empty_list)), '\n')


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(lista)) # Imprime o menor elemento da lista.
print(max(lista), '\n') # Imprime o maior elemento da lista.


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Imprime o NÚMERO DE ELEMENTOS DA LISTA.
print(len(lista), '\n')


# Verifica se os elementos estão na lista.
# O retorno vai ser booleano - True ou False.
print(0 in lista)
print(5 in lista)
print(20 in lista)
print(1000 in lista)
print(1 in lista, '\n')


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# O função append() adiciona um elemento no final de uma lista.
lista.append(1000)
print(lista)
lista.append(50)
print(lista)
lista.append(1000)
print(lista)
lista.append(80)
print(lista, '\n')


# Converte o texto "Python" em uma lista de strings com a função list().
lista = list('Python')
print(lista)
print(type(lista), '\n')
