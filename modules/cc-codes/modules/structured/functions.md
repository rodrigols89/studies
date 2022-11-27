# Functions

## Contents

 - [Creating Functions](#creating-functions)
   - [Prototype](#prototypef)
   - [Function definition (body)](#fbody)
   - [Call the function](#call-function)
 - [void functions](#void-functions)

---

<div id="creating-functions"></div>

## Creating Functions

To create a function we need:

 - Provide a prototype for the function.
 - Define a function (provide a body)
 - Call the function

---

<div id="prototypef"></div>

### Prototype

The function prototype defines:

 - What **information type** the function **receives**.
 - What **information type** the function **return**.

For example:

```cpp
void sample(); // Function prototype.
```

---

<div id="fbody"></div>

### Function definition (body)

The definition of a function receives a set of statement (instructions) that do the task for which the function was created.

For example:

```cpp
void sample()
{
    cout << "I'm a function" << endl;
}
```

**NOTE:**  
See that in the function definition we start writing the function prototype.

---

<div id="call-function"></div>

###  Call the function

We can "invoke" function from:

 - Main program (main function).
 - From (inside) another function.

```cpp
#include <iostream>
using namespace std;

void sample();

int main()
{
    cout << "Main function will invoke sample() function:" << endl;
    sample();

    return 0;
}

void sample()
{
    cout << "I'm sample function." << endl;
}

```

**OUTPUT:**  
```cpp
I'm sample function.
```




---

<div id="void-functions"></div>

## void functions

> A function that doesn't return any value has a return type **"void"** in your prototype.

For example:

```cpp
void system(const char*) // system function prototype.
```

**NOTE:**  
An important note is that a function with return type **"void"** doesn't can be attributed to a variable.

---

**REFERENCES:**  
[Aula 04 - Modularidade e Funções | Protótipo | Definição | Função | Curso de C++](https://www.youtube.com/watch?v=HSX6HT_k8n4&list=PLX6Nyaq0ebfgWfHqVHVAEPCDG54RLArJh&index=6)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
