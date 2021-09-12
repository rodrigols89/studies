# Introduction to Vectors

## Contents

 - [01 - Basics](#basics)

<div id="basics"></div>

## 01 - Basics

Okay, man, let's start our studies on vectors with a simple introduction to some very basic concepts. The first thing we should know is that a Vector always has a Magnitude and direction . What does this represent?

 - The **magnitude** represents a distance - **(e.g. "2 miles")**;
 - The **direction** indicates which way the vector is going - **(e.g. "East")**.

This all seems a little complicated, so let's start with a simple, **two-dimensional** example **(two coordinates - X and Y)**.

In this case, we will use:

 - **2** for **x**;
 - And **1** for **y**.

Our vector can be written as **v = (2, 1)**, however, more formally we would use the following notation, in which the dimensional coordinate values ​​for the vector are shown as a matrix:

![image](images/vec01.png)  

So what exactly does that mean? Well, the coordinate is two-dimensional and describes the movements needed to reach the end point (head) of the vector.

 - In this case, we need to move **2** units in **x** *dimension*;
 - And **1** unit in the **y** *dimension*.

**NOTE:**  
Note that we have not specified a starting point for the vector - We are simply describing a destination coordinate that encapsulates the **magnitude** and the **direction** of the vector.

> Think of it as the guidelines you need to follow to get there to from here , without specifying which one really is!

It is quite simple. We just define a **two - dimensional plane (two coordinates - X and Y)**, choose a starting point *(any point in our example, since it was not specified)* and plot the coordinate described by the vector in relation to the starting point.

See the following code to view the vector **V** *(that remember is described by the coordinate (2, 1))*:

[first_vector.py](src/first_vector.py)  
```python
import matplotlib.pyplot as plt
import numpy as np

# Create a Vector with the NumPy array function. 
v = np.array([2,1])

# Utiliza a função quiver() do Matplotlib para criar o plot/gráfico.
# A função quiver() recebe 4 argumentos principais:
# - As coordenadas iniciais do vetor - x = 0 e y = 0, no nosso caso
# - Quantas posições o vetor vai andar - x = 1 e y =1, nosso caso - *v


# Use Matplotlib quiver() function to create the plot/graph. 
# The quiver() function takes 4 main arguments: 
# - The initial coordinates of the vector - x = 0 and y = 0, in our case 
# - How many positions the vector will move: x = 2 and y = 1, our case - *v 
plt.quiver(0, 0, *v, scale=10, color='r')
plt.axis('equal') # Sets the plot size as "equal".

plt.grid()
plt.title('v = (2, 1)')
plt.xlabel('Coordinates - X')
plt.ylabel('Coordinates - Y')
plt.savefig('../images/first_vector.png', format='png')
plt.show()
```

**OUTPUT:**  

![image](images/first_vector.png)  

**NOTES:**  
So, to create our vector **(2, 1)**, we simply create a numpy array with the elements **[2, 1]**; Then, we use the **quiver()** function to visualize the vector; using point **[0, 0]** as a starting point **(or origin)**; Our vector of **(2, 1)** is shown as an arrow that starts at 0, 0 *(initially x = 0 and x = 0)* and moves:

 - **2** units along the **x-axis** (the right);
 - **1** unit along the **y-axis** (upward).

---

**REFERENCE:**  
[Operações básicas com vetores (Álgebra linear/ Cálculo vetorial)](https://www.youtube.com/watch?v=HwgOnEU9NYo&t=2s)  

---

**Rodrigo Leite -** **Software Engineer**
