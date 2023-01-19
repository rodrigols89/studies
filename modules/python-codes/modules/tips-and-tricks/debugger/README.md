# Debugger

## Conteúdo

 - [01 - Ferramentas mais comuns para Debugger em python](#tools)
 - [02 - Problema inicial](#initial-problem)
 - [03 - Breakpoint()](#breakpoint)
 - [04 - Comandos do Pdb (help/h)](#pdb-commands)
 - [05 - Entendendo o comando l(ist)](#list)
 - [06 - Entendendo o comando next (n)](#next)
 - [07 - O que tem dentro da variável msg?](#next-variables)
 - [08 - Entendendo o comando step (s)](#step)
 - [09 - Entendendo o comando continue (c)](#continue)
 - [10 - Entendendo os comandos type() & whatis](#type-whatis)
 - [11 - Entendendo os comandos p, pp e vars()](#p-pp-vars)
 - [12 - Entendendo os comandos quit e exit](#quit-exit)

---

<div id="tools"></div>

## 01 - Ferramentas mais comuns para Debugger em python

Antes de iniciar nossos estudos sobre ***depuração*** vou listar algumas das ferramentas mais comuns do Python com abreviações e significados:

 - **Python DeBuger (PDB):**
   - Embutido no Python.
 - **IPython DeBuger (IPDB):**
   - pip install ipdb.
 - **Remote Python DeBuger (RPDB):**
   - pip install rpdb.
   - Debuger remoto,v ia netcat.
 - **Web Python DeBuger (Web PDB):**
   - pip install web_pdb.server
   - Debuger remoto utilizando o browser
 - **PySnooper:**
   - pip install pySnooper
 - **Integrações de IDEs:**
   - VSCode.
   - PyCharm.

---

<div id="initial-problem"></div>

## 02 - Problema inicial

Talvez uma das coisas mais complicadas para quem está começando com Python é entender como debugar no terminal. Agora vem a pergunta-chave:

> Por que nós precisamos aprender a **debugar** no terminal se podemos utilizar uma **IDE** com várias ferramentas prontas?

**RESPOSTA:**  
Existem cenários, onde, nós não vamos poder abrir nossos códigos em uma **IDE**. Por exemplo, imagine que nós estamos acessando uma máquina remota e precisamos debugar uma parte específica do código, como faríamos sem saber debugar pelo terminal (console)?

Por exemplo, imagine que nós temos o seguinte código:

[example-01.py](src/example-01.py)
```python
def say_hello(name, age):
  return 'Hello, my name is {name}, age {age}'


if __name__ =="__main__":
  name = "Rodrigo"
  age  = "32"

  msg = say_hello(name, age)

  # TEST!
  assert msg == 'Hello, my name is Rodrigo, age 32'
```

Agora nós vamos rodar o código acima, que vai nos gerar o seguinte resultado:

**OUTPUT:**  
```python
$ python example-01.py


Traceback (most recent call last):
  File "example-01.py", line 12, in <module>
    assert msg == 'Hello, my name is Rodrigo, age 32'
AssertionError
```

**Vejam que o nosso teste não passou:**  
 - Mas por quê?
 - E o que tem dentro da variável **msg**?
   - Que é o retorno da nossa função **say_hello()**.

**NOTE:**  
Uma das maneiras de saber o que tem dentro da variável **"msg"** é abrindo o arquivo no modo iterativo utilizando o argumento **-i**:

```python
Traceback (most recent call last):
  File "example-01.py", line 12, in <module>
    assert msg == 'Hello, my name is Rodrigo, age 32'
AssertionError
>>> msg
'Hello, my name is {name}, age {age}'
>>>
```

**Ué, não deveria ter o nome e idade passado para a função?**
Na verdade o que nós temos aqui é o famoso erro de **"Semântica"**.

> **Erro semântico:** É um erro na "lógica de seu código", em sua semântica, o código está sintaticamente correto, porém não faz o que se esperava dele. Por isso, este tipo de erro é geralmente mais difícil de ser identificado e corrigido.

**NOTE:**  
A verdade é que nem sempre nós vamos poder entrar no modo iterativo e fazer esse tipo de observação.

> **Ok, mas e o erro aqui qual é?**

**NOTE:**  
Na verdade o problema aqui é que nós esquecemos de utilizar o **f** para formatar a string, mas vamos imaginar que nós não sabemos ainda qual é o erro.

> **Como encontrar um erro que nós nem imaginamos ainda onde esta?**

---

<div id="breakpoint"></div>

## 03 - Breakpoint()

Agora nós vamos aprender o que é **Breakpoint()** que nada mais é que:

> **Um ponto de parada dentro do código**

Por exemplo, vamos voltar para o nosso código anterior:

[example-01.py](src/example-01.py)
```python
1  def say_hello(name, age):
2   return 'Hello, my name is {name}, age {age}'
3
4
5  if __name__ =="__main__":
6   name = "Rodrigo"
7   age  = "32"
8
9   breakpoint()
10
11  msg = say_hello(name, age)
12
13  # TEST!
14  assert msg == 'Hello, my name is Rodrigo, age 32'
```

Vejam que na linha 9 agora nós temos um **breakpoint()**, mas o que isso significa? Imagine que o compilador/interpretador está lá linha por linha, lendo funções, variáveis e etc...  Eassim, que ele chegar no **breakpoint()** na linha 9 ele vai parar! Agora vem a pergunta:

> **O que vem depois que ele parar?**

**NOTE:**  
Na verdade ele não vai *parar* a execução do programa e sim ele vai **"pausar"** e ficar esperando.

> **Mas esperando o que?**

Nós interagirmos com ele! Vamos agora rodar nosso exemplo novamente com o **breakpoint()** e ver o que acontece:

```python
example-01.py(11)<module>()
$ python example-01.py

-> msg = say_hello(name, age)
(Pdb)
```

**NOTE:**  
Olhando para a saída acima nós temos o seguinte:
 - O caminho onde está o arquivo;
 - Uma **seta (->)** apontando para a próxima instrução depois do nosso **breakpoint()**;
 - E também nós temos o **(Pdb)** que nós sabemos que é o **Python DeBuger** embutido no Python.
 - Por fim nós devemos observação que depois do nome do nosso arquivo nós temos **(11)**:
   - example-01.py(11)
     - Isso significa que o nosso programa está parado (pausado) na linha 11

Agora vamos no nosso **Pdb** e digitar **msg** que é a variável que deveria ter o retorno da nossa função:

```python
(Pdb) msg
*** NameError: name 'msg' is not defined
```

**What? Como assim msg ainda não foi definido?**  
Na verdade nós temos acesso a tudo que está antes do **breakpoint()**, lembrem que nós estamos parados (pausados) na linha 11, ou seja, ele chegou na linha 11 e pausou, mas não leu ou executou nada lá ainda.

Por exemplo, vamos interagir com o **Pdb** e ver se ele responde bem sobre as variáveis **"name"** e **"age"**:

```python
(Pdb) name
'Rodrigo'
(Pdb) age
'32'
(Pdb)
```

**NOTE:**  
Vejam que realmente condiz com o que eu falei, o **Pdb** tem tudo disponível, porém, ATÉ o **breakpoint()**.

---

<div id="pdb-commands"></div>

## 04 - Comandos do Pdb (help/h)

Bem, sabendo que nós estamos pausados na linha 11 e o **Pdb** está disponível para nós interagirmos com ele é importante nós sabermos que existem comandos que nós podemos passar para ele (Pdb).

Por exemplo, se você utilizar o comando **help** ou **h (abreviação de help)** o **Pdb** vai retornar uma lista com esses comandos:

```python
(Pdb) help

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where

Miscellaneous help topics:
==========================
exec  pdb
```

**NOTE:**  
Vejam que em alguns comandos nós temos o comando original e a abreviação para esse comando.

---

<div id="list"></div>

## 05 - Entendendo o comando l(ist)

O comando **l(ist)** vai listar 11 linhas em volta do nosso ponto de parada. Por exemplo, veja a saída abaixo:

```python
  6       name = "Rodrigo"
  7       age  = "32"
  8
  9       breakpoint()
 10
 11  ->   msg = say_hello(name, age)
 12
 13       # TEST!
 14       assert msg == 'Hello, my name is Rodrigo, age 32'
```

Vejam que nós temos uma **seta (->)** apontando para onde nós estamos parados (pausado) e 11 em volta (divido para cima e para baixo) do nosso ponto de parada.

**NOTE:**  
Nós também podemos utilizar o comando help (h) em conjunto com o comando **l(ist)** para ver a documentação do do comando **l(ist)**.

```python
(Pdb) h l
l(ist) [first [,last] | .]

        List source code for the current file.  Without arguments,
        list 11 lines around the current line or continue the previous
        listing.  With . as argument, list 11 lines around the current
        line.  With one argument, list 11 lines starting at that line.
        With two arguments, list the given range; if the second
        argument is less than the first, it is a count.

        The current line in the current frame is indicated by "->".
        If an exception is being debugged, the line where the
        exception was originally raised or propagated is indicated by
        ">>", if it differs from the current line.
(Pdb)
```

---

<div id="next"></div>

## 06 - Entendendo o comando next (n)

Agora nós vamos entender como funciona o comando **next** que nada mas é que andar no nossso ponto de parada para a próxima instrução, ou conjunto de instruções internas (por exemplo, uma função).

**Não entendeu?**  
Nós não estavamos parado na linha 11?

```python
> example-01.py(11)<module>()
-> msg = say_hello(name, age)
(Pdb) list
  6       name = "Rodrigo"
  7       age  = "32"
  8
  9       breakpoint()
 10
 11  ->   msg = say_hello(name, age)
 12
 13       # TEST!
 14       assert msg == 'Hello, my name is Rodrigo, age 32'
```

**Se eu der o comando next o que vai acontecer?**

```python
(Pdb) next
example-01.py(14)<module>()
-> assert msg == 'Hello, my name is Rodrigo, age 32'
(Pdb) list
  9       breakpoint()
 10
 11       msg = say_hello(name, age)
 12
 13       # TEST!
 14  ->   assert msg == 'Hello, my name is Rodrigo, age 32'
```

**NOTES:**  
 - Vejam que agora a nossa **seta (->)** está apontando para a linha 14, ou seja, o comando next (n) pula instruções e não linhas.
 - Só para relembrar, o **Pdb** ainda não executou a linha 14, ele apenas está apontando para lá que é o nosso ponto de parada.

---

<div id="next-variables"></div>

## 07 - O que tem dentro da variável msg?

Bem, como nós sabemos antes não dava para saber o que tinha dentro da variável **msg** porque o nosso **breakpoint()** tinha pausado a compilação/interpretação antes desse ponto. Mas, como nós utilizamos o comando **next** para o nosso ponto de parada pular para a próxima instrução agora nós podemos ver o que tem na variável **msg**:

```python
(Pdb) msg
'Hello, my name is {name}, age {age}'
```

Opa, vejam que o problema é realmente o que nós estavamos pensando, faltou formatar a string com **f**.

---

<div id="step"></div>

## 08 - Entendendo o comando step (s)

Agora pensem comigo quando eu utilizo o comando **next** a nossa seta **(->)** não deveria ter entrado na função e ter parado lá? Pensando por esse lado sim, pois era a próxima instrução.

**NOTE:**  
O que acontece é que o **next** executa uma instrução completa de uma linha. Ou seja, se essa linha tiver instruções interna, por exemplo, execução de uma função ela vai rodar tudo e ir para a próxima instrução.

Agora vem outra pergunta-chave:

> E se eu quiser que o **Pdb** vá **PASSO** a **PASSO** até a parte interna da função?

**Utilize o comando step (s):**  
Com o comando step (s) nós conseguimos aplicar esse conceito, vejam o exemplo abaixo passo a passo:

```python
$ python example-01.py
example-01.py(11)<module>()
-> msg = say_hello(name, age)
(Pdb) list
  6       name = "Rodrigo"
  7       age  = "32"
  8
  9       breakpoint()
 10
 11  ->   msg = say_hello(name, age)
 12
 13       # TEST!
 14       assert msg == 'Hello, my name is Rodrigo, age 32'
[EOF]
(Pdb) step

--Call--
example-01.py(1)say_hello()
-> def say_hello(name, age):
(Pdb) list
  1  -> def say_hello(name, age):
  2       return 'Hello, my name is {name}, age {age}'
  3
  4
  5     if __name__ =="__main__":
  6       name = "Rodrigo"
  7       age  = "32"
  8
  9       breakpoint()
 10
 11       msg = say_hello(name, age)
(Pdb) step

example-01.py(2)say_hello()
-> return 'Hello, my name is {name}, age {age}'
(Pdb) list
  1     def say_hello(name, age):
  2  ->   return 'Hello, my name is {name}, age {age}'
  3
  4
  5     if __name__ =="__main__":
  6       name = "Rodrigo"
  7       age  = "32"
  8
  9       breakpoint()
 10
 11       msg = say_hello(name, age)
(Pdb) step

--Return--
example-01.py(2)say_hello()->'Hello, my na...e}, age {age}'
-> return 'Hello, my name is {name}, age {age}'
(Pdb) list
  1     def say_hello(name, age):
  2  ->   return 'Hello, my name is {name}, age {age}'
  3
  4
  5     if __name__ =="__main__":
  6       name = "Rodrigo"
  7       age  = "32"
  8
  9       breakpoint()
 10
 11       msg = say_hello(name, age)
(Pdb) step

example-01.py(14)<module>()
-> assert msg == 'Hello, my name is Rodrigo, age 32'
(Pdb) list
  9       breakpoint()
 10
 11       msg = say_hello(name, age)
 12
 13       # TEST!
 14  ->   assert msg == 'Hello, my name is Rodrigo, age 32'
```

**NOTE:**  
Vejam que com o comando **step (s)** nós vamos executando instrução por instrução, mesmo que tenham instruções internas. Diferente do comando **next** que executa todas as instruções de uma linha, mesmo que essa linha tenha instruções internas (como uma função).

---

<div id="continue"></div>

## 09 - Entendendo o comando continue (c)

A primeira coisa que vocês tem que ter em mente é que:

> **O comando *continue* executa um intervalo de instruções entre um *breakpoint()* e outro.**

**What? Como assim?**  
Vocês já pararam para pensar que em alguns momentos nós vamos precisar **debugar** partes do nosso código separadamente? Então, o comando **continue** em conjunto com **breakpoint()** possibilita isso.

Por exemplo, vejam o código abaixo:

[continue.py](src/)
```python
name = "Rodrigo"
age  = 32

breakpoint()

msg = "Hello World!"
employee = "Jobson"

breakpoint()

bye = "Good bye!"
```

**PDB:**  

```python
$ python continue.py
> continue.py(9)<module>()
-> msg = "Hello World!"
(Pdb) name
'Rodrigo'
(Pdb) age
32
(Pdb) msg
*** NameError: name 'msg' is not defined
(Pdb) continue
> continue.py(14)<module>()
-> bye = "Good bye!"
(Pdb) msg
'Hello World!'
(Pdb) employee
'Jobson'
(Pdb) bye
*** NameError: name 'bye' is not defined
(Pdb) continue
```

Olhando para o código acima e a depuração que foi feita nós temos o seguinte:

 - Como não tinha nenhum comando **breakpoint()** no início do arquivo ele já reconheceu as variáveis **name** e **age** e parou na linha 9;
 - Quando nós executamos o **continue** o *PDB* pulou para o próximo ponto de parada na linha 14, ou seja, o próximo **breakpoint()** e também já leu mais duas variáveis que eram **msg** e **employee**
 - Por fim, quando nós executamos o comando **continue** acabou a depuração já que não tinha mais **breakpoint()**:
   - Ou seja, não teve como a gente ver o tinha na variável **bye**.
   - Se você tiver interesse pode adicionar mais um **breakpoint()** depois desse ponto de parada para testar o que tinha na variável **bye** para caso de estudo.

**NOTE:**  
O mais importante a observar aqui é que o comando **continue** executa um intervalo de instruções entre um **breakpoint()** e outro, não importa quantas instruções tem entre um e outro, ele vai ler tudo que tiver entre um **breakpoint()** e outro e pausar. E isso é crucial para debugar partes do código sem precisar ficar rodando várias vezes os comando **next** ou **step**. 

---

<div id="type-whatis"></div>

## 10 - Entendendo os comandos type() & whatis

E se em algum momento nós precisarmos saber qual o tipo de uma variável como faz? Para isso você pode utilizar os comando **type()** e **whatis** do *PDB*:

Veja o exemplo abaixo:

```python
$ python example-01.py
> example-01.py(11)<module>()
-> msg = say_hello(name, age)
(Pdb) type(name)
<class 'str'>
(Pdb) whatis name
<class 'str'>
(Pdb) type(age)
<class 'str'>
(Pdb) whatis age
<class 'str'>
```

**NOTE:**  
Vejam como os comandos **types()** e **whatis** são úteis, principalmente, quando estamos debugando um código de outra pessoa e não sabemos muito bem o que está acontecendo.

---

<div id="p-pp-vars"></div>

## 11 - Entendendo os comandos p, pp e vars()

Resumidamente, os comandos **p**, **pp** e **vars()** fazem o seguinte:

 - **p:**
   - O comando **p (de print)** printa algo no *PDB*.
 - **pp:**
   - O comando **pp (de pretty)** printa algo no *PDB*, porem, mais bonitinho (ou formatado).
 - **vars()**
   - O comando **vars()** retorna todas as variáveis que já estão definidas atualmente e seus valores:

Vamos começar com o seguinte código:

[example-03.py](src/example-03.py)
```python
breakpoint()

name = "Rodrigo"
age  = 32

breakpoint()

msg = "Hello World!"
```

Agora vamos fazer alguns exemplos de **p** e **pp**:

```python
$ python example-03.py
> example-03.py(3)<module>()
-> name = "Rodrigo"
(Pdb) p name
*** NameError: name 'name' is not defined
(Pdb) p age
*** NameError: name 'age' is not defined
(Pdb) continue
> example-03.py(8)<module>()
-> msg = "Hello World!"
(Pdb) p name
'Rodrigo'
(Pdb) pp name
'Rodrigo'
(Pdb) p age
32
(Pdb) p "I Love You"
'I Love You'
(Pdb) pp "Oh my God!"
'Oh my God!
```

**NOTE:**  
Como foi dito na definição os comandos **p (de print)** e **pp (de pretty)** printam algo no terminal (console) do **PDB**.

Agora vamos ver alguns exemplos do comando **vars()** que retorna todas as variáveis que já estão definidas atualmente e seus valores:

```python
$ python example-03.py
> example-03.py(3)<module>()
-> name = "Rodrigo"
(Pdb) pp vars()
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__cached__': None,
 '__doc__': None,
 '__file__': 'example-03.py',
 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002BC46409640>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None}
(Pdb) continue
> example-03.py(8)<module>()
-> msg = "Hello World!"
(Pdb) pp vars()
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__cached__': None,
 '__doc__': None,
 '__file__': 'example-03.py',
 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002BC46409640>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'age': 32,
 'name': 'Rodrigo'}
(Pdb)
```

**NOTES:**  
 - A primeira observação aqui é que nós vamos sempre utilizar o comando **pp (de pretty)** porque ele printa as variáveis de forma mais organizada (você pode testar apenas o comando **p** para ver).
 - Outra observação é que o comando **vars()** só retorna as variáveis que já estão definidas, vejam que no **debuger** acime nós tivemos que executar o comando **continue** para ele pular para o próximo **breakpoint()** e lá sim as variáveis **name** e **age** já estavam definidas e assim foram exibidas no nosso retorno.

---

<div id="quit-exit"></div>

## 12 - Entendendo os comandos quit e exit

Os comandos **quit** e **exit** tem os mesmos proprósitos que é **sair do Pdb**.

**Exemplo com quit:**  
```python
$ python loop.py
> loop.py(2)<module>()
-> while count <= 10:
(Pdb) quit
Traceback (most recent call last):
  File "loop.py", line 2, in <module>
    while count <= 10:
  File "loop.py", line 2, in <module>
    while count <= 10:
  File "C:\Users\Drigo\anaconda3\lib\bdb.py", line 88, in trace_dispatch
    return self.dispatch_line(frame)
  File "C:\Users\Drigo\anaconda3\lib\bdb.py", line 113, in dispatch_line
    if self.quitting: raise BdbQuit
bdb.BdbQuit
```

**Exemplo com exit:**  
```python
$ python loop.py
> loop.py(2)<module>()
-> while count <= 10:
(Pdb) exit
Traceback (most recent call last):
  File "loop.py", line 2, in <module>
    while count <= 10:
  File "loop.py", line 2, in <module>
    while count <= 10:
  File "C:\Users\Drigo\anaconda3\lib\bdb.py", line 88, in trace_dispatch
    return self.dispatch_line(frame)
  File "C:\Users\Drigo\anaconda3\lib\bdb.py", line 113, in dispatch_line
    if self.quitting: raise BdbQuit
bdb.BdbQuit
```

---

**REFERÊNCIA:**  
[Como debugar código Python? - Live de Python #197](https://www.youtube.com/watch?v=yffiyHEiUvo)  
 - **54m/20s** (Quando usar where > por exempl uma função que chama outra função e onde nós estamos agora?)
 - **1h/7m** (IPDB + PYTHONBREAKPOINT=0)
 - **1h/19m/30m** (Como debugar no Jupyter?)

---

**Rodrigo Leite -** *drigols*
