# Fixture Arrange, Act, Assert, Cleanup with Pytest

## Contents

 - [01 - Intro to Arrange, Act, Assert, Cleanup (AAAC)](#intro)
   - [01.1 - Arrange](#01-1)
   - [01.2 - Act](#01-2)
   - [01.3 - Assert](#01-3)
   - [01.4 - Cleanup](#01-4)
 - [02 - Relationship between Fixture -> Arrange + Cleanup](#fixture-arrange)
 - [03 - Autouse fixtures (fixtures you don’t have to request)](#autouse)
 - [04 - Fixture scopes](#scopes)

---

<div id="intro"></div>

## 01 - Intro to Arrange, Act, Assert, Cleanup (AAAC)

You can think of a test as being broken down into **four steps**:

 1. Arrange
 2. Act
 3. Assert
 4. Cleanup

---

<div id="01-1"></div>

## 01.1 - Arrange

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

---

<div id="01-2"></div>

## 01.2 - Act

> The **Act** part is where we execute the test by calling the functions set up in the previous step.

**Act** on the target *behavior*. **Act** steps should cover the main thing to be tested. This could be:

 - Calling a function or method;
 - Calling a REST API
 - Or interacting with a web page.

**NOTE:**
Keep **actions** focused on the target *behavior*.

---

<div id="01-3"></div>

## 01.3 - Assert

> Finally, the **Assert** part is where we specify the pass criteria for the test, which fails it if not met, i.e. if the actual results of the test don’t match those we expected.

Assert is where we look at that resulting state and check if it looks how we’d expect after the dust has settled. It’s where we gather evidence to say the behavior does or does not align with what we expect. The assert in our test is where we take that measurement/observation and apply our judgement to it. If something should be green, we’d say `assert thing == "green"`.

---

<div id="01-4"></div>

## 01.4 - Cleanup

Cleanup is where the test picks up after itself, so other tests aren’t being accidentally influenced by it.

For example:

 - Clean database or table;
 - Delete diretory or files...

---

<div id="fixture-arrange"></div>

## 02 - Relationship between Fixture -> Arrange + Cleanup

> **“Fixtures”**, in the literal sense, are each of the **arrange** steps and data. They’re everything that test needs to do its thing.

**NOTE:**  
In pytest, **“fixtures”** are functions you define that serve this purpose. But they don’t have to be limited to just the **arrange** steps. For example Fixture also can be used to **Cleanup** step.

---

<div id="autouse"></div>

## 03 - Autouse fixtures (fixtures you don’t have to request)

> Sometimes you may want to have a fixture that you know all your tests will depend on. **“Autouse”** fixtures are a convenient way to make all tests automatically request them.

We can make a fixture an autouse fixture by passing in **autouse=True** to the fixture’s decorator. Here’s a simple example for how they can be used:

```python
# contents of test_append.py
import pytest


@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def order(first_entry):
    return []


@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(order, first_entry):
    assert order == [first_entry]


def test_string_and_int(order, first_entry):
    order.append(2)
    assert order == [first_entry, 2]
```

**NOTE:**  
Now ALL test will request **append_first() fixture** by default, because we define **autouse=True**.

---

<div id="scopes"></div>

## 04 - Fixture scopes

 - **function:** the default scope, the fixture is destroyed at the end of the test.
 - **class:** the fixture is destroyed during teardown of the last test in the class.
 - **module:** the fixture is destroyed during teardown of the last test in the module.
 - **package:** the fixture is destroyed during teardown of the last test in the package.
 - **session:** the fixture is destroyed at the end of the test session.

**NOTE:**  
Pytest only caches one instance of a fixture at a time, which means that when using a parametrized fixture, pytest may invoke a fixture more than once in the given scope.

---

**REFERENCES:**  
[pytest fixtures: explicit, modular, scalable](https://docs.pytest.org/en/6.2.x/fixture.html)

---

**Rodrigo Leite -** *drigols*
