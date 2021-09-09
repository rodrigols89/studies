# Estruturas de Dados simples - notes

> Minhas observaçõs sobre algumas estruturas de dados.

# 01 - Fatiamento (Slicing)

Para trabalhar com fatiamento (Slicing) é importante lembrar, das seguintes regras/notas:

 - Parâmetros => [START : END : STEP]

**(START):**  
Onde vai COMEÇAR o fatiamento. Ou seja, apartir de qual índice(index) vaicomeçar o fatiamento. Esse índice pode ser omitido, por exemplo:

```
[:2]
```

que significa que vai começar do elemento índice 0 até o elemento do índice 2.

**(END):**  
Onde vai ACABAR o fatiamento. Ou seja, qual o último índice(index), porém vale lembrar que o elemento desse índice não é capturado, ou seja, não vamos exibir esse elemento em um retorno por exemplo. Também podemos omitir o fim de um fatiamento, por exemplo:

```python
[2:]
```

Que significa que o elemento no índice 2 até o último elemento de uma list por exemplo.

**(STEP):**  
O "step" são passos ou regras que podemos aplicar em um fatiamento. Por exemplo:

```python
[0:20:3]
```

Que significa que vai começar do elemento no índice 0 até o elemento no índice 20 com um step de 3 elementos, ou seja, pulando 3 índices.

```python
# Lista para trabalharmos.
lista = [2, 3, 5, 7, 11, 15, 30, 45, 50, 80]

# Pega os elementos do índice 0 até o índice 2.
# OBS: Lembrando que o do índice 2 não vai ser pego.
print(lista[0:2])
print(lista[:2])

# Pega os elementos apartir do índice 2 até o último elemento.
# OBS: Veja que como não definimos o último índice, ele pega TODOS.
print(lista[2:])

# Pega os elementos apartir do índice 2 até o índice 4.
# OBS: Lembrando que o do índice 4 não vai ser pego.
print(lista[2:4])
```

# 02 - Range
O **range()** é um tipo de seqüência "imutável" de números e é comumente usado para looping de um número específico de vezes em um comando "for" já que representam um intervalo.

O comando range() gera um valor contendo números inteiros sequenciais, obedecendo a sintaxe:

 - Sintaxe: range(inicio, fim)

**OBS:**  
O número finalizador, o "fim", não é incluído na sequência.

```python
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
```

# 03 - Conjuntos
Um conjunto, diferente de uma sequência, é uma coleção NÃO ORDENADA e que NÃO ADMITE ELEMENTOS DUPLICADOS. **"Chaves"** ou a função **"set()"** podem ser usados para criar conjuntos.

**OBS:**  
 - Para criar um conjunto vazio você tem que usar set(), não {};
 - O segundo cria um dicionário vazio - {}

```python
frutas = {'Laranja', 'Pera', 'Uva', 'Laranja', 'Banana', 'Pera', 'Banana'}
print(frutas)
print(type(frutas))
```

Os objetos de um conjunto também suportam operações matemáticas como:
 - União
 - Interseção
 - Diferença
 - Diferença Simétrica

Podemos transformar um texto em um conjunto com a frunção set() e testar as operações:

```python
# Cria conjuntos com a função set()
a = set('abacate')
print(type(a))
b = set('abacaxi')
print(type(b))

print(a) # Imprime o conjunto "a"
print(b) # Imprime o conjunto "b"
print(a - b) # Diferença dos conjuntos "a" e "b"
print(a | b) # União dos conjuntos "a" e "b"
print(a & b) # Interseção dos conjuntos "a" e "b"
print(a ^ b) # Diferença simétrica dos conjuntos "a" e "b"
```

# 04 - Dicionários
Os dicionários são estruturas poderosas e muito utilizadas já que podemos acessar seus elementos através de chaves e não de sua posição.

> Em outras linguagens este tipo é conhecido como **"matrizes associativas".**

Qualquer chave de um dicionário é associada (ou mapeada) a um valor. Os valores podem ser qualquer tipo de dado do Python. Portanto, os dicionários são pares de **"CHAVE-VALOR"** NÃO ORDENADOS.

```python
# Exemplo de um dicionário para representar um cadastro de uma pessoa.
pessoa = {"nome": 'Rodrigo', 'idade': 29, 'cidade': 'Campina Grande'}
print(pessoa)
print(type(pessoa))
```

Não é possível acessar um elemento de um dicionário por um índice como na lista. Devemos acessar por sua "chave":

```python
print(pessoa['nome'])
print(pessoa['idade'])
```

Se precisarmos adicionar algum elemento, por exemplo o "país", basta fazermos:

```python
pessoa['país'] = 'Brasil'
print(pessoa)
```

Um dicionário possui um método para retornar as suas keys - **keys()**

```python
print(pessoa.keys())
```

Um dicionário também possui um método para retornar valores - **values()**

```python
print(pessoa.values())
```

Também podemos criar dicionários utilizando a função - **dict()**

```python
a = dict(um=1, dois=2, três=3)
print(a)
```

**Rodrigo Leite** *- Software Engineer*
