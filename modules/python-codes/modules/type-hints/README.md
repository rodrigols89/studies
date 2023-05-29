# Type Hints

## Contents

 - **Primitive Types:**
    - [varName: int = value](#integers)
    - [varName: float = value](#floating-point)
    - [varName: str = value](#strings)
    - [varName: bool = value (True=1 or False=0)](#bool)
 - **Collections:**
 - **Composite Types::**
 - **Classes and Objects:**
 - **Modules and Packages:**
 - **Custom Types:**
 - [**References**](#references)

<!--- ( Primitive Types ) --->

---

<div id="integers"></div>

## varName: int = value

**Integer function example:**
[sum_integers.py](src/sum_integers.py)
```python
def sum(x: int, y: int) -> int:
    return x + y


if __name__ =="__main__":

    a: int = 10
    b: int = 20

    result: int = sum(a, b)

    print("a + b: ", result)
    print("Type: ", type(result))
```

**OUTPUT:**
```bash
a + b:  30
Type:  <class 'int'>
```

---

<div id="floating-point"></div>

## varName: float = value

[div_float.py](src/div_float.py)
```python
def div(x: float, y: float) -> float:
    try:
        return x / y
    except ZeroDivisionError as e:
        raise ZeroDivisionError(e)

if __name__ =="__main__":

    a: float = 10
    b: float = 2

    result: float = div(a, b)

    print("a / b: ", result)
    print("Type: ", type(result))
```

**OUTPUT:**
```bash
a / b:  5.0
Type:  <class 'float'>
```

---

<div id="strings"></div>

## varName: str = value

[say_name.py](src/say_name.py)
```python
def say_name(first_name: str, last_name: str) -> str:
    return first_name + " " + last_name

if __name__ =="__main__":

    first_name: str = "Rodrigo"
    last_name: str = "Leite"

    name: str = say_name(first_name, last_name)

    print("Name: ", name)
    print("Type: ", type(name))
```

**OUTPUT:**
```bash
Name:  Rodrigo Leite
Type:  <class 'str'>
```

---

<div id="bool"></div>

## varName: bool = value (True=1 or False=0)

[check_signal.py](src/check_signal.py)
```python
# bool: boolean values (True=1 or False=0)

def check_signal(signal: bool) -> bool:
    if signal == 1:
        return True
    elif signal == 0:
        return False

if __name__ =="__main__":

    turn_on: bool = 1
    turn_off: bool = 0

    # True sample.
    result: bool = check_signal(turn_on)
    print("Status: ", result)
    print("Type: ", type(result))

    # False sample.
    result = check_signal(turn_off)
    print("Status: ", result)
    print("Type: ", type(result))
```

**OUTPUT:**
```bash
Status:  True
Type:  <class 'bool'>
Status:  False
Type:  <class 'bool'>
```

<!--- ( References ) --->

---

<div id="references"></div>

## References

 - [Python Types Intro](https://fastapi.tiangolo.com/python-types/)
 - [ChatGPT](https://chat.openai.com/)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
