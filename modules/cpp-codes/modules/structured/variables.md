# Variables (Global, Local, Static)

## Contents

 - **Variable Global vs. Local:**
   - [Global Variables](#global-var)
     - [Global variables can be modified by all the program](#gvm)
   - [Local Variables](#local-var)

---

<div id="global-var"></div>

## Global Variables

 - A declared variable outside the functions is a *Global Variable*.
 - That variable is visible to all the code.
 - *Global Variables* not initialized receives zero (0) value.

For example, the variables below are global:

**CONSOLE:**  
```cpp
#include <iostream>
using namespace std;

int x;
int y = 1;

int main()
{
    cout << "x value is " << x << endl;
    cout << "y value is " << y << endl;

    return 0;
}
```

**OUTPUT:**  
```cpp
x value is 0
y value is 1
```

**NOTE:**  

 - See that the "x" return was zero. It's because the "x" variable was not initialized.
 - This happens (acontece) because global variables are stored in a specific region of memory just for global variables:
   - This region is completely cleared before your program starts.

---

<div id="gvm"></div>

## Global variables can be modified by all the program 

> A Global variable can be modified by all the program.

For example, see the code below:

```cpp
#include <iostream>
using namespace std;

int num;

int f();
int g();


int main()
{
	num = 1;
	cout << f() + g() + num << endl;
}

int f()
{
	num = num + 3;
	return num;
}

int g()
{
	num = 2;
	return num;
}
```

**OUTPUT:**  
```
8
```

**NOTE:**  
See that the function **f()** and **g()** can modify the Global Variable **num**.

---

<div id="local-var"></div>

## Local Variables

> A **variable declared inside a function** is called **local variable** and is **visible only inside the function**.

 - Parameters of the functions are local variables​;
 - Are not automatically initialized to zero (0):
   - If no initialized receives *memory trash*.
 - Are allocated on input of the function and freed on output of the function...

---

**REFERENCES:**  
[Aula 05 - Criação de Funções | Bibliotecas | Parâmetros e Argumentos de Funções | Curso de C++](https://www.youtube.com/watch?v=bHyKo1b8SY4&list=PLX6Nyaq0ebfgWfHqVHVAEPCDG54RLArJh&index=9)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
