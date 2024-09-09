<<<<<<< HEAD
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
=======
# The Python Debugger

## Contents

 - [Opening scripts in Debugger Mode](#debugger-mode)
 - [list (or l) and arrow (->)](#list-arrow)
 - [step (or s) + print (or p), type(), whatis](#useful-stack)
   - [print (or p)](#print-or-p)
   - [type() and whatis](#type-and-whatis)
 - [step (or s) problem + next (or n) solution](#next-solution)
 - [break (or b), continue (or c), clear (or cl)](#break-continue-clear)
   - [continue (or c)](#continue-or-c)
   - [clear (or cl)](#clear)
 - [**REFERENCES**](#ref)
<!--- 
[WHITESPACE RULES]
"20" Whitespace character.
--->




















<!--- ( Debugger Mode ) --->

---

<div id="debugger-mode"></div>

## Opening scripts in Debugger Mode

To open Python scripts in `Debugger Mode`, we can use the following command in the terminal:

```bash
pdb <script>.py
```

or

```bash
python -m pdb <script>.py
```





















<!--- ( l(ist) ) --->

---

<div id="list-arrow"></div>

## list (or l) and arrow (->)

To understand `list (or l)` and the `arrow (->)` in the context of **"Pdb"**, let's imagine that we have the following codes:

```python
# sum.py

def the_sum(x: int, y: int) -> int:
    z: int = x + y
    w: int = x + y + z
    n: int = x + y + z + w
    return n
```

```python
# debugging.py

hello: str = "Hello, World!"

msg: str = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

x: int = 10
y: int = 20

from sum import the_sum

op = the_sum(x, y)
```

Now, let's run the script in the `Debugger Mode`:

```bash
pdb3 debugging.py
```

**Pdb:**
```bash
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
```

If we enter `list (or l)` again, it will list the next 10 lines:

**Pdb:**
```bash
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
(Pdb) list
 12  	
 13  	from sum import the_sum
 14  	
 15  	op = the_sum(x, y)
[EOF]
```

 - `[EOF] means "End of File"`
   - It is displayed when you use the `list (or l)` command and reach the end of the source file, indicating that there are no more lines to display.
 - `->`
   - The `arrow ->` means the next line of code to be executed.
   - **NOTE:** Remember that this line has not been executed yet (ainda). In other words, the debugger does not know what is in this line *yet (ainda)*.

> **NOTE:**  
> We can also provide a *"range"* of lines to the `list (or l)` command.

For example, to list lines 5 through 15:

**Pdb:**
```bash
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum
 14  	
 15  	op = the_sum(x, y)
```

> **NOTE:**  
> If you want to list from a specific line, you can just use the line number.

For example, let's see the line 10:

**Pdb:**
```bash
(Pdb) list 10
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum
 14  	
 15  	op = the_sum(x, y)
```

> **NOTE:**  
> When we list from a specific line Pdb returns `5 lines up` and `5 lines down` **from the line you specified (10 no seu caso)**.





















<!--- ( step (or s) + print (or p) ) --->

---

<div id="useful-stack"></div>

## step (or s) + print (or p), type(), whatis

To understand `step (or s)` command, let's imagine that we have the following codes:

```python
# sum.py

def the_sum(x: int, y: int) -> int:
    z: int = x + y
    w: int = x + y + z
    n: int = x + y + z + w
    return n
```

```python
# debugging.py

hello: str = "Hello, World!"

msg: str = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

x: int = 10
y: int = 20

from sum import the_sum

op = the_sum(x, y)
```

Now, let's run the script in the `Debugger Mode`:

```bash
pdb3 debugging.py
```

**Pdb:**
```bash
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
```

As we know the `arrow (->)` means the current line (instruction) of code will be executed...

> **But, how can we run this line?**  
> A simple command to run the current line is the `step (or s)` command.

For example:

**Pdb:**
```bash
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20

(Pdb) step

(Pdb) list
  1  	# debugging.py
  2  	
  3  	hello: str = "Hello, World!"
  4  	
  5  ->	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20

(Pdb) s

(Pdb) list
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  ->	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum
 14  	
 15  	op = the_sum(x, y)
```

See that always we run the `step (or s)` command the `arrow (->)` changes the line (instruction).

> **But what is the *"purpose"* or *"advantage"* of changing the line arrow?**  
> This is important because the debugger only knows what is on that line (for example, the value of a variable) when it executes the line (instruction).

<div id="print-or-p"></div>

### Print (or p)

For example, let's use the command `print (or p)` to see the values in the **"hello"** and **"msg"** variables:

**Pdb:**
```bash
(Pdb) list 8
  3  	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  ->	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum

(Pdb) print(hello)
Hello, World!

(Pdb) p msg
'\nLorem ipsum dolor sit amet, consectetur adipiscing elit.\nSed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n'
```

See that:

 - `print(hello)`
   - We use the command `print()` to print the value in the **"hello"** variable.
 - `p msg`
   - We use the command `p` to print the value in the **"msg"** variable.

> **What happens if we try to print the value in the variable "x"?**

**Pdb:**
```bash
(Pdb) list 8
  3  	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  ->	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum

(Pdb) print(x)
*** NameError: name 'x' is not defined
```

> `NameError: name 'x' is not defined`  
> This happens because the `arrow (->)` is on the line of the variable "x". In other words, this line has not yet (ainda) been executed, so the debugger does not recognize the "x" variable.

<div id="type-and-whatis"></div>

### type() and whatis

> Two other useful commands are the `type()` and `whatis` commands, which return the variable type.

For example, let's see the type of some variables:

**Pdb:**
```bash
(Pdb) list 8
  3  	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
 12  	
 13  ->	from sum import the_sum

(Pdb) type(hello)
<class 'str'>

(Pdb) whatis x
<class 'int'>

(Pdb) whatis y
<class 'int'>

(Pdb) whatis msg
<class 'str'>
```





















<!--- ( step (or s) problem and next (or n) solution ) --->

---

<div id="next-solution"></div>

## step (or s) problem and next (or n) solution

To understand the **step (or s)** *"problem"*, let's imagine we have the following codes:

```python
# sum.py

def the_sum(x: int, y: int) -> int:
    z: int = x + y
    w: int = x + y + z
    n: int = x + y + z + w
    return n
```

```python
# debugging.py

hello: str = "Hello, World!"

msg: str = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

x: int = 10
y: int = 20

from sum import the_sum

op = the_sum(x, y)
```

Now, let's run the script in the `Debugger Mode`:

```bash
pdb3 debugging.py
```

**Pdb:**
```bash
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
```

Now, let's run some `step (or s)` commands:

**Pdb:**
```bash
-> hello: str = "Hello, World!"

(Pdb) step
-> msg: str = """

(Pdb) step
-> x: int = 10

(Pdb) step
-> y: int = 20

(Pdb) step
-> from sum import the_sum
(Pdb) list
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
 12  	
 13  ->	from sum import the_sum
 14  	
 15  	op = the_sum(x, y)
[EOF]
```

> **What happens if we try to run the `step (or s)` command again?**

**Pdb:**
```bash
(Pdb) step
--Call--
> <frozen importlib._bootstrap>(1349)_find_and_load()
(Pdb) list
1344 	
1345 	
1346 	_NEEDS_LOADING = object()
1347 	
1348 	
1349 ->	def _find_and_load(name, import_):
1350 	    """Find and load the module."""
1351 	
1352 	    # Optimization: we avoid unneeded module locking if the module
1353 	    # already exists in sys.modules and is fully initialized.
1354 	    module = sys.modules.get(name, _NEEDS_LOADING)
```

> **What?**

 - Well, the `step (or s)` run the *"current line (->)"* and if that line has sub-instructions (functions), it will run them too.
 - **NOTE:** No matter how many nested sub-instructions (functions) there are, the `step (or s)` command will execute them one by one.

> **How to solve that?**  
> Using the `next (or n)` command, we can execute the current line *without stepping into (sem entrar)* its sub-instructions.

For example:

**Pdb:**
```bash
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20

(Pdb) n
-> msg: str = """

(Pdb) n
-> x: int = 10

(Pdb) n
-> y: int = 20

(Pdb) n
-> from sum import the_sum

(Pdb) n
-> op = the_sum(x, y)
(Pdb) list
 10  	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum
 14  	
 15  ->	op = the_sum(x, y)
[EOF]
```

Now...

 - If we execute the `step (or s)` command, it will execute the current line and *step into (entra)* its sub-instructions.
 - If we execute the `next (or n)` command, it will execute the current line and step to the next line (instruction).

**step (or s) example:**
```bash
(Pdb) list
 10  	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum
 14  	
 15  ->	op = the_sum(x, y)
[EOF]

(Pdb) step
--Call--
> sum.py(3)the_sum()
-> def the_sum(x: int, y: int) -> int:

(Pdb) list
  1  	# sum.py
  2  	
  3  ->	def the_sum(x: int, y: int) -> int:
  4  	    z: int = x + y
  5  	    w: int = x + y + z
  6  	    n: int = x + y + z + w
  7  	    return n
[EOF]
```

**next (or n) example:**
```bash
(Pdb) list
 10  	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum
 14  	
 15  ->	op = the_sum(x, y)
[EOF]

(Pdb) next
--Return--
> debugging.py(15)<module>()->None
-> op = the_sum(x, y)
(Pdb) list
 10  	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum
 14  	
 15  ->	op = the_sum(x, y)
[EOF]

(Pdb) next
--Return--
> <string>(1)<module>()->None

(Pdb) list
[EOF]

(Pdb) next
The program finished and will be restarted
> debugging.py(3)<module>()
-> hello: str = "Hello, World!"

(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
```

> **"The program finished and will be restarted"**  
> Note that `next (or n)` executes line by line and then returns to the beginning of the program.





















<!--- ( break (or b) ) --->

---

<div id="break-continue-clear"></div>

## break (or b), continue (or c), clear

> **NOTE:**  
> To understand the need for the `break (or b)` command, let's imagine that we have a file with *10 thousand (10k)* lines.

**Well, we would (teríamos) have a problem...**  
We would (teríamos) have to go line by line using the `step (or s)` or `next (or n)` command until we reach the place we want.

> **Ok, but how solve this problem?**  
> Using the `break (or b)` command, we can sets a **"Breakpoint (ponto de parada)"** on the selected line.

For example, imagine we have the following code:

```python
# debugging.py

hello: str = "Hello, World!"

msg: str = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

x: int = 10
y: int = 20

def the_sum(x: int, y: int) -> int:
    z: int = x + y
    w: int = x + y + z
    n: int = x + y + z + w
    return n

op = the_sum(x, y)

name: str = "John"

age: int = 30

dic: dict = {"name": name, "age": age}

list1 = [1, 2, 3, 4, 5]

list2 = [6, 7, 8, 9, 10]

list3 = list1 + list2

print(list3)
```

Now, let's run the script in the `Debugger Mode`:

```bash
pdb3 debugging.py
```

**Pdb:**
```bash
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
(Pdb) list
 12  	
 13  	def the_sum(x: int, y: int) -> int:
 14  	    z: int = x + y
 15  	    w: int = x + y + z
 16  	    n: int = x + y + z + w
 17  	    return n
 18  	
 19  	op = the_sum(x, y)
 20  	
 21  	name: str = "John"
 22  	
(Pdb) list
 23  	age: int = 30
 24  	
 25  	dic: dict = {"name": name, "age": age}
 26  	
 27  	list1 = [1, 2, 3, 4, 5]
 28  	
 29  	list2 = [6, 7, 8, 9, 10]
 30  	
 31  	list3 = list1 + list2
 32  	
 33  	print(list3)
(Pdb) list
[EOF]
```

**Now, imagine we need to run all lines (instructions) until the the_sum() function:**  
To do that, we can set a **breakpoint (ponto de parada)** on the `the_sum()` function.

**Pdb:**
```bash
(Pdb) break 13
Breakpoint 1 at debugging.py:13

(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20

(Pdb) list
 12  	
 13 B	def the_sum(x: int, y: int) -> int:
 14  	    z: int = x + y
 15  	    w: int = x + y + z
 16  	    n: int = x + y + z + w
 17  	    return n
 18  	
 19  	op = the_sum(x, y)
 20  	
 21  	name: str = "John"
 22 
```

See that:

 - We define a **Breakpoint (ponto de parada)** in the file "debugging.py".
 - On the line 13.

**NOTE:**  
To list all **Breakpoints (pontos de parada)**, we need to use the `break (or b)` command without arguments:

**Pdb:**
```bash
(Pdb) break
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at debugging.py:13
```

> **Ok, but how do we change the arrow (->) to the Breakpoint (ponto de parada)?**  
> Using the `continue (or c)` command.

<div id="continue-or-c"></div>

### Continue (or c)

The `continue (or c)` command executes lines (instructions) until the next **breakpoint (ponto de parada)**.

> **Why *"next Breakpoint (ponto de parada)"*?**

 - By default, the first instruction in the file will be the first **Breakpoint (ponto de parada)**.
 - In other words, where the `arrow (->)` starts.

For example:

**Pdb:**
```bash
-> hello: str = "Hello, World!"
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
```

> **NOTE:**  
> See that in our case the first instruction is the `hello: str = "Hello, World!"`. In other words, the first **Breakpoint (ponto de parada)**.

Now, let's set some **Breakpoints (pontos de parada)** and changes the `arrow (->)` using the `continue (or c)` command:

**Pdb:**
```bash
(Pdb) break 13
Breakpoint 1 at debugging.py:13

(Pdb) break 21
Breakpoint 2 at debugging.py:21

(Pdb) break 33
Breakpoint 3 at debugging.py:33

(Pdb) break
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at debugging.py:13
2   breakpoint   keep yes   at debugging.py:21
3   breakpoint   keep yes   at debugging.py:33
(Pdb) 
```

Now, let's check these **Breakpoints (pontos de parada)** using the `list (or l)` command:

**Pdb:**
```bash
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
(Pdb) list
 12  	
 13 B	def the_sum(x: int, y: int) -> int:
 14  	    z: int = x + y
 15  	    w: int = x + y + z
 16  	    n: int = x + y + z + w
 17  	    return n
 18  	
 19  	op = the_sum(x, y)
 20  	
 21 B	name: str = "John"
 22  	
(Pdb) list
 23  	age: int = 30
 24  	
 25  	dic: dict = {"name": name, "age": age}
 26  	
 27  	list1 = [1, 2, 3, 4, 5]
 28  	
 29  	list2 = [6, 7, 8, 9, 10]
 30  	
 31  	list3 = list1 + list2
 32  	
 33 B	print(list3)
(Pdb) list
[EOF]
```

> **NOTE:**  
> Remember that the arrow (->) starts on the file's first instruction.

Finally, let's change the `arrow (->)` using the `continue (or c)` command:

**Pdb:**
```bash
(Pdb) p hello
*** NameError: name 'hello' is not defined
(Pdb) p msg
*** NameError: name 'msg' is not defined
(Pdb) p x
*** NameError: name 'x' is not defined
(Pdb) p y
*** NameError: name 'y' is not defined

(Pdb) continue
> debugging.py(13)<module>()
-> def the_sum(x: int, y: int) -> int:

(Pdb) p hello
'Hello, World!'
(Pdb) p msg
'\nLorem ipsum dolor sit amet, consectetur adipiscing elit.\nSed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n'
(Pdb) p x
10
(Pdb) p y
20

(Pdb) p op
*** NameError: name 'op' is not defined

(Pdb) continue
> debugging.py(21)<module>()
-> name: str = "John"

(Pdb) p op
120

(Pdb) name
*** NameError: name 'name' is not defined
(Pdb) age
*** NameError: name 'age' is not defined
(Pdb) dic
*** NameError: name 'dic' is not defined
(Pdb) list1
*** NameError: name 'list1' is not defined
(Pdb) list2
*** NameError: name 'list2' is not defined
(Pdb) list3
*** NameError: name 'list3' is not defined

(Pdb) continue
> debugging.py(33)<module>()
-> print(list3)

(Pdb) name
'John'
(Pdb) age
30
(Pdb) dic
{'name': 'John', 'age': 30}
(Pdb) list1
[1, 2, 3, 4, 5]
(Pdb) list2
[6, 7, 8, 9, 10]
(Pdb) list3
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

> **See how interesting the use of Breakpoints (pontos de parada) is.**  
> We execute a range of lines (instructions) at once (de uma vez) just by adding **Breakpoints (pontos de parada)**.

> **Ok, but how remove Breakpoints (pontos de parada)?**  
> Using the `clear (or cl)` command.

<div id="clear"></div>

### clear (or cl)

To remove **Breakpoints (pontos de parada)** we use the `clear (or cl)` command:

**Pdb:**
```bash
(Pdb) break
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at debugging.py:13
	breakpoint already hit 1 time
2   breakpoint   keep yes   at debugging.py:21
	breakpoint already hit 1 time
3   breakpoint   keep yes   at debugging.py:33
	breakpoint already hit 1 time

(Pdb) clear 1
Deleted breakpoint 1 at debugging.py:13

(Pdb) cl 2
Deleted breakpoint 2 at debugging.py:21

(Pdb) cl 3
Deleted breakpoint 3 at debugging.py:33

(Pdb) break
(Pdb) 
```





















---

<div id="ref"></div>

## REFERENCES

 - [Como debugar código Python? - Live de Python #197](https://www.youtube.com/watch?v=yffiyHEiUvo)

---

**Rodrigo** **L**eite da **S**ilva
>>>>>>> python-codes
