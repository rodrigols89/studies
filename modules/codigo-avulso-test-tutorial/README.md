# Python com Unittest

> Minhas notas do tutorial do **[Michell Stuttgart](https://github.com/mstuttgart)**.

## Conteúdo

 - **Python com Unittest:**
   - [01 - Criando arquivos Python com o comando touch do Linux](#touch)
   - [02 - Os arquivos de teste devem terminar com o nome "test"](#test-name)
   - [03 - Criando e configurando o arquivo setup.py](#setup-py)
   - [04 - Criando testes para a classe FiguraGeometrica](#gigurageometrica-test-01)
   - [05 - Criando testes para a classe Quadrado](#quadrado)
   - [06 - Criando testes para a classe Circulo](#circulo)
   - [07 - Revisão sobre Classes e Métodos Abstratos](#oop-abs)
   - [08 - Utilizando "NotImplementedError" em classes/métodos Abstratos](#notimplementederror)

---

<div id="touch"></div>

## 01 - Criando arquivos Python com o comando touch do Linux

Aqui nós vamos aprender como criar arquivos com o comando **touch** do Linux:

**Dentro do diretório */codigo_avulso_test_tutorial*:**  
```
touch figura_geometrica.py circulo.py quadrado.py
```

**Dentro do diretório */test*:**  
```
touch figura_geometrica_test.py circulo_test.py quadrado_test.py
```

---

<div id="test-name"></div>

## 02 - Os arquivos de teste devem terminar com o nome "test"

Uma observação importante é que os arquivos de teste devem ter o nome terminado em test, para que o módulo de **Unittest** encontre os nossos arquivos de teste automaticamente.

Por isso, nós colocamos os nomes dos arquivos originais terminados com `_test.py`:

 - **Arquivos originais:**
   - figura_geometrica.py
   - circulo.py
   - quadrado.py
 - **Arquivos de Teste:**
   - figura_geometrica_test.py
   - circulo_test.py
   - quadrado_test.py

---

<div id="setup-py"></div>

## 03 - Criando e configurando o arquivo setup.py

Agora nós vamos aprender como configurar um arquivo setup.py e para que ele serve. Primeiro vamos criar o arquivo na raiz do nosso projeto utilizando o comando **touch**:

```
touch setup.py
```

Agora nós vamos adicionar o seguinte código ao arquivo:

[setup.py](setup.py)
```python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
  name='codigo-avulso-test-tutorial',
  packages=['codigo_avulso_test_tutorial', 'test'],
  test_suite='test',
)
```

No código acima:

 - **name**
   - Representa o nome do seu projeto.
 - **packages**
   - São os diretórios do seu projeto que possuem código fonte.
 - **test_suite**
   - Indica o diretório onde estão os fontes de teste.
   - É importante declarar esse diretório pois o Unittest irá procurar dentro dele os arquivos de teste que iremos escrever.

---

<div id="gigurageometrica-test-01"></div>

## 04 - Criando testes para a classe FiguraGeometrica

Agora, vamos usar a lógica do **TDD**:

> Primeiro criamos o código de teste de uma classe para em seguida criamos o código da mesma.

Das classes que criamos, o arquivo [figura_geometrica.py](codigo_avulso_test_tutorial/figura_geometrica.py) servirá como uma classe base para as outras classes. Os métodos que nós vamos ter na nessa classe vão ser:

 - **get_area**
   - Que retorna a área do nosso elemento geométrico.
 - **get_perimetro**
   - Que retorna o perímeto do nosso elemento geométrico.

> Vale salientar que os métodos de teste iniciam com a palavra `test_`.

Agora abra o arquivo [figura_geometrica_test.py](test/figura_geometrica_test.py) em seu editor preferido e adicione o código abaixo:

[figura_geometrica_test.py](test/figura_geometrica_test.py)
```python
# -*- coding: utf-8 -*-
from unittest import TestCase
from codigo_avulso_test_tutorial.figura_geometrica import FiguraGeometrica

# O nome da classe deve iniciar com a palavra Test
class TestFiguraGeometrico(TestCase):

  # Serve para incializar variavei que usaremos
  # globalmente nos testes
  def setUp(self):
    TestCase.setUp(self)
    self.fig = FiguraGeometrica()

  # Retorna uma NotImplementedError
  # O nome do metodo deve comecar com test
  def test_get_area(self):
    self.assertRaises(NotImplementedError, self.fig.get_area)

  # Retorna uma NotImplementedError
  # O nome do metodo deve comecar com test
  def test_get_perimetro(self):
    self.assertRaises(NotImplementedError, self.fig.get_perimetro)
```

**NOTE:**  
Os métodos **test_get_area()** e **test_get_perimetro()** representam testes dos métodos da classe principal [figura_geometrica.py](codigo_avulso_test_tutorial/figura_geometrica.py).

Agora vamos criar esses métodos na classe principal [figura_geometrica.py](codigo_avulso_test_tutorial/figura_geometrica.py):

[figura_geometrica.py](codigo_avulso_test_tutorial/figura_geometrica.py)
```python
# -*- coding: utf-8 -*-

class FiguraGeometrica(object):

  # Retorna a area da figura
  def get_area(self):
    raise NotImplementedError

  # Retorna o perimetro da figura
  def get_perimetro(self):
    raise NotImplementedError
```

**NOTE:**  
Vale salientar que se criarmos um objeto dessa classe e chamarmos um dos dois métodos, uma exceção do tipo **NotImplementedError** será lançada, pois ambos os métodos possuem escopo vazio (Ou seja, não foram implementados ainda).

Finalmente podemos executar o teste da nossa classe. Usando o terminal, no diretorio em que o arquivo setup.py está, execute o seguinte comando:

```python
python setup.py test
```

**OUTPUT:**  
```python
running test
running egg_info
writing codigo_avulso_test_tutorial.egg-info/PKG-INFO
writing top-level names to codigo_avulso_test_tutorial.egg-info/top_level.txt
writing dependency_links to codigo_avulso_test_tutorial.egg-info/dependency_links.txt
reading manifest file 'codigo_avulso_test_tutorial.egg-info/SOURCES.txt'
writing manifest file 'codigo_avulso_test_tutorial.egg-info/SOURCES.txt'
running build_ext
test_get_area (test.figura_geometrica_test.TestFiguraGeometrico) ... ok
test_get_perimetro (test.figura_geometrica_test.TestFiguraGeometrico) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

---

<div id="quadrado"></div>

## 05 - Criando testes para a classe Quadrado

Vamos criar agora outras classes que realmente fazem algo de útil e seus respectivos testes. Começando pela classe Quadrado, vamos escrever um teste para a mesma no arquivo [quadrado_test.py](test/quadrado_test.py):

[quadrado_test.py](test/quadrado_test.py)
```python
# -*- coding: utf-8 -*-

from unittest import TestCase
from codigo_avulso_test_tutorial.quadrado import Quadrado

class TestQuadrado(TestCase):

  def setUp(self):
    TestCase.setUp(self)
    self.fig = Quadrado()

  def test_get_area(self):
    # Verificamos se o resultado é o esperado
    # de acordo com a formula de area do quadrado
    self.fig.lado = 2
    self.assertEqual(self.fig.get_area(), 4)
    self.fig.lado = 7.0
    self.assertEqual(self.fig.get_area(), 49.0)

  def test_get_perimetro(self):
    self.fig.lado = 2
    self.assertEqual(self.fig.get_perimetro(), 8)
    self.fig.lado = 7.0
    self.assertEqual(self.fig.get_perimetro(), 28.0)
```

Em seguida, adicionamos o código da classe ***Quadrado*** no arquivo [quadrado.py](codigo_avulso_test_tutorial/quadrado.py):

[quadrado.py](codigo_avulso_test_tutorial/quadrado.py)
```python
# -*- coding: utf-8 -*-

from .figura_geometrica import FiguraGeometrica

class Quadrado(FiguraGeometrica):

    def __init__(self):
      self.lado = 0

    # Retorna a area do quadrado
    def get_area(self):
      return self.lado**2

    # Retorna o perimetro do quadrado
    def get_perimetro(self):
      return 4 * self.lado
```

**NOTE:**  
Assim como fizemos no exemplo anterior, agora vamos executar os testes:

```
python setup.py test
```

**OUTPUT:**  
```python
running test
running egg_info
writing codigo_avulso_test_tutorial.egg-info/PKG-INFO
writing top-level names to codigo_avulso_test_tutorial.egg-info/top_level.txt
writing dependency_links to codigo_avulso_test_tutorial.egg-info/dependency_links.txt
reading manifest file 'codigo_avulso_test_tutorial.egg-info/SOURCES.txt'
writing manifest file 'codigo_avulso_test_tutorial.egg-info/SOURCES.txt'
running build_ext
test_get_area (test.quadrado_test.TestQuadrado) ... ok
test_get_perimetro (test.quadrado_test.TestQuadrado) ... ok
test_get_area (test.figura_geometrica_test.TestFiguraGeometrico) ... ok
test_get_perimetro (test.figura_geometrica_test.TestFiguraGeometrico) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

Uma detalhe interessante a ser observado é que agora os testes da classe Quadrado estão sendo executados junto com os testes da classe **FiguraGeometrica** sem que fosse necessário alterar nenhuma configuração do projeto, ou adicionar algum novo diretório no arquivo **setup.py**.

**NOTE:**  
Isso acontece por que usamos a sufixo `_test` no nome dos nossos código fonte de teste e também adicionamos o diretório **test** na tag **test_suite** no arquivo **setup.py**.

Desse modo, quando executamos os testes, o **módulo python Unittest** percorre o diretório **test**, carrega automaticamente todos os arquivos com sufixo `_test` e executa os testes dentro deles.

---

<div id="circulo"></div>

## 06 - Criando testes para a classe Circulo

Para encerrarmos o tutorial, vamos agora implementar os testes da classe ***Circulo***:

[circulo_test.py](test/circulo_test.py)
```python
# -*- coding: utf-8 -*-
import math
from unittest import TestCase
from codigo_avulso_test_tutorial.circulo import Circulo

class TestCirculo(TestCase):

  def setUp(self):
    TestCase.setUp(self)
    self.fig = Circulo()

  def test_get_area(self):
    # Utilizamos a formula diretamente por conveniencia
    # já que math.pi e double e sendo assim, possui
    # muitas casas decimais
    self.fig.raio = 2
    area = math.pi * self.fig.raio**2
    self.assertEqual(self.fig.get_area(), area)

    self.fig.raio = 7.0
    area = math.pi * self.fig.raio**2
    self.assertEqual(self.fig.get_area(), area)

  def test_get_perimetro(self):
    self.fig.raio = 2
    perimetro = 2 * math.pi * self.fig.raio
    self.assertEqual(self.fig.get_perimetro(), perimetro)

    self.fig.raio = 7.0
    perimetro = 2 * math.pi * self.fig.raio
    self.assertEqual(self.fig.get_perimetro(), perimetro)
```

Agora de fato vamos implementar na classe [circulo.py](codigo_avulso_test_tutorial/circulo.py):

[circulo.py](codigo_avulso_test_tutorial/circulo.py)
```python
# -*- coding: utf-8 -*-
import math
from .figura_geometrica import FiguraGeometrica

class Circulo(FiguraGeometrica):

  def __init__(self):
    self.raio = 0

  # Retorna a area do circulo
  def get_area(self):
    return math.pi * self.raio**2

  # Retorna o perimetro do circulo
  def get_perimetro(self):
    return 2 * math.pi * self.raio
```

Finalmente, rodamos os testes agora com a presença da classe circúlo:

```
python setup.py test
```

**OUTPUT:**  
```python
running test
running egg_info
writing codigo_avulso_test_tutorial.egg-info/PKG-INFO
writing top-level names to codigo_avulso_test_tutorial.egg-info/top_level.txt
writing dependency_links to codigo_avulso_test_tutorial.egg-info/dependency_links.txt
reading manifest file 'codigo_avulso_test_tutorial.egg-info/SOURCES.txt'
writing manifest file 'codigo_avulso_test_tutorial.egg-info/SOURCES.txt'
running build_ext
test_get_area (test.quadrado_test.TestQuadrado) ... ok
test_get_perimetro (test.quadrado_test.TestQuadrado) ... ok
test_get_area (test.figura_geometrica_test.TestFiguraGeometrico) ... ok
test_get_perimetro (test.figura_geometrica_test.TestFiguraGeometrico) ... ok
test_get_area (test.circulo_test.TestCirculo) ... ok
test_get_perimetro (test.circulo_test.TestCirculo) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

---

<div id="oop-abs"></div>

## 07 - Revisão sobre Classes e Métodos Abstratos

Só para relembrar alguns conceitos básicos sobre ***Orientação a Objetos***, vale lembrar que a classe **FiguraGeometrica** é uma classe abstrada. Ou seja:

> Os métodos **get_area()** e **get_perimetro()** devem ser implementados nas classes filhas da classe **FiguraGeometrica**.

---

<div id="notimplementederror"></div>

## 08 - Utilizando "NotImplementedError" em classes/métodos Abstratos

Segundo a Documentação oficial do Python a Utilização de [NotImplementedError](https://docs.python.org/pt-br/3/library/exceptions.html#NotImplementedError)

> Em classes base, definidas pelo usuário, os métodos abstratos devem gerar essa exceção quando requerem que classes derivadas substituam o método, ou enquanto a classe está sendo desenvolvida, para indicar que a implementação real ainda precisa ser adicionada.

---

**REFERÊNCIAS:**  
[Python com Unittest, Travis CI, Coveralls e Landscape (Parte 1 de 4)](http://pythonclub.com.br/python-com-unittest-travis-ci-coveralls-e-landscape-parte-1-de-4.html)
