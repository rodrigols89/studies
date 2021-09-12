# Calculating Magnitude of a Vector

## Contents

 - [01 - Review](#review)
 - [02 - Applying the Pythagorean Theorem](#pythagorean-theorem)

<div id="review"></div>

## 01 - Review

Before starting to study how to calculate **Magnitude of a vector**, let's pay attention to some details and review some concepts. First let's see our plot created in our introduction:

![image](images/first_vector.png)  

**NOTE:**  
If you pay attention, our vector can be compared to one **Right Triangle**. It will look something like this:

![image](images/teorema-pitagoras.png)  

Oops, so can we calculate the size of our vector using the same formula we used to calculate the hypotenuse of one **Right Triangle**? **Yes, boy**!

> The sum of the side squares; is equal to the square of the hypotenuse.


<div id="pythagorean-theorem"></div>

---

## 02 - Applying the Pythagorean Theorem

Getting back to what matters ...

> Calculating that **Magnitude of the vector** from its Cartesian coordinates requires measuring the distance between the arbitrary starting point and the head point of the vector.

For a two-dimensional vector, **we are actually just calculating the length of the hypotenuse in a right triangle** - so that we could simply invoke the **Pythagorean Theorem** and calculate the square root of the sum of the squares of its components, like this:

![image](images/vec02.png)  

> The notation for the magnitude of a vector is to surround the vector name with vertical bars - you can use single bars (for example, | v |) or double bars (|| v ||). Double bars are often used to avoid confusion with absolute values. Note that the components of the vector are indicated by subscript indices (v<sub>1</sub>, v<sub>2</sub>, ... v<sub>n</sub>).

In this case, the vector **v** has two components with values **2** and **1**, so our magnitude calculation is:

![image](images/vec03.png)  

Which is:

![image](images/vec04.png)  

Like this:

![image](images/vec05.png)  

Let's see how to solve this in Python:

[magnitude.py](src/magnitude.py)
```python
import numpy as np
import math

v = np.array([2, 1])
vMag = math.sqrt(v[0]**2 + v[1]**2) # Take the Vector Magnitude.

print("Magnitude of a Vector {0} is {1}".format(v, vMag))
```

**OUTPUT:**  
```python
Magnitude of a Vector [2 1] is 2.23606797749979
```

**NOTE:**  

> This calculation works for vectors of **any dimensionality** - you just take the square root of the sum of the square components:

![image](images/vec06.png)  

In Python, we can use **linalg.norm()** NumPy function to calculate the **magnitude of a vector**. This is interesting because it prevents us from, for example, creating a semantic error when creating the code:

[magnitude_linalg_norm.py](src/magnitude_linalg_norm.py)  
```python
import numpy as np

v = np.array([2, 1])
vMag = np.linalg.norm(v) # Take the Vector Magnitude. 

print("Magnitude of my Vector {0} is {1}".format(v, vMag))
```

**OUTPUT:**  
```python
Magnitude of my Vector [2 1] is 2.23606797749979
```

See that now we don't even need to import the Math library . Only with NumPy we've solved everything.

---

**REFERENCE:**  
[Operações básicas com vetores (Álgebra linear/ Cálculo vetorial)](https://www.youtube.com/watch?v=HwgOnEU9NYo&t=2s)  

---

**Rodrigo Leite -** **Software Engineer**
