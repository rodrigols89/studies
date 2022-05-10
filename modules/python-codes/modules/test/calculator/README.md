# Criando uma calculadora com pytest & TDD

> Minhtas **notas** e **códigos** do tutorial [TDD in Python with pytest](https://www.thedigitalcatonline.com/blog/2020/09/10/tdd-in-python-with-pytest-part-1/).

## NOTES:

 - [01 - from directory.file import ClassFunction_x, ClassFunction_y, ClassFunction_z](#imports)
 - [02 - Rodando um teste específico](#specific-test)
 - [03 - [Mindset] Crie o teste + Codifique o mínimo possível + refatore (Step-By-Step)](#)

---

<div id="imports"></div>

## 01 - from directory.file import ClassFunction_x, ClassFunction_y, ClassFunction_z

Uma dúvida que eu sempre tinha era como funcionava esse sistema de imports, então, depois desses exemplos deu para abstrair essa lógica:

```python
from directory.file import ClassFunction_x, ClassFunction_y, ClassFunction_z
```

---

<div id="specific-test"></div>

## 02 - Rodando um teste específico

Em alguns casos, vamos precisar rodar um teste específico (por exemplo, para ter uma saída mais limpa do pytest). Para isso, é só especificar o caminho do arquivo e adiciona **::** em conjunto com o nome da função de teste.

Por exemplo:

```python
pytest -ssv tests/test_main/test_main.py::test_add_two_numbers
```

**NOTE:**  
Vejam que nós estamos rodando um teste específico no arquivo **tests/test_main/test_main.py** cujo nome da função é **test_add_two_numbers**.

---

<div id="step-by-step"></div>

## 03 - [Mindset] Crie o teste + Codifique o mínimo possível + refatore (Step-By-Step)

Uma abordagem muito comum na hora de se trabalhar com **TDD** é codificar seguindo a lógica do **Step-By=Step (passo a passo**.

Por exemplo nós criamos um teste para o método **Calculator.add**, porém nem a class foi criada ainda:

[test_main.py](tests/test_main/test_main.py)
```python
from calculator.main import Calculator

def test_add_two_numbers():
  calc_instance = Calculator()
  result = calc_instance.add(4, 5)
  assert result == 9
```

**Console:**  
```python
pytest -ssv
```

**OUTPUT:**  
```python
ImportError: cannot import name 'Calculator' from 'calculator.main'
```

Agora nós vamos criar a classe **Calculator**:

[main.py](calculator/main.py)
```python
class Calculator:
  pass
```

**Console:**  
```python
pytest -ssv
```

**OUTPUT:**  
```python
AttributeError: 'Calculator' object has no attribute 'add'
```

Vejam que agora nós já temos outro tipo de erro. Vamos agora adicionar o método **add()**:

[main.py](calculator/main.py)
```python
class Calculator:

  def add(self):
    pass
```

**Console:**  
```python
pytest -ssv
```

**OUTPUT:**  
```python
TypeError: add() takes 1 positional argument but 3 were given
```

Opa, agora nós já temos outro tipo de erro, vamos refatorar novamente:

[main.py](calculator/main.py)
```python
class Calculator:

  def add(self, a, b):
    pass
```

**Console:**  
```python
pytest -ssv
```

**OUTPUT:**  
```python
    def test_add_two_numbers():
      calc_instance = Calculator()
      result = calc_instance.add(4, 5)
>     assert result == 9
E     assert None == 9

tests\test_main\test_main.py:6: AssertionError

FAILED tests/test_main/test_main.py::test_add_two_numbers - assert None == 9
```

Outro tipo de erro, agora vamos dar um retorno que satisfaça nosso **assert**:

[main.py](calculator/main.py)
```python
class Calculator:

  def add(self, a, b):
    return 9
```

**Console:**  
```python
pytest -ssv
```

**OUTPUT:**  
```python
tests/test_main/test_main.py::test_add_two_numbers PASSED
```

Veja que agora o teste passou, mas nós estamos manipulando para que ele der certo. Agora, vamos refatorar novamente para de fato a soma seja resultados de dois números passados pelo usuário:

[main.py](calculator/main.py)
```python
class Calculator:

  def add(self, a, b):
    return a + b
```

**Console:**  
```python
pytest -ssv
```

**OUTPUT:**  
```python
tests/test_main/test_main.py::test_add_two_numbers PASSED
```

**NOTE:**  
Viram agora como funciona o método **Step-By-Step (passo a passo)**? Agora imagine que um dos requisitos do nosso sistema é que essa função **Calculator.add()** some o valor de **n** números, ou seja, o usuário pode enviar quantos números desejar e ele vai retornar a soma de todos eles... Refatorando, vamos ter:

[test_main.py](tests/test_main/test_main.py)
```python
from calculator.main import Calculator

def test_add_two_numbers():
  // code

def test_add_three_numbers():
  calc_instance = Calculator()
  result = calc_instance.add(5, 5, 10)
  assert result == 20
```

**NOTE:**  
Como nosso método **add()** vai receber **n** números e retorna a soma de todos eles, nós podemos criar vários testes, mas por agora nós vamos criar um teste que vai testar a soma de 3 números.

> Agora vamos refatorar nosso método para satisfazer esse requisitos - <u>Retornar a soma de n números</u>.

A primeira coisa que vamos fazer é rodar o teste para ver o resultado da função **test_add_three_numbers()**:

**Console:**  
```python
pytest -ssv
```

**OUTPUT:**  
```python
tests/test_main/test_main.py::test_add_two_numbers PASSED
tests/test_main/test_main.py::test_add_three_numbers FAILED
```

Vejam que o teste para 2 números passou, porém, para 3 não. Vamos agora refatorar novamente para ele receber **n** números:


[main.py](calculator/main.py)
```python
  def add(self, *args):
    return sum(args)
```

**Console:**  
```python
pytest -ssv
```

**OUTPUT:**  
```python
tests/test_main/test_main.py::test_add_two_numbers PASSED
tests/test_main/test_main.py::test_add_three_numbers PASSED
```

**NOTE:**  
Vejam que agora os 2 testes passaram e independente de quantos números o usuários passar ele vai retornar a soma de todos eles. Nós também podemos criar vários outros testes para verificar se realmente o requisito satisfaz o que foi pedido - <u>Retornar a soma de n números</u>.

---

**Rodrigo Leite -** *drigols*
