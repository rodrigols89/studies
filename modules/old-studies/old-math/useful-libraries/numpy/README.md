# NumPy

# Contents

 - [01 - Instalando a biblioteca NumPy](#01)
 - [02 - Adicionando o NumPy ao requirements](#02)
 - [03 - Importando e verificando a versão do NumPy](#03)
 - [04 - Criando arrays com NumPy](#04)
 - [05 - Shapes de um Array](#05)
 - [06 - Função np.arange() do NumPy](#06)
 - [07 - Função np.zeros do NumPy](#07)
 - [Considerações Finais](#08)

<div id='01'></div>

## 01 - Instalando a biblioteca NumPy

Para instalar o NumPy (supondo que você esteje usando uma distribuição Linux) você pode fazer o seguinte no terminal:

```python
pip install --upgrade numpy==1.18
```

Veja que nós estamos especificando a versão em que vamos trabalhar, no caso **NumPy V1.18**. Agora suponha que hoje mesmo o NumPy atualizou para uma versão mais recente, como eu atualizo? Muito simples...

```python
pip install numpy --upgrade
```

Agora para ver os detalhes da versão atual você pode fazer o seguinte:

```
pip show numpy
```

E teremos como retorno um relatório sobre a biblioteca NumPy (na versão atual):

```
Name: numpy
Version: 1.18.1
Summary: NumPy is the fundamental package for array computing with Python.
Home-page: https://www.numpy.org
Author: Travis E. Oliphant et al.
Author-email: None
License: BSD
```

<div id='02'></div>

## 02 - Adicionando o NumPy ao requirements

É comum em um projeto nós amarrarmos a versões do NumPy para quem for trabalhar no projeto baixar a versão correta e evitar incompatibilidades. Para isso nós adicionamos as bibliotecas do projeto em um arquivo chamado [requirements.txt](../../../requirements.txt). Para fazer isso a partir do **pip** é muito simples:

```python
pip freeze > requirements.txt
```

**NOTE:**  
Para finalizar vamos dar apenas mais essa dica (supondo que você está em um ambiente virtual/virtualenv) você pode ver a lista de pacotes instalados nesse ambiente com o **pip list**:

```python
pip list

Package    Version
---------- -------
numpy      1.18.1 
pip        20.0.2 
setuptools 45.2.0 
wheel      0.34.2
```

<div id='03'></div>

## 03 - Importando e verificando a versão do NumPy

Bem nós já vimos como verificar a versão atual do NumPy com o pip e etc... Mas como importar o NumPy e verifica sua versão atual dentro de um módulo/script python?

[start_numpy.py](src/start_numpy.py)
```python
import numpy as np

def checkVersion():
  print("Current version: ", np.__version__)

if __name__ =='__main__':
  checkVersion()
```

<div id='04'></div>

## 04 - Criando arrays com NumPy

Bem, agora como criar um array com uma função NumPy?

Veja o exemplo abaixo:

[array_numpy.py](src/array_numpy.py)
```python
import numpy as np

def create_array(elements):
  arr = np.array(elements)
  return arr

if __name__ =='__main__':
  lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  arr = create_array(lst)
  print(arr)
```

Veja que lindo, nós temos:
 - Uma função que recebe elementos/dados **- (uma lista por exemplo)**;
 - Cria uma array NumPy a partir destes elementos/dados;
 - Retorna o array NumPy criado.

Tem como verificar o tipo da lista e array para ver se diferencia? Claro, vamos:

[test_type.py](src/test_type.py)
```python
import numpy as np

def test_type(tp):
  print("Type: ", type(tp))

def create_array(elements):
  arr = np.array(elements)
  return arr

if __name__ =='__main__':
  lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  print(lst)
  test_type(lst)

  arr = create_array(lst)
  print(arr)
  test_type(arr)
```

Agora vamos ver como vai ser a saída:

```python
[0, 1, 2, 3, 4, 5, 6, 7, 8]
Type:  <class 'list'>

[0 1 2 3 4 5 6 7 8]
Type:  <class 'numpy.ndarray'>
```

Veja que agora nós temos uma **'list'** e o tipo **'numpy.ndarrau'**.

<div id='05'></div>

## 05 - Shapes de um Array

Também é possível verificar as dimensões (shape) do nosso array. Para isso nós utilizamos o atributo **shape** do NumPy para fazer isso:

[test_shape.py](src/test_shape.py)
```python
import numpy as np

def checkShape(array):
  print(array.shape)

if __name__ =='__main__':
  lst = [1, 2, 3, 5, 5]
  arr = np.array(lst)
  checkShape(arr)
```

<div id='06'></div>

## 06 - Função np.arange() do NumPy

Com a função **arange()** do NumPy nós podemos criar um array com parâmetros predefinido. Os parâmetros são os seguintes:

 - **Start -** Ou, a partir de onde vai começar nosso array;
 - **Stop  -** Onde vai terminar nosso array;
 - **Step  -** Por exemplo, quantos pulos vai dar o nosso array - (podemos aplicar uma lógica aqui também):
   - O **"step"** também pode ser omitido.

Vamos que criar uma função que recebe esses 3 argumentos, cria um array e retorna ele já criado?

[arrange.py](src/arrange.py)
```python
import numpy as np

def create_arrange(start, stop, step=None):
  arr = np.arange(start, stop, step)
  return arr

if __name__ =='__main__':
  arr = create_arrange(1, 20)
  print(arr)
```

Agora vamos ver qual vai ser a saída da nossa linda função?

```
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
```

**NOTE:**  
Veja que ele não imprime o último elemento. Veja que nós também não utilizamos o argumento *step*, como ele é opcional nós deixamos ele default na função **step=None**. Vamos testar ele agora?

[arrange.py](src/arrange.py)
```python
import numpy as np

def create_arrange(start, stop, step=None):
  arr = np.arange(start, stop, step)
  return arr

if __name__ =='__main__':
  arr = create_arrange(1, 20, 2)
  print(arr)
```

E o resultado agora vai ser o seguinte:

```
[ 1  3  5  7  9 11 13 15 17 19]
```

Lindo não?

<div id='07'></div>

## 07 - Função np.zeros do NumPy

Uma outra função bastante conhecida é a **np.zeros()** do NumPy. Ele cria um array com zeros a partir de uma dimensão dada:

[zeros.py](src/zeros.py)
```python
import numpy as np

def create_zeros(*args):
  arrZeros = np.zeros(args)
  return arrZeros

if __name__=='__main__':
  arr = create_zeros(10)
  print(arr, "\n")

  lst = [5, 2]
  arr = create_zeros(*lst)
  print(arr, "\n")

  lst_two = [5, 5]
  arr = create_zeros(*lst_two)
  print(arr)
```

Vamos ver a saida?

```python
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] 

[[0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]] 

[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
```

Pretty não? Veja que nós estamos utilizando o `*args` em nossa função **create_zeros()**, por isso para passar lista nós utilizamos o asterisco **`( * )`**.

<div id='08'></div>

## Considerações Finais

Esse tutorial vai ser apenas uma introdução simples, focando apenas no básico, se você desejar se aprofundar mais é recomendado procurar a [Documentação NumPy](https://numpy.org/doc/) para aprender outras funções e como trabalhar com elas.

**Rodrigo Leite** *- Software engineer*
