########################################################################
#                        append() vs extend()                          #
########################################################################
# A função append() só consegue inserir um elemento por vez.           #
# Se quisermos inserir mais elementos podemos somar ou multiplicar     #
# listas, ou então utilizar a função extend():                         #
########################################################################

# Cria uma lista vazia.
empty_list = []

empty_list.append('zero')
print(empty_list)

empty_list.append('um')
print(empty_list)

empty_list.extend(['dois', 'três'])
print(empty_list)

empty_list += ['quatro']
print(empty_list)
