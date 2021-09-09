# Funções - notes

# 01 - Palavra reservada "pass"

```python
def velocidade(espaco, tempo):
  pass
```

Como nossa função acima ainda não faz nada, utilizamos a palavra chave **pass** para dizer ao interpretador que definiremos as instruções depois. A palavra **pass** não é usada apenas em funções, podemos usar em qualquer bloco de comandos como:

 - Nas instruções **if**,
 - **while** e **for**...

# 02 - Funções com parâmetros

Um conjunto de parâmetros consiste em uma lista com nenhum ou mais elementos que podem ser obrigatórios ou opcionais.

Para um parâmetro ser opcional atribuímos um valor padrão (default) para ele - o mais comum é utilizar reservada ***None***:

```python
def dados(nome=None, idade=None):
  print('nome: {}'.format(nome))
  if(idade is not None):
    print('idade: {}'.format(idade))
  else: print('idade: não informada')

if __name__ == "__main__":
  dados('Rodrigo Leite', 30) # Passa o nome e idade.
  dados('Rodrigo Leite') # Passa só o nome.

  # Específica o atributo idade para passar a idade como argumento
  # diretamente para o campo correto.
  dados(idade=30)
```

# 03 - ( * ) args vs ( ** ) kwargs

Utilizamos as chamadas variáveis mágicas do Python:
 - ( * ) args;
 - ( ** ) kwargs

Não é necessário utilizar exatamente estes nomes: *args* e *kwargs*. Apenas o asterisco ( * ), ou dois deles ( ** ), será necessário.

Podemos optar, por exemplo, em escrever:
 - ( * ) var
 - ( **) vars

> Mas ( * ) args e ( ** ) kwargs é uma convenção entre a comunidade Python.

### 03.1 - ( * )args

Primeiro vamos aprender a usar o ( * ) args:

> Que significa que o programador ainda não sabe de antemão quantos argumentos serão passados para sua função, apenas que são muitos.

Então, neste caso usamos a palavra chave ( * ) args. Por exemplo:

 - O asterisco ( * ) executa um empacotamento dos dados para facilitar a passagem de parâmetros;
 - E a função que recebe este tipo de parâmetro é capaz de fazer o desempacotamento.

### 03.2 - ( ** ) kwargs

O ( ** ) kwargs permite que passemos uma variável do tipo ***chave-value*** como argumentos para uma função (como elementos de um dicionário).

**OBSERVAÇÕES - PARTE01:**  
 - O ( * ) args não sabe de antemão quantos argumentos vão ser passados;
 - O ( * ) args pode receber como argumento uma tupla ou lista como argumento;
 - O ( ** ) kwargs recebe como argumento uma variável do tipo *chave-value*;
 - O ( ** ) kwargs pode receber como argumento um *dicionário* como argumento - (chave-valor).

**OBSERVAÇÕES - PARTE02:**
 - Lembre que nós 2 casos de ( * ) args e ( ** ) kwargs quando nós passamos argumentos para as funções nós precisamos sempre adicionar os asteriscos:
   - test('Python', *lista)
   - chave_value(**dicionario)

```python
# Exemplo de função comm *args:
def test_args(first, *args):
  print('O primeiro argumento: {}'.format(first))
  for n in args:
    print('Outro argumento: {}'.format(n))

# Exemplo de função comm **kwargs:
def chave_value(**kwargs):
  for key, value in kwargs.items():
    print('{0}: {1}'.format(key, value))

if __name__ == "__main__":
  # O argumento Python=(first) é como qualquer outro parâmetro de função, só que vai ser o primeiro.
  # Já o args recebe múltiplos parâmetros. Viu como é fácil?
  test_args('Python', 'é', 'muito', 'legal')

  print()

  # Também poderíamos conseguir o mesmo resultado passando um list ou tuple
  # como argumentos, acrescido do asterisco:
  lista = [20, 30, 40] # Exemplo com lista.
  test_args(10, *lista)
  tupla = ('Amazon', 'Microsoft', 'Apple') # Exemplo com tupla.
  test_args('Google', *tupla)

  print()

  # [**kwargs] - Passando argumentos para a função "chave_value":
  chave_value(empresa='Google')
  # Também podemos passar um dicionário acrescido de dois símbolos asterisco
  # já que se trata de chave e valor:
  dicionario = {'nome': 'Rodrigo Leite da Silva', 'idade': 30}
  chave_value(**dicionario)
```

# 04 - Funções de Primeira Classe (First-Class Functions)

***Objetos de primeira classe*** em uma linguagem de programação são tratados uniformemente por toda parte:
 - Eles podem ser armazenados em estruturas de dados;
 - Passados como argumentos;
 - Ou usados em estruturas de controle.

> Uma linguagem de programação diz que suporta funções de primeira classe se trata funções como objetos de primeira classe... ***O Python suporta o conceito de funções de primeira classe***.

Propriedades de funções de primeira classe:
 - 01 - Uma função é uma instância do tipo de objeto;
 - 02 - Você pode armazenar uma função em uma variável;
 - 03 - Você pode passar a função como argumento para outra função;
 - 04 - Você pode retornar a função de uma função;
 - 05 - Você pode armazená-las em estruturas de dados, como tabelas de hash, listas,…


```python
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
```

# 05 - x

**Rodrigo Leite** *- Software Engineer*
