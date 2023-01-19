# Iteráveis, Iterator, Generator (+yield)

> A maioria dos exemplos abaixo foram testados (criados) com <u>IPython</u>.

## Contents

 - **Iteráveis:**
   - [Introdução às variáveis (objetos) iteráveis](#intro)
 - **Iterator:**
   - [Introdução ao Iterator](#intro-to-iterator)
 - **Generator:**
   - [Funções geradoras com yield](#yield-functions)
 - **Tips & Tricks:**
   - [Iterator (Ideia principal)](#idea)
   - [[Tamanho em Byte] - Lista normal x List Generator/Iterators (List Comprehension)](#byte)
   - [return vs. yield](#return-yield)

---

<div id="intro"></div>

## Introdução às variáveis (objetos) iteráveis

A primeira coisa que nós vamos aprender é descobrir se o que tem dentro de uma variável é um **iterável**. Por exemplo, vejam a lista, dicionário e tupla abaixo:

**IPython:**
```python
In [2]: l = [1, 2, 2, 3, 5]

In [3]: d = {'x': 1, 'y': 2, 'z': 3}

In [4]: t = (1, 2, 3, 4, 5)
```

> **Ok, agora como eu sei se essas variáveis são iteráveis?**

Para saber se uma variável **x** é um iterável basta chamar a função **hasattr()** do Python e passa como argumento à variável e `__iter__`.

> **Ou seja, nós estamos testando se uma variável tem o método `__iter__`.**

Vamos ver na prática agora:

**IPython:**
```python
In [12]: hasattr(l, '__iter__')
Out[12]: True

In [13]: hasattr(d, '__iter__')
Out[13]: True

In [14]: hasattr(t, '__iter__')
Out[14]: True
```

Vejam que listas, dicionários e tuplas são iteráveis.

> **Mas e strings e números são iteráveis?**

**IPython:**
```python
In [15]: s = "string"
In [16]: hasattr(s, '__iter__')
Out[16]: True

In [17]: n = 123456
In [18]: hasattr(n, '__iter__')
Out[18]: False
```

**NOTE:**  
Vejam que strings são iteráveis, porém, números (int) não são.

> **Mas o que significa uma variável ser <u>iterável</u>?** <u>Significa que nós podemos iterar pelos seus elementos (por exemplo, com um "for" statement)</u>.

**IPython:**
```python
In [19]: for item in l:
    ...:     print(item)
    ...: 
1
2
2
3
5


In [20]: for item in d:
    ...:     print(item)
x
y
z


In [21]: for item in t:
    ...:     print(item)
1
2
3
4
5


In [23]: for item in s:
    ...:     print(item)
s
t
r
i
n
g


TypeError                                 Traceback (most recent call last)
Input In [22], in <cell line: 1>()
----> 1 for item in n:
      2     print(item)

TypeError: 'int' object is not iterable
```

Vejam que nós conseguimos iterar pelos elementos de quase todas variáveis, menos a **n**, pois ela não é um iterável.

> **Mas como o statement "for" consegue aplicar essa iteração por cada elemento?**

---

<div id="intro-to-iterator"></div>

## Introdução ao Iterator

Na verdade, o Python pega a variável iterável que nós passamos para o statement **for** e transforma ela em um <u>Iterator</u> com a função **iter()** do Python e utiliza o método interno **next()** que é responsável por pegar o próximo elemento de um Iterator toda vez que for chamado.

Por exemplo, vamos testar se nossas variáveis (objetos) tem o método **next()**:

**IPython:**
```python
In [33]: hasattr(l, '__next__')
Out[33]: False

In [34]: hasattr(d, '__next__')
Out[34]: False

In [35]: hasattr(t, '__next__')
Out[35]: False

In [36]: hasattr(s, '__next__')
Out[36]: False
```

**NOTE:**  
Vejam que as variáveis (objetos) não tem a função **next()**. Isso, porque nós ainda não transformamos elas em <u>Iterator</u>  como o statement **for** faz.

Por exemplo, vamos transformar nossas variáveis (objetos) em <u>Iterators</u> e depois testar se elas tem a função **next()**:


**IPython:**
```python
In [39]: l = iter(l)
In [40]: hasattr(l, '__next__')
Out[40]: True


In [41]: d = iter(d)
In [42]: hasattr(d, '__next__')
Out[42]: True


In [43]: t = iter(t)
In [44]: hasattr(t, '__next__')
Out[44]: True


In [45]: s = iter(s)
In [46]: hasattr(s, '__next__')
Out[46]: True
```

**NOTE:**  
Nice, vejam que agora nossas variáveis (objetos) podem desfrutar da função **next()**.

> **Mas o que isso muda?**

Muda, que nós conseguimos agora aplicar a mesma abordagem do statement **for** que utiliza a função **next()** para iterar pelos elementos de um iterável.

Veja o exemplo abaixo:

**IPython:**
```python
In [9]: next(l)
Out[9]: 1
In [10]: next(l)
Out[10]: 2
In [11]: next(l)
Out[11]: 2
In [12]: next(l)
Out[12]: 3
In [13]: next(l)
Out[13]: 5



In [55]: next(d)
Out[55]: 'x'
In [56]: next(d)
Out[56]: 'y'
In [57]: next(d)
Out[57]: 'z'



In [23]: next(t)
Out[23]: 1
In [24]: next(t)
Out[24]: 2
In [25]: next(t)
Out[25]: 3
In [26]: next(t)
Out[26]: 4
In [27]: next(t)
Out[27]: 5



In [30]: next(s)
Out[30]: 's'
In [31]: next(s)
Out[31]: 't'
In [32]: next(s)
Out[32]: 'r'
In [33]: next(s)
Out[33]: 'i'
In [34]: next(s)
Out[34]: 'n'
In [35]: next(s)
Out[35]: 'g'
```

---

<div id="yield-functions"></div>

## Funções geradoras com yield

> A palavra-chave **yield** pode ser usada no corpo de qualquer função para transformar a mesma (função) em um iterável.

**What? Como assim função iterável?**  
Sim, nós podemos criar funções/métodos que podem ser iteráveis. Por exemplo, veja uma função iterável abaixo e como iterar por ela com o statement **"for"** e a função **next()**:

**IPython:**
```python
In [1]: def generator():
   ...:     yield 'A'
   ...:     yield 'B'
   ...:     yield 'C'
   ...: 


In [2]: generator()
Out[2]: <generator object generator at 0x7f03582dce40>

In [4]: for item in generator():
   ...:     print(item)
   ...: 
A
B
C


In [32]: g = generator()
In [33]: next(g)
Out[33]: 'A'
In [34]: next(g)
Out[34]: 'B'
In [35]: next(g)
Out[35]: 'C'
```

**NOTE:**  

 - **Só para ficar claro toda vez que a função iterável (feita com yield) for chamada:**
   - Ela vai parar em determinado **yield** e gera um valor para quem chamou a função;
   - Quando a função for chamada novamente, ela vai parar no próximo **yield** e gerar outro valor;
   - E assim, sucessivamente... Até gerar um exceção ou você criar uma condição para ela parar.

**NOTE:**  
Outra observação crucial aqui é que a saída da função é um generator e não a função em sí. Por exemplos, vamos testar os tipos:

**IPython:**
```python
In [36]: def generator():
    ...:     yield 'A'
    ...:     yield 'B'
    ...:     yield 'C'


In [39]: type(generator)
Out[39]: function

In [41]: g = generator()
In [42]: type(g)
Out[42]: generator

In [44]: type(generator()) <-- Esse exemplo pega a saída da função.
Out[44]: generator
```

---

<div id="idea"></div>

## Iterator (Ideia principal)

> A ideia principal de um <u>Iterator</u> é resolver o problema de trabalhar com sequências que não cabem na memória. Por exemplo:

 - Um arquivo muito grande (Por exemplo, CSV):
   - Outro exemplo é você ter um arquivo de 10Gb e sua memória RAM ser apenas de 8Gb. Isso, seria um problema, pois vocẽ não teria memória suficiente para abrir todo o arquivo.
 - Uma resposta complexa de Banco de Dados...

---

<div id="byte"></div>

## [Tamanho em Byte] - Lista normal x List Generator/Iterators (List Comprehension)

Bem, antes de nós verificarmos a diferença de uma <u>lista normal</u> e uma <u>lista generator</u> vamos revisar como criar listas com **List Comprehension**.

A sintaxe para criar uma **List Comprehension** é a seguinte:

```python
var = [expr for item in list]
```

Ok, vamos criar uma lista com 100 elementos seguindo essa sintaxe:

**IPython:**
```python
l = [x for x in range(100)]
In [47]: type(l)
Out[47]: list
```

Ótimo, vejam que nós temos um objeto do tipo lista. Mas como eu consigo criar uma <u>lista generator</u> com **List Comprehension**?

> Simples, basta trocar o **colchetes []** por **parênteses ()**.

**IPython:**
```python
In [48]: l2 = (x for x in range(100))
In [49]: type(l2)
Out[49]: generator
```

**NOTE:**  
Vejam que nós criamos um **generator** e não uma tupla como muitos imaginariam. <u>Mas esse efeito só é satisfeito com **List Comprehension**</u>.

Agora que nós já sabemos como criar uma <u>lista normal</u> e uma <u>lista generator</u> com **List Comprehension** vamos ver se existem alguma diferença de tamanho entre elas em **Bytes**.

**IPython:**
```python
In [51]: import sys


In [52]: normal_list = [x for x in range(100)]
In [53]: generator_list2 = (x for x in range(100))

In [54]: sys.getsizeof(normal_list)
Out[54]: 920
In [56]: sys.getsizeof(generator_list2)
Out[56]: 112
```

**NOTE:**  
Vejam que nós temos uma diferença absurda em Bytes que foram alocados entre a <u>lista normal</u> e a <u>lista generator</u>.

> **E se eu continuar aumentando o tamanho dos elementos que eu quero nas listas?**

**IPython:**
```python
In [57]: normal_list = [x for x in range(1000)]
In [58]: generator_list = (x for x in range(1000))

In [60]: sys.getsizeof(normal_list)
Out[60]: 8856
In [61]: sys.getsizeof(generator_list)
Out[61]: 112
```

Ué, a <u>lista normal</u> aumentou o tamanho em Bytes, porém, a <u>lista generator</u> continua consumindo o mesmo tamanho em bytes.

> **Por que?**

**NOTE:**  
 - Isso acontece porque a <u>lista normal</u> aloca memória para todos os elementos de uma vez na memória;
 - E a <u>lista generator</u> não vai alocar todos os valores na memória, ele só vai pegar um valor quando você pedir:
   - Para pedir esses valores você pode utilizar o statement **for** ou a função **next()**.


Por exemplo, veja o código abaixo:

**IPython:**
```python
In [22]: l = (x for x in range(10))
In [23]: next(l)
Out[23]: 0
In [24]: next(l)
Out[24]: 1
In [25]: next(l)
Out[25]: 2
In [26]: next(l)
Out[26]: 3
In [27]: next(l)
Out[27]: 4
In [28]: next(l)
Out[28]: 5
In [29]: next(l)
Out[29]: 6
In [30]: next(l)
Out[30]: 7
In [31]: next(l)
Out[31]: 8
In [32]: next(l)
Out[32]: 9


In [40]: for item in l:
    ...:     print(item)
0
1
2
3
4
5
6
7
8
9
```

**NOTE:**  
Só para fins de teste vamos criar uma lista normal, verificar o tamanho em Bytes, transformar em um iterator e depois verificar o tamanho em Bytes novamente.

**IPython:**
```python
In [43]: import sys

In [44]: l = [1, 2, 3, 4, 5]
In [45]: sys.getsizeof(l)
Out[45]: 120

In [46]: l = iter(l)

In [47]: sys.getsizeof(l)
Out[47]: 48
```

**NOTE:**  
Vejam que nós estamos otimizando o tamanho que nossas variáveis (objetos iteráveis) gastam em Bytes e isso é muito útil, pois, nós vamos consumir menos memória com nossos programas.

---

<div id="return-yield"></div>

## return vs. yield

 - Quando usamos o **return** dizemos que a função **"retorno algo"**.
 - Quando usamos o **yield** dizemos que  a função **"faz/gera algum tipo de valor"**.

---

**REFERENCES**  
[Geradores, Iteradores e Iteráveis em Python - Aula 25](https://www.youtube.com/watch?v=gHrc6FLBh20&list=LL&index=2&t=282s)  
[Live de Python #86 - Iteradores e Geradores](https://www.youtube.com/watch?v=Xj5LlCeW0m0)
[LIST COMPREHENSIONS NO PYTHON](https://pythonacademy.com.br/blog/list-comprehensions-no-python)  

---

**Rodrigo Leite -** *drigols*
