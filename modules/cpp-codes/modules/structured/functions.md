# Functions

## Contents

 - [Creating Functions](#creating-functions)
   - [Prototype](#prototypef)
   - [Function definition (body)](#fbody)
   - [Call the function](#call-function)
 - [void functions](#void-functions)
 - [The "main" function (+argc and argv)](#main-function)
 - **Tips & Tricks:**
   - [Coming soon...](#)

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

<div id="main-function"></div>

## The "main" function (+argc and argv)

> The **main function** is a starting point of all programs in C++.

```cpp
#include <iostream>
using namespace std;

void sample();

int main()
{
    cout << "Hello, I'm a main function!" << endl;

    return 0;
}
```

**OUTPUT:**
```
Hello, I'm a main function!
```

> **NOTE:**  
> The **main function** is an **interface** between the *Operating System* and *your program*.

The **main function** also can be written as follows:

```cpp
#include <iostream>
using namespace std;


int main(int argc, char ** argv)
{
    // Code here...

    return 0;
}
```

> **What means the parameters *"arg"c* and *"argv"*?**

 - **argc**
   - Is the commands quantity passed to the program on the command line *(including the program name)*.
 - **argv**
   - It's the commands themselves (São os comandos em si):
     - As if it were a list of words separated by index, starting from index zero *(program name)*.

For example, see the program that shows the program name and your first command passed by the command line:

[main_argc_argv-01.cpp](src/main_argc_argv-01.cpp)
```cpp
#include <iostream>
using namespace std;


int main(int argc, char ** argv)
{
    cout << "Program name: " << argv[0] << endl;

    // argc = 1 is when only run de program without arguments.
    // argv > 1 is when we pass arguments on the command line.
    if (argc > 1)
        cout << "arg: " << argv[1] << endl;

    return 0;
}
```

**INPUT:**  
```cpp
g++ main_argc_argv-01.cpp -std=c++17 -o test-main

./test-main.exe first-command
```

**OUTPUT:**
```
Program name: C:\Workspace\p1\modules\cc-codes\modules\structured\src\test-main.exe
argc: first-command
```

---

**REFERENCES:**  
[Aula 02 - Introdução à Linguagem C++ | função main | biblioteca iostream | cout | Curso de C++](https://www.youtube.com/watch?v=HrikceiLvDI&list=PLX6Nyaq0ebfgWfHqVHVAEPCDG54RLArJh&index=5)  
[Aula 04 - Modularidade e Funções | Protótipo | Definição | Função | Curso de C++](https://www.youtube.com/watch?v=HSX6HT_k8n4&list=PLX6Nyaq0ebfgWfHqVHVAEPCDG54RLArJh&index=6)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
