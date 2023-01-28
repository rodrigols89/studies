# Storage types in C++ (Automatic, Static, Thread, Dynamic)

## Contents

 - **[Storage types in c++](#storage-types)**
   - [Automatic Storage (Local scopes)](#automatic)
   - [Static Storage (Global scopes)](#static)
 - **Tips & Tricks:**
   - [Static variables in Local scopes (Initialized when the program start and deleted when the program terminated)](#static-var-ls)
   - **Variable Global vs. Local:**
     - [Global Variables](#global-var)
       - [Global variables can be modified by all the program](#gvm)
     - [Local Variables](#local-var)

---

<div id="storage-types"></div>

## Storage types in c++

The most common types of *storage (variables)* in c++ are:

 - **Automatic (Local scopes):**
   - Function (or method) runtime.
   - Are functions (or method) parameters and local variables.
   - These variables are visible only in the scope of functions (or methods).
   - Without linker (sem ligação).
 - **Static (Global scopes):**
   - **During program runtime:**
     - For example, *global variables*.
   - **With linker (com ligação):**
     - **External variables (without "static" keyword):**
       - Are variables visible on other files.
       - You can't declare another variable with the same name in another file because exists this variable that can be visible in the others files.
       - To use an external variable in other file we need use **"extern"** keyword to use the Global Variable in the current file:
         - However, we can't assign a value in this statement (step). E.g, `extern int sizeVar = 1000;`.
         - We can only get the global variable to use in the current file in this statement (step): `extern int sizeVar;`.
     - **Internal variables (using "static" keyword):**
       - Are variables visible only in the current file.
       - You can declare another variable with the same name in another file because this variable is only visible in the current file.
 - **Thread:**
   - During thread runtime.
   - Using *"thread_local*"*.
 - **Dynamic (Global scopes):**
   - Controlled by the programmer.
   - Using *"new" operator* to allocate memory.
   - Using *"delete" oprator* to delete allocate memory.

---

<div id="automatic"></div>

## Automatic Storage (Local scopes)

The **Automatic Storage (Local scopes)** are:

 - Function (or method) runtime.
 - Are functions (or method) parameters and local variables.
 - These variables are visible only in the scope of functions (or methods).
 - Without linker (sem ligação).

For example, see the code below three **local variables (scope variables)**:

[automatic_storage_foo.cpp](src/automatic_storage_foo.cpp)
```cpp
int foo(int x, int y)
{
    int z = 10;
    return x + y + z;
}
```

In the function **foo()** above we have three *local variables (scope variables)*:

 - **Two parameters variables:**
   - `int x, int y`
 - **One local scope variable:**
   - `int z = 10`
 - **The three variables are created during function runtime and deleted when the function (scope) finish.**

> **NOTE:**  
> - These variables are created **automatically** when the function start and deleted when the function finish.
> - Therefore (por isso), **automatic storage**.

---

<div id="static"></div>

## Static Storage (Global scopes)

The **Static Storage (Global scopes)** are variables visible:

 - **During program runtime:**
   - For example, *global variables*.
 - **With linker (com ligação):**
   - **External variables (without "static" keyword):**
     - Are variables visible on other files.
     - You can't declare another variable with the same name in another file because exists this variable that can be visible in the others files.
     - To use an external variable in other file we need use **"extern"** keyword to use the Global Variable in the current file:
       - However, we can't assign a value in this statement (step). E.g, `extern int sizeVar = 1000;`.
       - We can only get the global variable to use in the current file in this statement (step): `extern int sizeVar;`.
   - **Internal variables (using "static" keyword):**
     - Are variables visible only in the current file.
     - You can declare another variable with the same name in another file because this variable is only visible in the current file.


For example, see the **static variables (External and Internal)** below:

[extern_foo.h](src/extern_foo.h)
```cpp
#pragma once

void printSize();
```

[extern_foo.cpp](src/extern_foo.cpp)
```cpp
#include <iostream>

extern int sizeVar;

void printSize()
{
    std::cout << "The size is: " << sizeVar;
}
```

[static_storage_foo.cpp](src/static_storage_foo.cpp)
```cpp
#include <iostream>
#include "extern_foo.h"

int sizeVar = 1000; // External, visible on other files.
static int index;   // Internal, visible only in the current file.

int main()
{
    printSize();

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ extern_foo.cpp static_storage_foo.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
The size is: 1000
```

**NOTE:**  
See that, we use the **"extern"** keyword to use a global variable in other file.

---

<div id="static-var-ls"></div>

## Static variables in Local scopes (Initialized when the program start and deleted when the program terminated)

> **What happen if I declare a static variable in a Local Scope (e.g. Function or method)?**

How we know the static variables are alive during program runtime. That's, even (mesmo) if a function terminates a static variable still exists until the program terminates.

> **That's, we can use the same value of a variable to other function call.**

For example, imagine we need to count how many times a function is called, the code is the following:

[count.h](src/count.h)
```cpp
#pragma once

void countCalls();
```

[count.cpp](src/count.cpp)
```cpp
#include <iostream>

void countCalls()
{
    static int count = 1;
    // This increment is after cout print (count++).
    std::cout << "The number of call from this function is: " << count++ << "\n";
}
```

[main_count.cpp](src/main_count.cpp)
```cpp
#include "count.h"

int main()
{
    countCalls();
    countCalls();
    countCalls();
    countCalls();
    countCalls();

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ count.cpp main_count.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
The number of calls from this function is: 1
The number of calls from this function is: 2
The number of calls from this function is: 3
The number of calls from this function is: 4
The number of calls from this function is: 5
```

**NOTE:**  
See that, even (mesmo) the function (scope) is terminated the *static variable* remains (permanece) alive during program runtime. That's, we can use the variable value many times during program runtime.

> **But, why the `"static int count = 1"` statement is no run all the times of the function is called?**

 - **Remember:**
   - The static variable is initialized when the program start to run.
   - And deleted when the program terminated.

> **NOTE:**  
> That's, the statement `"static int count = 1"` is only run one time when the program start to run.

---

<div id="global-var"></div>

## Global Variables

 - A declared variable outside of the all functions is a *Global Variable*:
   - For example, variables declared outside main() function are Global variables.
 - That variable is visible to all the code (file).
 - *Global Variables* not initialized receives zero (0) value.

For example, the variables below are global:

[main_global.cpp](src/main_global.cpp)
```cpp
#include <iostream>

// Global variables.
int x;
int y = 1;

int main()
{
    std::cout << "x value is " << x << "\n";
    std::cout << "y value is " << y << "\n";

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ main_global.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
x value is 0
y value is 1
```

**NOTE:**  

 - See that the "x" variable return was zero:
   - It's because the "x" variable was not initialized.
 - This happens (acontece) because global variables are stored in a specific region of memory just for global variables:
   - This region is completely cleared before your program starts.

---

<div id="gvm"></div>

## Global variables can be modified by all the program 

> A Global variable can be modified by all the program.

For example, see the code below:

[main_global_modified.cpp](src/main_global_modified.cpp)
```cpp
#include <iostream>

// Global variable.
int num;

// Function prototypes
int f();
int g();

int main()
{
    num = 1;
    std::cout << f() + g() + num << "\n";
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

**COMPILATION AND RUN:**
```cpp
g++ main_global_modified.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
8
```

**NOTE:**  
See that the functions **main()**, **f()** and **g()** can modify the Global Variable **num**.

---

<div id="local-var"></div>

## Local Variables

> A **variable declared inside a function (or method)** is called **local variable** and is **visible only inside the function**.

 - Parameters of the functions (or methods) are local variables​.
 - Are not automatically initialized to zero (0):
   - If no initialized receives *memory trash*.
 - Are allocated on input of the function (or method) and freed on output of the function (or method).

---

**REFERENCES:**  
[Aula 05 - Criação de Funções | Bibliotecas | Parâmetros e Argumentos de Funções | Curso de C++](https://www.youtube.com/watch?v=bHyKo1b8SY4&list=PLX6Nyaq0ebfgWfHqVHVAEPCDG54RLArJh&index=9)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
