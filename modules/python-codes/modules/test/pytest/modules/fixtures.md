# Pytest - Fixtures

## Contents

 - [01 - Intro to Fixtures](#intro)
 - [02 - Conftest.py](#conftest)

---

<div id="intro"></div>

## 01 - Intro to Fixtures

> Fixtures are functions, which will run before each test function to which it is applied.

**Fixtures** are used to feed some data to the tests such as:

 - Database connections.
 - URLs to test.
 - Some sort of input data.

Therefore, instead of running the same code for every test, we can attach **fixture** function to the tests and it will run and return the data to the test before executing each test.

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
Here, we have a **fixture** function named **input_value()**, which *supplies* the input to the tests.

**NOTE:**  
However, the approach comes with its own limitation. A **fixture** function defined inside a test file has a scope within the test file only. We cannot use that fixture in another test file. To make a fixture available to multiple test files, we have to define the fixture function in a file called **conftest.py**.

---

<div id="conftest"></div>

## 02 - Conftest.py

> We can define the fixture functions in this file to make them accessible across multiple test files.

Create a new file **conftest.py** and add the below code into it:

[conftest.py](../conftest.py)
```python
import pytest

@pytest.fixture
def input_value():
  input = 39
  return input
```

**NOTE:**  
Now you can use this fixture in multiple test files.

---

**REFERENCES:**  
[Pytest - Fixtures](https://www.tutorialspoint.com/pytest/pytest_fixtures.htm)  
[Pytest - Conftest.py](https://www.tutorialspoint.com/pytest/pytest_conftest_py.htm)  

---

**Rodrigo Leite -** *drigols*
