# Módulos & Pacotes

## 01 - Maneiras de importar pacotes/módulos em Python

Para importar um módulo utilizamos a palavra-chave **import**:

[math.py](src/math.py)
```python
import math
print(math.sqrt(25))
```

O código acima importará todos os módulos de *math*, para importar apenas o necessário utilizamos a palavra-chave **from**:

[from-example.py](src/from-example.py)
```python
from mathe import sqrt
print(sqrt(25))
```

Observe que ao utilizar ***from package import item***, o item pode ser:
 - Um subpacote;
 - Submódulo;
 - Classe;
 - Função;
 - Variável.

**NOTE:**  
Para diminuir a digitação, costuma-se importar todas as funções de *math* dessa forma:

```python
from math import *
```

## 02 - import item.subitem.subsubitem

> Em uma construção como *import item.subitem.subsubitem* - **cada item, com exceção do último**, **deve ser um pacote**.

O último pode ser também um pacote ou módulo, mas nunca uma classe, função ou variável contida em um módulo.

## 03 - A tabela de símbolos e a função dir()

**Função dir():**  
A função embutida **dir()** é usada para se descobrir quais nomes são definidos por um módulo, ela devolve a tabela de símbolos (uma lista ordenada de strings).

**Tabela de Símbolos:**  
Uma Tabela de Símbolos é um dicionário de dados que cada módulo possui, onde são armazenadas todas as variáveis, funções e classes definidas neste módulo.

Como exemplo, **no terminal**, temos:

```python
$ python3
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
```

## 04 - Introdução a Módulo & Pacotes em Python

 - Um script Python é considerado como Módulo;
 - Um diretório (pasta) é indicado como pacote quando este conta com a presença do arquivo `__init__.py`;
 - Um pacote pode conter vários outros módulos, chamamos de submódulos.

Com esses 3 conceitos (não formais) em mente, vamos criar alguns exemplos. Primeiro crie a seguinte estrutura de diretórios e arquivos:

```
sound/
  __init__.py
  effects/
    __init__.py
    echo.py
    surround.py
    reverse.py
  filters/
    __init__.py
    equalizer.py
    vocoder.py
    karaoke.py
```

Todos os arquivos estão em branco. Apenas o arquivo [sound/effects/echo.py](sound/effects/echo.py) possui o seguinte conteúdo:

[sound/effects/echo.py](sound/effects/echo.py)
```python
# -*- coding: utf-8 -*-

def echofilter():
  print("OK, 'echofilter()' function executed!")
```

Bem agora vamos fazer alguns testes no terminal para entender melhor como trabalhar com esse pacote e módulos. Vá até o terminal **(tenha certeza de está ../sound)**:

```python
python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
```

Para importar a função **echofilter()** do módulo [echo.py](sound/effects/echo.py) podemos fazer de três formas diferentes:

**Abordagem 01:**
```python
>>> import sound.effects.echo
>>> sound.effects.echo.echofilter()
OK, 'echofilter()' function executed!
```

**Abordagem 02:**
```python
>>> from sound.effects import echo
>>> echo.echofilter()
OK, 'echofilter()' function executed!
```

**Abordagem 03:**
```python
>>> from sound.effects.echo import echofilter
>>> echofilter()
OK, 'echofilter()' function executed!
```


**NOTE:**  
Cuidados... Normalmente deduzimos, erroneamente, que podemos importar o módulo diretamente:

```python
>>> exit()
$ python
>>> import sound
```

Na verdade, podemos sim, se olharmos para a tabela de símbolos veremos:

```python
>>> import sound
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'sound']
```

Olha o pacote alí no final, mas se executarmos no terminal algumas das linhas de código abaixo veja o resultado:

```python
>>> sound.effects
>>> sound.effects.echo
>>> sound.effects.echo.echofilter()
```

**ERROR:**
```
AttributeError: module 'sound' has no attribute 'effects'
```

Isso porque não inicializamos o pacote, lembre-se que criamos o arquivo `__init__.py` totalmente vazio.

## 05 - Utilizando a diretiva "all"

Ao invés de importamos os módulos vamos direto utilizar a diretiva **`__all__`** com a lista de *pacotes e/ou módulos* que desejamos disponibilizar. Dessa forma, ao importar o pacote todo **`(from package import *)`** ele saberá quais módulos devem ser importados.

Altere o conteúdo do arquivo [sound/__init__.py](sound/__init__.py) para:

```python
__all__ = ['effects', 'filters']
```

Altere também o conteúdo do arquivo [sound/effects/__init__.py](sound/effects/__init__.py) para:

```python
__all__ = ['echo']
```

Agora vamos reiniciar o terminal e cair para o abraço:

```python
quit()
python
>>> from sound.effects import *
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', >>> echo.echofilter()
OK, 'echofilter()' function executed!
```

## 06 - Entendendo  o `if __name__ == "__main__"`

Bem, vamos começar com alguns conceitos e abstrações antes de aprender como funciona o **`if __name__ == "__main__"`**:

 - Seu script escrito em Python pode ser executado, por exemplo:
   - **Na linha de comando;**
   - **E também pode ser importado como um módulo (para outro módulo).**
 - Um módulo (por exemplo, o seu script) poderá ser importado por outros scripts Python.

Agora nós temos dois casos, duas situações:
 - Uma quando executamos seu script diretamente - **(na linha de comando)**;
 - E outra quando importamos seu script para *"dentro"* de nosso script.

**NOTE:**  
Se você quisesse diferenciar essas duas situações, poderia perguntar:

> **"Quem está executando o código?"** - *Terminal?* *Outro script?*

É isso o que **`if __name__ == "__main__"`** está fazendo, diferenciando os dois casos.

Vamos a um pequeno exemplo. Imagine que você possui um arquivo denominado [foo.py](src/foo.py) e, dentro dele, o seguinte código:

[foo.py](src/foo.py)
```python
#
# Script foo.py
#
print(__name__)
```

Ao executar o **script no terminal**, descobrimos o valor de **`__name__`**:

```python
python foo.py
__main__
```

Bem, nesse caso nós estamos usando o módulo [foo.py](src/foo.py) diretamente. Agora vamos ver como ficar usando ele a partir de outro módulo (importando) ou no terminal (importando também):

**Terminal:**
```python
>>> import foo
foo
```

**Importando por outro módulo/script - [test.py](src/test.py)**  
```python
python test.py
foo
```

Veja que as 2 abordagens retornaram **foo**, que é o nome do módulo que **nós importamos**.

Agora vamos criar uma tomada de decisão com a estrutura **if** no nosso [foo.py](src/foo.py):

[foo.py](src/foo.py)
```python
#
# Script foo.py
#
if __name__ == '__main__':
  print('Executed me directly')
else:
  print('Import Approach')
```

Agora vamos ver os resultados:

**Chamando o módulo/script diretamente**
```
python foo.py
Executed me directly
```

**Importando o módulo/script**
```
>>> python
>>> import foo
Import Approach


python test.py
Import Approach
```

Veja que ele diferencia quando executamos o *arquivo/módulo* principal **[foo.py](src/foo.py)** ou **importamos** ele.

## 07 - Qual a vantagem do `if __name__ =='__main__'`?

Bem agora vai vir a parte mais linda e maravilhosa deste tutorial. **Por que** e **Quanto utilizar** o **`if __name__=='__main__'`**? Vamos na prática né...

Primeiro, vamos criar o seguinte módulo/script:

[sqrt.py](src/sqrt.py)
```python
from math import sqrt

def square(n):
  print(sqrt(n))

square(25)
```

Agora nós temos o seguinte:
 - Um módulo com um código principal - [sqrt.py](src/sqrt.py);
 - Esse módulo importa o **módulo sqrt** do **pacote math**;
 - Cria uma função que printa o quadrado de número **"n"** recebido como argumento;
 - E por fim chama a função **square()** para testar o resultado.

Agora suponha que essa sua função ficou tão maravilhosa que você que usar ela em outros módulos/scripts, vamos importar para ver como fica?

[test_square.py](src/test_square.py)
```python
from sqrt import square
square(100)
```

Agora qual vai ser o resultado do nosso teste?

```python
5.0
10.0
```

**What?** Bem, lembram daquela parte de código onde nós testavamos a função **square()**?

```python
def square(n):
  print(sqrt(n))

square(25)
```

Mesmo sem você chamar essa função o interpretador vai executar o código/bloco principal do módulo/script [sqrt.py](src/sqrt.py).

Ah, Então é muito fácil, vamos remover essa parte de código de testes e usar a apenas a função **square()**. Mas suponha que o nosso módulo/script [sqrt.py](src/sqrt.py) tenha realmente testes e/ou inicializadores que não queremos usar junto com o **código/bloco principal**?

É ai que entra a magia do **`if __name__ =='__main__'`**. Tenha em mente o seguinte:


```python
# -*- coding: utf-8 -*-

""" Código/Bloco do módulo principal
"""

if __name__ == '__main__':
  """ Código/Bloco do módulo secundário
  """
```

O que nós precisamos fazer é o seguinte:
 - Separar códigos que **não queremos disponibilizar** (testes por exemplo) no **Código/Bloco do módulo secundário**;
 - E os códigos que **queremos disponibilizar** (funções por exemplo) no **Código/Bloco do módulo principal**.

Vamos refatorar e testar?

[sqrt.py](src/sqrt.py)
```python
from math import sqrt

def square(n):
  print(sqrt(n))

if __name__ =='__main__':
  square(25)
```

Agora vamos testar no [test_square.py](src/test_square.py):

```python
from sqrt import square
square(100)
```

```python
python test_square.py
10.0
```

Opa, veja que agora o nosso módulo/script de teste retorno apenas o que nós queremos, ou seja, ele ignorou os códigos/bloco secundário.

## Considerações Finais

Bem, vamos recapitular os seguintes conceitos:

 - **1º -** O seu módulo/script pode ser executado diretamente;
 - **2ª -** O seu módulo/script pode ser importado por outro módulo/script;
 - **3º -** O **`if __name__ =='__main__'`** pode ser usado para diferenciar quando um script está sendo executado:
   - Diretamente **- (exemplo, python foo.py)**;
   - Ou importado por outro módulo/script **- (exemplo, import foo)**.
 - **4º -** Nosso módulo/script tem os códigos/bloco:
   - Principal;
   - e/ou secundário.
 - **5º -** Nós podemos separar a executação deles com o **`if __name__ =='__main__'`** para:
   - Os códigos/bloco principal ficar disponível para quem importar;
   - E os códigos/bloco secundário ficar disponível apenas para execução do módulo em que questão - (Por exemplo, para testes)

---

**REFERENCES:**  
[Importando módulos no Python (imports)](http://www.devfuria.com.br/python/imports/)  
[Módulos e Pacotes em Python](http://www.devfuria.com.br/python/modulos-pacotes/)  
[Entenda o __name__ == "__main__"](http://www.devfuria.com.br/python/entenda-__name__-__main__/)  

---

**Rodrigo Leite** - *Software Engineer*
