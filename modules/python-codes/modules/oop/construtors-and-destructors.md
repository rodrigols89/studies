# Construtores & Destruidores

## Conteúdo

 - [01 - Palavra reservada "self"](#01)
 - [02 - Construtores em Python: `__init__`](#02)
   - [02.1 - Adicionando valores default para os nossos construtores](#02-1)
   - [02.2 - Passando argumentos para o nosso construtor por Posição vs Keywords](#02-2)
 - [03 - Destruidores em Python](#destructors)

---

<div id="01"></div>

## 01 - Palavra reservada "self"

A primeira coisa que você tem que saber quando estiver aprendendo sobre métodos de classes em Python é que todos os métodos utilizam a **palavra reservada *"self"***.

Nós não damos um valor para este parâmetro quando chamamos o método, *o Python fornece*. Se temos um método que não aceita nenhum argumento, ainda assim temos que ter um argumento ***self***.

Por exemplo, vamos criar uma objeto que vai representar uma pessoa com um método que diz apenas **"Hello World"**:

[person_say_hello.py](src/person_say_hello.py)
```python
class Person():

  def say_hello(self):
    print("Hello World!")

if __name__ == "__main__":
  p = Person()
  p.say_hello()
```

**OUTPUT:**  
```python
Hello World!
```

**NOTE:**  
Vejam que mesmo sem termos definido nenhum parâmetro para o método **say_hello()**, mesmo assim ele ainda deve utilizar a palavra reservada **"self"**.

---

<div id="02"></div>

## 02 - Construtores em Python: `__init__`

O método `__init__` é semelhante aos construtores em C++ e Java. É executado assim que um objeto de uma classe é instanciado. O método é útil para fazer qualquer inicialização que você queira fazer com seu objeto.

Veja o exemplo abaixo:

[construtor_init-v1.py](src/construtor_init-v1.py)
```python
class Person:
  
  def __init__(self, name):
    self.name = name
    
  def say_name(self):
    print('Hello, my name is:', self.name)
    
if __name__ == "__main__":
  p = Person('Rodrigo')
  p.say_name()
```

**OUTPUT:**  
```python
Hello, my name is: Rodrigo
```

> Ok, mas o que esse tal construtor `__init__` tem de tão importante?

Vocês concordam comigo que toda pessoa tem que ter um nome? Agora vamos tentar executar novamente nosso programa em Python sem passar nenhum argumento para nosso construtor, ou seja, não vamos passar nenhum nome para o nosso objeto:

```python
class Person:
  
  def __init__(self, name):
    self.name = name
    
  def say_name(self):
    print('Hello, my name is:', self.name)
    
if __name__ == "__main__":
  p = Person()
  p.say_name()
```

**OUTPUT:**  
```python
Traceback (most recent call last):
  File "....", line 15, in <module>
    p = Person()
TypeError: __init__() missing 1 required positional argument: 'name'
```

Veja que agora nós temos um erro como retorno. Isso porque o nosso construtor não tem nenhum valor default para o atributo *name*.

**NOTE:**  
Uma das vantagens desse método é que você meio que **obriga** a quem está criando (instanciando) um objeto *pessoa* passar um nome para o mesmo. Como nós já falamos antes, não faz sentido ter uma pessoa sem nome.

<div id="02-1"></div>

## 02.1 - Adicionando valores default para os nossos construtores

É comum na programação nós também deixarmos alguns atributos default (padrão) na inicialização de nossos objetos.

Isso também não quer dizer que quem está criando (instanciando) o objeto não possa alterar. Isso significa que se nenhum valor for passado como argumento para esse atributo o método construtor `__init__` utilizará o valor default.

Vamos novamente criar um objeto para representar uma pessoa, porém, esse vai ter vários atributos, alguns default e outros não:

[person.py](src/person.py)  
```python
class Person:
  
  def __init__(self, nome, idade=None, numero_olhos = 2, naturalidade = "Brazil"):
    self.nome = nome
    self.idade = idade
    self.numero_olhos = numero_olhos
    self.naturalidade = naturalidade
    
if __name__ == "__main__":
  p = Person('Rodrigo')
  print(p.__dict__)
```

**OUTPUT:**  
```python
{'nome': 'Rodrigo', 'idade': None, 'numero_olhos': 2, 'naturalidade': 'Brazil'}
```

**NOTE:**  
Agora nós vamos analisar dois pontos muito importantes:

 - **PRIMEIRO:**
   - Nós utilizamos o método `__dict__` que retorna para nós nosso objeto como um dicionário, onde:
     - A **chave** representa os **atributos**;
     - E os valores são realmente os valores do nosso objeto.
 - **SEGUNDO:**
   - Agora vamos analisar cada atributo do nosso objeto:
     - **nome:** O nome era obrigado pois não tinha nenhum valor default (padrão);
     - **idade:** Esse eu não passei de proposito só para deixar claro que nós podemos utilizar o **"None"** como um valor default para algum atributo do nosso construtor;
     - **numero_olhos:** Bem, a menos que você venha de outro planeta o número de olhos de uma pessoa normal são 2 mesmo, por isso, eu deixei os valores padrão. Mas nada impede de você alterar e colocar 1, caso você tenha perdido um deles;
     - **naturalidade:** Como eu sou Brasileiro vou partir do pressuposto que todos que vão ler aqui também são. Mas nada impede de você alterar para a sua nacionalidade *(por exemplo, Jamaica)*.

<div id="02-2"></div>

## 02.2 - Passando argumentos para o nosso construtor por Posição vs Keywords

Existem duas maneiras lógicas de passar argumentos para os atributos do nosso construtor:

 - Pelo a posição que o atributo foi declarado no construtor;
 - Ou pelo a Keywords.

Veja o código abaixo para ficar mais claro:

[position_vs_keywords.py](src/position_vs_keywords.py)
```python
class Person:
  
  def __init__(self, nome, idade=None, numero_olhos = 2, naturalidade = "Brazil"):
    self.nome = nome
    self.idade = idade
    self.numero_olhos = numero_olhos
    self.naturalidade = naturalidade
    
if __name__ == "__main__":
  p1 = Person('Rodrigo', 32, 2, "EUA")
  p2 = Person(nome="Isaac Newton", idade=80, numero_olhos=1, naturalidade="Reino Unido")

  print(p1.__dict__)
  print(p2.__dict__)
```

**OUTPUT:**  
```python
{'nome': 'Rodrigo', 'idade': 32, 'numero_olhos': 2, 'naturalidade': 'EUA'}
{'nome': 'Isaac Newton', 'idade': 80, 'numero_olhos': 1, 'naturalidade': 'Reino Unido'}
```

Veja que no nosso primeiro objeto **p1** nós inicializamos os atributos por posição; Enquanto o segundo **p2** nós inicializamos por Keywords.

**NOTE:**  
Se você recebeu um método e não sabe quais parâmetros foram definidos é muito simples:

 - Assim que você fechar o método, por exemplo **print(aqui dentro)**, dentro do parênteses você vai ver as definições do método;
 - Outra abordagem é **segurar Ctrl e clica no método** *(depende do seu editor de texto)* que vai abrir o **builtins.pyi**.

---

<div id="destructors"></div>

## 03 - Destruidores em Python

> **Destrutores** são chamados quando um objeto é destruído. Em Python, os destruidores não são tão necessários quanto em C++ porque Python tem o **Garbage Collector (coletor de lixo)** que lida com o gerenciamento de memória automaticamente. 

O método `__del__()` é conhecido como método destruidor em Python. Ele é chamado quando todas as referências ao objeto foram excluídas, ou seja, quando um objeto é coletado como lixo. 

Por exemplo, vejam o código abaixo:

[destructors-01.py](src/destructors-01.py)
```python
class Employee:

	def __init__(self):
		print('Employee created.')

	def __del__(self):
		print('Destructor called, Employee deleted.')

obj = Employee()
del obj
```

**OUTPUT:**  
```python
Employee created.
Destructor called, Employee deleted.
```

**NOTE:**  
Não é comum programadores Python ficarem se preocupando com o uso de memória, mas em alguns programas que exigem alta performance é bom saber quando utillizar.

---

**REFERÊNCIAS:**  
[Python Impressionador: Curso de Python Completo](https://www.hashtagtreinamentos.com/curso-python)
