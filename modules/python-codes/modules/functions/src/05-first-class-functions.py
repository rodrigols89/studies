#######################################################
# 01 - Funções são objetos                            #
#######################################################
def test():
  pass
print(type(test))



#######################################################
# 02 - Você pode armazenar uma função em uma variável #
#######################################################
def upper_message(text):
  return text.upper()
message = upper_message('rodrigo') # Salva a função/referência na variável "message".
print(message) # Chama a função a partir da variável/referência "message".



#######################################################################
# 03 - Funções podem ser passadas como argumentos para outras funções #
#######################################################################
def upper(text):
  return text.upper()

def lower(text):
  return text.lower()

print()

print(upper('rodrigo')) # Deixa o texto em maiúsculo.
print(lower('RoDrigo')) # Deixa o texto em minúsculo.

print()

# Agora sim, vamos criar uma função que recebe outra função como argumento.
def higher_order_function(func):
  # Essa função que vamos receber vai ter o objetivo de manipular o texto abaixo. 
  result = func('Rodrigo Leite - Software Engineer')
  return result # Retorna o texto alterado.

# Agora vamos passar a função upper() como argumento que vai ser utilizada
# para deixar um texto em maiúsculo dentro da função higher_order_function().
print(higher_order_function(upper))

# Agora vamos passar a função lower() como argumento que vai ser utilizada
# para deixar um texto em minúsculo dentro da função higher_order_function().
print(higher_order_function(lower), '\n')



#######################################################################
# 04 - Funções podem retornar outra função                            #
#######################################################################
def create_adder(x):
  def adder(y):
    return x + y
  return adder

# Quando nós criamos essa instância, nós estamos passando para o parâmetro
# "x" o valor "10". Ou seja, o "x" vai sempre iniciar com o valor "10" e
# a medida que vamos adicionando valores em "n" vai ser +10:
n = create_adder(10)
print(n(15))
print(n(20))
print(n(30), '\n')



###############################################################################
# 05 - Você pode armazená-las em estruturas de dados, como listas, tuplas,... #
###############################################################################
def test1():
  return 10

def test2():
  return 20

lista = [test1, test2] # Salva as funções em uma lista.
tupla = (test1, test2) # Salva as funções em uma tupla.

# Pega os retornos das funções a partir da lista.
for n in lista:
  print(n())

# Pega os retornos das funções a partir da tupla.
for n in tupla:
  print(n())
