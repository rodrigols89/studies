# Calculating the Direction (amplitude) of a Vector

## Contents

 - [01 - Introduction](#intro)

<div id="intro"></div>

## 01 - Introduction

To calculate the **direction (amplitude) Vector** you must use a little trigonometry.

> We can obtain the vector angle by calculating a **inverse tangent**, or tan<sup>-1</sup> (O -1 is not an exponent, it just indicates an inverse function sign) , expressed in degrees).

**NOTE:**  
In any **Right Triangle**, the tangent is calculated as the *opposite from adjacent*. In a two-dimensional Vector, this is the value of **y** over the value of **x**, therefore, for our Vector **v = (2, 1)**:

![img](images/vec07.png)  

This produces the result **0.5**, from which we can use a calculator to calculate the *inverse tangent* to obtain the angle in degrees:

![img](images/vec08.png)  

Note that the steering angle is indicated as θ .

See the following Python code to confirm this:

[inverse_tan.py](src/inverse_tan.py)  
```python
import numpy as np
import math

v = np.array([2, 1])
vTan = v[1] / v[0] # Calculates the tangent.
print ('tan = ' + str(vTan)) # Prints the tangent.

vAtan = math.atan(vTan) 
print('inverse-tan = ' + str(math.degrees(vAtan)))
```

**OUTPUT:**  
```python
tan = 0.5
inverse-tan = 26.56505117707799
```

---

**REFERENCE:**  
[Operações básicas com vetores (Álgebra linear/ Cálculo vetorial)](https://www.youtube.com/watch?v=HwgOnEU9NYo&t=2s)  

---

**Rodrigo Leite -** **Software Engineer**
