# tuple[type]

## Contents

 - [Intro to Type Hint tuple[type]](#intro)

---

<div id="intro"></div>

## Intro to Type Hint tuple[type]

To start with Type Hint tuple[type], let's see example below:

**typing library approach:**

[tuple.typing.py](src/tuple.typing.py)
```python
from typing import Tuple


def process_items(items_t: Tuple[int, int, str]):
    return items_t


if __name__ == "__main__":

    my_tuple = tuple([10, 10, "Rodrigo"])
    new_tuple = process_items(my_tuple)

    print(new_tuple)
    print(type(new_tuple))
```

**OUTPUT:**  
```python
(10, 10, 'Rodrigo')
<class 'tuple'>
```

**No typing library approach:**

[tuple.py](src/tuple.py)
```python
def process_items(items_t: Tuple[int, int, str]):
    return items_t


if __name__ == "__main__":

    my_tuple = tuple([10, 10, "Rodrigo"])
    new_tuple = process_items(my_tuple)

    print(new_tuple)
    print(type(new_tuple))
```

**OUTPUT:**  
```python
(10, 10, 'Rodrigo')
<class 'tuple'>
```

**NOTE:**  
The variable **items_t** is a tuple with 3 items, <u>an int</u>, <u>another int</u>, <u>and a str</u>.


---

**REFERENCES:**  
[Python Types Intro](https://fastapi.tiangolo.com/python-types/)  

---

**Rodrigo Leite -** *drigols*
