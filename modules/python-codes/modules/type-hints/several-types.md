# Several Types

## Contents

 - [Intro to Type Hint Several Types](#intro)
 - [Optional = None](#optional)

---

<div id="intro"></div>

## Intro to Type Hint Several Types

> You can declare that a variable can be any of several types, for example, an **int** or a **str**.

 - In Python 3.6 and above (including Python 3.10) you can use the **Union** type from **typing** and put inside the square brackets the possible types to accept.
 - In Python 3.10 there's also an alternative syntax were you can put the possible types separated by a vertical bar **(|)**.

**typing library approach:**

[union_typing.py](src/union_typing.py)
```python
from typing import Union


def process_item(item: Union[int, str]):
    print(item)


if __name__ == "__main__":
    age: int = 10
    name: str = "Rodrigo"

    process_item([age, name])
```

**OUTPUT:**  
```python
[10, 'Rodrigo']
```

**Python 3.10 and above:**

[python3-10_and_above.py](src/python3-10_and_above.py)
```python
def process_item(item: int | str):
    print(item)


if __name__ == "__main__":
    age: int = 10
    name: str = "Rodrigo"

    process_item([age, name])
```

**OUTPUT:**  
```python
[10, 'Rodrigo']
```

**NOTE:**  
In both cases this means that item could be an **int** or a **str**.

---

<div id="optional"></div>

## Optional = None

> You can declare that a value could have a type, like **str**, but that it could also be None.

In Python 3.6 and above (including Python 3.10) you can declare it by importing and using **Optional** from the **typing** module:

**typing library approach:**

```python
from typing import Optional


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
```

This also means that in Python 3.10, you can use **Something | None**:

**Python 3.10 and aboveapproach:**

```python
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
```














































---

**REFERENCES:**  
[Python Types Intro](https://fastapi.tiangolo.com/python-types/)  

---

**Rodrigo Leite -** *drigols*
