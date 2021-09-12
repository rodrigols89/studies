# NumPy - Settings

## Contents

 - [01 - Installing NumPy library](#installing-numpy)
 - [02 - Adding NumPy to the requirements](#adding-numpy-to-requirements)
 - [03 - Importing and checking NumPy version](#importing-checking)

<div id='installing-numpy'></div>

## 01 - Installing NumPy library

To install NumPy *(assuming you are using a Linux distribution)* you can do the following in the terminal:

```python
pip  install  - - upgrade  numpy == 1.18
```

See that we are specifying the version we will be working on, in the case **NumPy V1.18**. Now suppose that today NumPy has updated to a newer version, how do I update?

Very simple:

```python
pip  install  numpy  - - upgrade
```

Now to see the details of the current version you can do the following:

```python
pip show numpy
```

And we will return a report on the NumPy library (in the current version):

```python
Name: numpy
Version: 1.18.1
Summary: NumPy is the fundamental package for array computing with Python.
Home-page: https://www.numpy.org
Author: Travis E. Oliphant et al.
Author-email: None
License: BSD
```

<div id="adding-numpy-to-requirements"></div>

## 02 - Adding NumPy to the requirements

It is common in a project for us to tie versions of NumPy to anyone working on the project to download the correct version and avoid incompatibilities. For this we added the project libraries to a file called **requirements.txt**.

To do this from the **pip** is very simple:

```python
pip freeze > requirements.txt
```

**NOTE:**  
To finish we are going to give just one more tip *(assuming you are in a virtual / virtualenv environment)* you can see the list of packages installed in that environment with the **pip list** command:

```python
pip  list
```

**OUTPUT:**  

```python
Package     Version 
- - - - - - - - - -  - - - - - - - 
numpy       1.18 .1  
pip         20.0 . 2  
setuptools  45.2 . 0  
wheel       0.34 . 2
```

<div id="importing-checking"></div>

## 03 - Importing and checking NumPy version

Well we've already seen how to check the current version of NumPy with pip and etc... But how to import NumPy and check its current version inside a python module/script?

[numpyVersion.py](src/numpyVersion.py)
```python
import numpy as np

def checkVersion():
  print("NumPy Library/Current version: ", np.__version__)

if __name__ =='__main__':
  checkVersion()
```

**OUTPUT:**  
```python
NumPy Library/Current version:  1.18.1
```

---

**REFERENCES:**  
[NumPy - Docs](https://numpy.org/doc/)  

---

**Rodrigo Leite -** *Software Engineer*
