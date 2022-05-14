# PyTest - Tips & Tricks

## Conteúdo

 - [Executando testes únicos/específicos](#specific-test)
 - [Pulando/Ignorando (Skipping) testes + Adicionando razão](#skipping-test)
 - [Marcando/Rotulando testes (Tagging)](#tagging)
 - [Rodando testes em ordem de preferência](#order)

---

<div id="specific-test"></div>

## Executando testes únicos/específicos

Em alguns casos, vamos precisar rodar um teste específico (por exemplo, para ter uma saída mais limpa do pytest). Para isso, é só especificar o caminho do arquivo e adiciona **::** em conjunto com o nome da função de teste.

Por exemplo:

```python
pytest -ssv tests/test_main/test_main.py::test_add_two_numbers
```

**NOTE:**  
Vejam que nós estamos rodando um teste específico no arquivo **tests/test_main/test_main.py** cujo nome da função é **test_add_two_numbers**.

---

<div id="skipping-test"></div>

## Pulando/Ignorando (Skipping) testes + Adicionando razão

Às vezes é útil pular testes, por exemplo:

 - Imagine que nós adicionamos um novo código que fez com que muitos (alguns) testes parassem de passar (PASSED).
 - Ou que um recurso específico teve que ser desativado temporariamente:
   - O que também faria com que alguns testes não passassem.

**NOTE:**  
Em todos esses casos, o *decorador* **pytest.mark.skip** é seu amigo. Imagine que nós temos um teste chamado **test_add()** e queremos que ele seja pulado, veja como fica no exemplo abaixo:


```python
@pytest.mark.skip
def test_add():
  [...]
```

O resultado na linha de comando será *(após a execução pytest -svv)*:

```python
tests/test_calc.py::test_addition SKIPPED
```

> Vejam que o nosso teste foi pulado (SKIPPED).

**NOTE:**  
A solução anterior é boa para um salto temporário, mas se o teste tiver que permanecer desativado por muito tempo, é melhor anotar um motivo específico para a exclusão. Na minha experiência, 1 dia é suficiente para esquecer pequenos detalhes como esse, então meu conselho é sempre colocar um motivo bem escrito nos testes ignorados.

Para adicionar um motivo/razão para o teste ser pulado/ignorado nós podemos utilizar o atributo **reason** em conjunto com o decorador **skip**.

Vejam o exemplo abaixo:

```python
@pytest.mark.skip(reason="Addition has been deactivated because of issue #123")
def test_add():
  [...]
```

**NOTE:**  
Porém, temos uma observação aqui, que é na hora de chamar o **pytest** na linha de comando nós devemos passar o argumento **-rs** para listar as razões (reasons) pelo as quais os testes foram pulados/igonorados.

Novamente, vejam o exemplo abaixo:

```python
pytest -svv -rs
```

**OUTPUT:**  
```python
tests/test_calc.py::test_addition SKIPPED
[...]
============================= short test summary info =============================
SKIP [1] tests/test_calc.py:5: Addition has been deactivated because of issue #123

====================== 12 passed, 1 skipped in 0.02 seconds =======================
```

---

<div id="tagging"></div>

## Marcando/Rotulando testes (Tagging)

> Nossos testes testes podem ser <u>marcados</u> ou <u>rotulados</u> usando **pytest.mark**.

**Mas qual a vantagem de marca/rotular testes?**  
O motivo é que nós podemos utilizar essas marcações para executar ou pular um <u>conjuntos de testes</u>.

Digamos que identificamos um conjunto de testes muito lentos que não queremos executar continuamente, então, é só marcar eles como **slow** e executar eles separadamente:

```python
@pytest.mark.slow
def test_addition():
  [...]


def test_subtraction():
  [...]


@pytest.mark.slow
def test_multiplication():
  [...]
```

Para rodar os testes marcados como **slow** basta adicionar o parâmetro **-m** em conjunto com o marcado **slow**:

```python
pytest -svv -m slow
```

**NOTE:**  
Outra observação é que cada teste pode ter mais de um marcador, por exemplo:

```python
@pytest.mark.complex
@pytest.mark.slow
def test_addition():
  [...]
```

**NOTE:**  
Nesse caso, o teste será executado por **pytest -svv -m slowe** e por **pytest -svv -m complex**.

A opção **-m** suporta expressões complexas como:

```python
$ pytest -svv -m 'not slow'
```

> O exemplo acima, executa todos os testes que **não** estão marcados com **slow**.

Veja esse outro exemplo:

```python
$ pytest -svv -m 'mac or linux'
```

 - O exemplo acima, executa todos os testes marcados com **mac** e todos os testes marcados com **linux**.
 - Outra observação é o operador **or**, ou seja, nós também podemos utilizar o operador **and**.

---

<div id="order"></div>

## Rodando testes em ordem de preferência

Em alguns casos nós vamos preferir que determinados testes rodem em uma sequência de nossa preferência. Para isso, o pyteste tem o atributo **order**, onde, nós podemos definir quais as prioridades de cada teste.

Vejam o exemplo abaixo:

**Teste sample:**  
```python
import pytest

@pytest.mark.run(order=3)
def test_three():
  assert True

@pytest.mark.run(order=4)
def test_four():
  assert True

@pytest.mark.run(order=2)
def test_two():
  assert True

@pytest.mark.run(order=1)
def test_one():
  assert True
```

**OUTPUT:**  
```python
test.py::test_one PASSED
test.py::test_two PASSED
test.py::test_three PASSED
test.py::test_four PASSED
```

---

**REFERÊNCIAS:**  
[Useful pytest command line options](https://www.thedigitalcatonline.com/blog/2018/07/05/useful-pytest-command-line-options/)  
[Execute pytest in order](https://stackoverflow.com/questions/34504929/execute-pytest-in-order)

---

**Rodrigo Leite -** *drigols*
