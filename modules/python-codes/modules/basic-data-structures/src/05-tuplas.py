###########################################################################
#                            ( Tuplas )                                   #
###########################################################################
# Uma tupla é uma lista "imutável", ou seja, uma tupla é uma sequência    #
# que não pode ser alterada depois de criada.                             #
#                                                                         #
# Uma tupla é definida de forma parecida com uma lista com a diferença    #
# do delimitador. Enquanto listas utilizam colchetes como delimitadores,  #
# as tuplas usam parênteses.                                              #
###########################################################################

days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
print(type(days))

# Podemos omitir os parênteses e inserir os elementos separados por vírgula:
dias = 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'
print(type(dias))

lista = [3, 4]
tupla = (1, 2, lista)
print(tupla)
