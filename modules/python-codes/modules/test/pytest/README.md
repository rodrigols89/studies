# Pytest

![img](images/logo.png)

## Contents

 - [Running a specific test in a test file (file_source::specifictest)](#running-specific-test)
 - [Tagging (e.g. "mark.slow")](#tagging)
 - [Running tests in preference order (order=1, order=2)](#order-tests)
 - [Skipping tests + Adding reason ("-rs" to list)](#skipping-test)
 - **Arrange, Act, Assert, Cleanup (AAAC):**
   - [Arrange](#arrange)
   - [Act](#act)
   - [Assert](#assert)
   - [Cleanup](#cleanup)
   - [Relationship between Fixture -> Arrange + Cleanup](#fixture-arrange)
 - **Fixtures:**
   - [Intro to Fixtures](#intro-to-fixtures)
   - [`conftest.py`](#conftest)
   - [Fixture rules](#fixture-rules)
 - **Tips & Tricks:**
   - [Creating reverse tests (Creating a test for a feature, not a feature to a test)](#reverse-tests)
 - **[Settings](#settings)**
 - **[References](#references)**

---

<div id="running-specific-test"></div>

## Running a specific test in a test file (file_source::specifictest)

Sometimes, we need to run a specific test in a test file. For example, to get a clean output on the console for a specific test. To do so, we need to:

```bash
pytest -ssv source/test_file.py::specific_test
```

For exanoke, imagine we have the following test file and tests:

**test_calc.py**  
```python
def test_sum(x, y):
    ...


def test_sub(x, y):
    ...


def test_div(x, y):
    ...


def test_mult(x, y):
    ...
```

> **NOTE:**  
> See that we use **"::"** to get a specific test in the file.

To test a specific test above **(for example, "test_sum")** we run:

```bash
pytest -ssv source/test_calc::test_sum
```

---

<div id="tagging"></div>

## Tagging (e.g. "mark.slow")

> Our tests can be labeled (rotulados) using **"pytest.mark"**.


**But what is the advantage of brand/label (marcar/rotular) tests?**  
The reason is that we can use this brand/label (marcar/rotular) to run or skip a *set of tests*.

For example, let's say we identify a set of *very slow* tests that we don't want to run continuously, so we just **mark** them as **slow** and run them separately:

**test_calc.py**  
```python
@pytest.mark.slow
def test_sum(x, y):
    ...


def test_sub(x, y):
    ...


def test_div(x, y):
    ...

@pytest.mark.slow
def test_mult(x, y):
    ...
```

To run the tests **mark** as **"slow"**, just add the parameter **"-m"** together with **"slow"**:

```bash
pytest -svv -m slow
```

**NOTE:**  
Another observation is that each test can have many decorators. For example:

```python
@pytest.mark.complex
@pytest.mark.slow
def test_mult(x, y):
    ...
```

**NOTE:**  
In this case, the test is run by **pytest -svv -m slow** and **pytest -svv -m complex**.

The option **"-m"** supported complex expressions, such:

```python
$ pytest -svv -m 'not slow'
```

**NOTE:**  
In the above example, we run all tests **is not marked as "slow"**.

Let's, see another example:

```python
$ pytest -svv -m 'mac or linux'
```

**NOTE:**  
In the above example, we run all tests marked as **"mac"** or **"linux"**.

---

<div id="order-tests"></div>

## Running tests in preference order (order=1, order=2)

In some cases, we may prefer certain tests to run in a specific order. To accomplish this (para isso), pytest provides the **'order'** attribute, which allows us to define the priorities of each test.

See the example below:

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

<div id="skipping-test"></div>

## Skipping tests + Adding reason ("-rs" to list)

Sometimes it is useful to **skip** tests, for example:

 - Imagine that we have added new code that caused many tests to fail.
 - Or that a specific feature had to be temporarily disabled:
   - Which would also cause some tests to fail.

**NOTE:**  
In all of these cases, the **"pytest.mark.skip"** decorator is your friend. Imagine that we have a test called **test_add()** and we want to skip it, see how it looks in the example below:"

```python
@pytest.mark.skip
def test_add():
    ...
```

```bash
pytest -svv
```

**OUTPUT:**  
```python
tests/test_calc.py::test_add SKIPPED
```

> See that our test was **"SKIPPED"**.

**NOTE:**  
sometimes it's interesting to add a **"reason"** because we skip a test. To add a reason we use the attribute **"reason"**, For example:

```python
@pytest.mark.skip(reason="Addition has been deactivated because of issue #123")
def test_add():
    ...
```

**NOTE:**  
However, we have a note here, that when calling *pytest* from the command line we must pass the **"-rs"** argument to list the reasons why the tests were skipped/ignored.

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

<div id="Arrange"></div>

## Arrange

> **Arrange** is where we prepare everything for our test.

**NOTE:**  
This means pretty much everything except for the **“act”**.

It’s lining up the dominoes so that the **act** can do its thing in one, state-changing step. This can mean:

 - Preparing objects;
 - Starting/killing services;
 - Entering records into a database;
 - Generating some credentials for a user that doesn’t exist yet;
 - Waiting for some process to finish;
 - Or even things like defining a URL to query.

See the **Arrange** examples below:

**Prepare the values of the variables to be tested:**  
```python
def test_scale_must_work_with_lowercase_tonic():
    # Arrange
    tonic = 'c'
    key = 'major'
```

**Prepare a message error to show when the test fails:**
```python
def test_scale_must_return_an_error_saying_that_the_tonic_not_exists():
    # Arrange
    tonic = 'X'
    key = 'major'
    error_message = f'That tonic does not exist, try {NOTES}'
```


**Use the "@mark.parametrize" decorator to make fake data to test:**
```python
from pytest import mark

@mark.parametrize(
    'tonic, key, expected',
    [
        ('C', 'major', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', 'major', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', 'major', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('C', 'minor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('C#', 'minor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('F', 'minor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
    ],
)  # Arrange
def test_scale_must_return_correct_note(tonic, key, expected):
    ...
```

---

<div id="act"></div>

## Act

> The **Act** part is where we execute the test by calling the functions set up in the previous step.

**Act** on the target *behavior*. **Act** steps should cover the main thing to be tested. This could be:

 - Calling a function or method;
 - Calling a REST API
 - Or interacting with a web page.

> **NOTE:**  
> Keep (mantenha) *actions* **focused on the target behavior**.

See the **Act** examples below:

**Example 01:**  
```python
def test_scale_must_work_with_lowercase_tonic():
    # Arrange
    tonic = 'c'
    key = 'major'

    # Act
    result = scale(tonic, key)
```

**Example 02:**  
```python
from pytest import mark, raises


def test_scale_must_return_an_error_saying_that_the_tonic_not_exists():
    # Arrange
    tonic = 'X'
    key = 'major'
    error_message = f'That tonic does not exist, try {NOTES}'

    # Act
    with raises(ValueError) as error:
        scale(tonic, key)
```

**Example 03:**  
```python
@mark.parametrize(
    'tonic, key, expected',
    [
        ('C', 'major', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', 'major', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', 'major', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('C', 'minor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('C#', 'minor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('F', 'minor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
    ],
)  # Arrange
def test_scale_must_return_correct_note(tonic, key, expected):
    # Act
    result = scale(tonic, key)
```

---

<div id="assert"></div>

## Assert

> Finally, the **Assert** part is where we specify the pass criteria for the test, which fails it if not met, i.e. if the actual results of the test don’t `match` those we `expected`.

Assert is where we look at that resulting state and check if it looks how we’d expect after the dust has settled. It’s where we gather evidence to say the behavior does or does not align with what we expect. The assert in our test is where we take that measurement/observation and apply our judgement to it. If something should be green, we’d say `assert thing == "green"`.

See the **Assert** examples below:

**Example 01:**
```python
def test_scale_must_work_with_lowercase_tonic():
    # Arrange
    tonic = 'c'
    key = 'major'

    # Act
    result = scale(tonic, key)

    # Assert
    assert result
```

**Example 02:**
```python
def test_scale_must_return_an_error_saying_that_the_tonic_not_exists():
    # Arrange
    tonic = 'X'
    key = 'major'
    error_message = f'That tonic does not exist, try {NOTES}'

    # Act
    with raises(ValueError) as error:
        scale(tonic, key)

    # Assert
    assert error_message == error.value.args[0]
```

**Example 03:**
```python
@mark.parametrize(
    'tonic, key, expected',
    [
        ('C', 'major', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', 'major', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', 'major', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('C', 'minor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('C#', 'minor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('F', 'minor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
    ],
)  # Arrange
def test_scale_must_return_correct_note(tonic, key, expected):
    # Act
    result = scale(tonic, key)

    # Assert
    assert result['notes'] == expected
```

---

<div id="cleanup"></div>

## Cleanup

Cleanup is where the test picks up after itself, so other tests aren’t being accidentally influenced by it.

For example:

 - Clean database or table;
 - Delete diretory or files...

---

<div id="fixture-arrange"></div>

## Relationship between Fixture -> Arrange + Cleanup

> **“Fixtures”**, in the literal sense, are each of the **arrange** steps and data. They’re everything that test needs to do its thing.

**NOTE:**  
In pytest, **“fixtures”** are functions you define that serve this purpose. But they don’t have to be limited to just the **arrange** steps. For example Fixture also can be used to **Cleanup** step.

---

<div id="intro-to-fixture"></div>

## Intro to Fixtures

> Fixtures are functions, which will run before each test function to which it is applied.

**Fixtures** are used to feed (alimentar) some data to the tests such as:

 - Database connections.
 - URLs to test.
 - Some sort of input data.

**NOTE:**  

 - **[ENG] -** Therefore, instead of running the same code for every test, we can attach **fixture** function to the tests and it will run and return the data to the test before executing each test.
 - **[PT] -** Portanto, em vez de executar o mesmo código para todos os testes, podemos anexar a função fixture aos testes e ela executará e retornará os dados para o teste antes de executar cada teste.

A function is marked as a **fixture** by −

```python
@pytest.fixture
```

See **fixture** example below:

```python
@pytest.fixture
def input_value():
    input = 39
    return input

def test_divisible_by_3(input_value):
    assert input_value % 3 == 0

def test_divisible_by_6(input_value):
    assert input_value % 6 == 0
```

**NOTE:**  
 - Here, we have a **fixture** function named **input_value()**, which *supplies* the input to the tests.
 - See that the test functions **test_divisible_by_3()** and **test_divisible_by_6()** have the fixture **input_value()** function as a parameter.
   - That means, before the functions that have fixture **input_value()** function as a parameter, the function **input_value()** is run.

---

<div id="conftest"></div>

## `conftest.py`

However, the approach comes with its own limitation. A **fixture** function defined inside a test file has a scope within the test file only. We cannot use that fixture in another test file. To make a fixture available to multiple test files, we have to define the fixture function in a file called `conftest.py`.

> We can define the fixture functions in this file to make them accessible across multiple test files.

Create a new file [conftest.py](conftest.py) and add the below code into it:

[conftest.py](conftest.py)
```python
import pytest

@pytest.fixture
def input_value():
    input = 39
    return input
```

Now you can use this **fixture** in multiple test files.

> Ok, but where put the `conftest.py` file?

 - **root/tests:**
   - **[PT] -** Se apenas sua pasta de */tests* precisar do `conftest.py`, coloque-a na pasta de */tests*. 
   - **[EN] -** If only your */tests* folder needs `conftest.py`, then put it in the */tests* folder.

---

<div id="fixture-rules"></div>

## Fixture rules

 - Only **create** a *"Fixture"* **when duplicating the code**.

---

<div id="reverse-tests"></div>

## Creating reverse tests (Creating a test for a feature, not a feature to a test)

A good practice to write tests is a reverse approach:

 - **First, write the "assert" of the test.**
 - **Next, what will generate the "assert".**
 - **Next, create "arrange" (if necessary) to test.**
 - **Finally, write the test "function name".**

That means:

 - **We are creating a test for a feature;**
 - **Not a feature to a test.**

---

<div id="settings"></div>

## Settings

**Create Virtual Environment:**  
```bash
pythonX.YZ -m venv environment
```

**Activate:**  
```bash
source environment/bin/activate
```

**Install Dependencies:**  
```bash
pip install -U -v --require-virtualenv -r requirements.txt
```

---

<div id="references"></div>

## References

 - [Useful pytest command line options](https://www.thedigitalcatonline.com/blog/2018/07/05/useful-pytest-command-line-options/)
 - [Execute pytest in order](https://stackoverflow.com/questions/34504929/execute-pytest-in-order)
 - [pytest fixtures: explicit, modular, scalable](https://docs.pytest.org/en/6.2.x/fixture.html)
 - [Pytest - Fixtures](https://www.tutorialspoint.com/pytest/pytest_fixtures.htm)
 - [Pytest - Conftest.py](https://www.tutorialspoint.com/pytest/pytest_conftest_py.htm)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
