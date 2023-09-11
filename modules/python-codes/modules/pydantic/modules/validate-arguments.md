# "validate_arguments" decorator

## Contents

 - [Intro to "validate_arguments" decorator](#intro)

---

<div id="intro"></div>

## Intro to "validate_arguments" decorator

To understand "validate_arguments" decorator let's start with the follows the example:

[pydantic-01.py](src/pydantic-01.py)
```python
def sum(x, y):
    return x + y
```

Now, let's test the function with **IPython**:

**ipython -i pydantic-01.py**  
```python
In [5]: sum('', '')
Out[5]: ''

In [6]: sum([], [])
Out[6]: []

In [7]: sum([5], [10])
Out[7]: [5, 10]

In [8]: sum('', '10')
Out[8]: '10'
```

**NOTE:**  
Ok, we have a problem. We should return numbers (int or float), but the function also returns strings, lists.

To solve that, let's try to add **type hinting** and try again:

[pydantic-02.py](src/pydantic-02.py)
```python
def sum(x: float, y: float) -> float:
    return x + y
```

**ipython -i pydantic-02.py**  
```python
In [1]: sum('', '')
Out[1]: ''

In [2]: sum([], [])
Out[2]: []

In [3]: sum([5], [10])
Out[3]: [5, 10]

In [4]: sum('', '10')
Out[4]: '10'
```

> **How a solve this?** Using **"validate_arguments"** Pydantic decorator...

[validate_arguments.py](src/validate_arguments.py)
```python
from pydantic import validate_arguments

@validate_arguments
def sum(x: float, y: float) -> float:
    return x + y
```

**ipython -i validate_arguments.py**  
```python
----> 1 sum('', '')
ValidationError: 2 validation errors for Sum
x
  value is not a valid float (type=type_error.float)
y
  value is not a valid float (type=type_error.float)


----> 1 sum([], [])
ValidationError: 2 validation errors for Sum
x
  value is not a valid float (type=type_error.float)
y
  value is not a valid float (type=type_error.float)


----> 1 sum(10, '')
ValidationError: 1 validation error for Sum
y
  value is not a valid float (type=type_error.float)


In [6]: sum(10, 10)
Out[6]: 20.0

In [8]: sum(10, '1')
Out[8]: 11.0

In [9]: sum('10', '1')
Out[9]: 11.0

In [10]: sum('10', '1.5')
Out[10]: 11.5
```

**NOTE:**  
See that now the return is:

 - A error (ValidationError) when pass invalid values.
 - And when we pass strings representing numbers, they are converted (casting) to float or int.

**NOTE:**  
The validation is at **runtime**.

---

**REFERENCES:**  
[Pydantic - Live de Python #165](https://www.youtube.com/watch?v=UdfLu1G47BU)

---

**Rodrigo Leite -** *drigols*
