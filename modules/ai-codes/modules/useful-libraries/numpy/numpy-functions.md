# NumPy Functions

## Contents

 - [01 - array() function](#array-function)
 - [02 - arange() function](#arange-function)
 - [03 - zeros() function](#zeros-function)

<div id="array-function"></div>

## 01 - array() function

Well, how to create an array with a NumPy functions?

See the example below using **array()** function:

[arrayFunction.py](src/arrayFunction.py)
```python
import numpy as np

def create_array(elements):
  arr = np.array(elements)
  return arr

if __name__ =='__main__':
  lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  arr = create_array(lst)
  print(arr)
```

**OUTPUT:**  

```python
[0 1 2 3 4 5 6 7 8]
```

See how beautiful we have:

 - A function that receives elements/data - **(a list for example)**;
 - Create a NumPy array from these elements/data;
 - Returns the created NumPy array.

<div id="arange-function"></div>

## 02 - arange() function

With **arange()** function we can create an array with predefined parameters. The parameters are as follows:

 - **Start -** Or, where will our array start from;
 - **Stop -** Where will our array end;
 - **Step -** For example, how many jumps will our array take *(we can apply logic here too)*:
   - The **"step"** can also be omitted.

Let's create a function that takes these 3 arguments; Creates an array and returns it already created?

[arrange.py](src/arrange.py)
```python
import numpy as np

def create_arrange(start, stop, step=None):
  arr = np.arange(start, stop, step)
  return arr

if __name__ =='__main__':
  arr = create_arrange(1, 20)
  print(arr)
```

**OUTPUT:**  
```python
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
```

**NOTE:**  
See that it does not print the last element; Note that we also don't use the step argument, as it is optional we leave it default in the **step=None** function.

Shall we test it now?

```python
if __name__ =='__main__':
  arr = create_arrange(1, 20, 2)
  print(arr)
```

**OUTPUT:**  
```python
[ 1  3  5  7  9 11 13 15 17 19]
```

<div id="zeros-function"></div>

## 03 - zeros() function

Another well-known function is **np.zeros()**. It creates an array with zeros from a given dimension:

[zeros.py](src/zeros.py)
```python
import numpy as np

def create_zeros(*args):
  arrZeros = np.zeros(args)
  return arrZeros

if __name__=='__main__':
  arr = create_zeros(10)
  print(arr, "\n")

  lst = [5, 2]
  arr = create_zeros(*lst)
  print(arr, "\n")

  lst_two = [5, 5]
  arr = create_zeros(*lst_two)
  print(arr)
```

**OUTPUT:**  
```python
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

[[0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]]

[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
```

**Pretty not?**  
See that we are using the `*argsin` our **create_zeros()** function, so to pass the list we use the asterisk `(*)`.

---

**REFERENCES:**  
[NumPy - Docs](https://numpy.org/doc/)  

---

**Rodrigo Leite -** *Software Engineer*
