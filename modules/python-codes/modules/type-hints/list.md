# list[type]

## Contents

 - [Intro to Type Hint list[typer]](#intro)

---

<div id="intro"></div>

## Intro to Type Hint list[typer]

To start, let's define a variable to be a **list** of **str**:

**typing library approach:**  

[list_typing.py](src/list_typing.py)
```python
from typing import List


def process_items(items: List[str]):
    for item in items:
        print(item)


if __name__ == "__main__":
    my_list = ["Rodrigo", "Jhon", "Matheus", "10"]
    process_items(my_list)
```

**OUTPUT:**  
```python
Rodrigo
Jhon
Matheus
10
```

**No typing library approach:**  

[list.py](src/list.py)
```python
def process_items(items: list[str]):
    for item in items:
        print(item)


if __name__ == "__main__":
    my_list = ["Rodrigo", "Jhon", "Matheus", "10"]
    process_items(my_list)
```

**OUTPUT:**  
```python
Rodrigo
Jhon
Matheus
10
```

**NOTE:**  
Those internal types in the square *brackets []* are called "type parameters". In this case, **str** is the type parameter passed to **List** *(or list in Python 3.9 and above)*.

**That means:**  
The variable items is a **list**, and each of the items in this **list** is a **str**.

**NOTE:**  
If you use Python 3.9 or above, you don't have to import **List** from **typing**, you can use the same regular **list** type instead.

---

**REFERENCES:**  
[Python Types Intro](https://fastapi.tiangolo.com/python-types/)  

---

**Rodrigo Leite -** *drigols*
