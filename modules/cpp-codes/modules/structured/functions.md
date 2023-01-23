# Functions

## Contents

 - [Creating Functions](#creating-functions)
   - [Prototype](#prototypef)
   - [Function definition (body)](#fbody)
   - [Call the function](#call-function)
 - [void functions](#void-functions)
 - [The "main" function (+argc and argv)](#main-function)
 - [Default parameters in C++ functions (+"ambiguous" problem in overloading functions)](#default-parameters)

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

<div id="default-parameters"></div>

## Default parameters in C++ functions (+"ambiguous" problem in overloading functions)

> A default parameter is a value provided in a function declaration that is automatically assigned by the compiler if the calling function doesn’t provide a value for the argument.

**NOTE:**  
In case any value is passed, the default value is overridden. 

The following is a simple C++ example to demonstrate the use of default arguments. Here, we don’t have to write 3 sum functions; only one function works by using the default values for 3rd and 4th arguments:

[default_parameters.h](src/default_parameters.h)
```cpp
#pragma once;

int sum(int x, int y, int z = 0, int w = 0);
```

[default_parameters.cpp](src/default_parameters.cpp)
```cpp
int sum(int x, int y, int z = 0, int w = 0) // assigning default values to z,w as 0
{
    return (x + y + z + w);
}
```

[drive_default_parameters.cpp](src/drive_default_parameters.cpp)
```cpp
#include <iostream>
#include "default_parameters.h"

int main()
{
    std::cout << "Function return passing 2 arguments (10, 15): " << sum(10, 15) << "\n";
    std::cout << "Function return passing 3 arguments (10, 15, 25): " << sum(10, 15, 25) << "\n";
    std::cout << "Function return passing 4 arguments (10, 15, 25, 30): " << sum(10, 15, 25, 30) << "\n";

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ default_parameters.cpp drive_default_parameters.cpp -o defaultParameters && ./defaultParameters
```

**OUTPUT:**  
```cpp
Function return passing 2 arguments (10, 15): 25
Function return passing 3 arguments (10, 15, 25): 50
Function return passing 4 arguments (10, 15, 25, 30): 80
```

**NOTE:**  
However, we need to take care if function overloading is done containing the default arguments, then we need to make sure it is not ambiguous to the compiler, otherwise it will throw an error.

The following is the modified version of the above program:

[test_dp_overloading.cpp](src/test_dp_overloading.cpp)
```cpp
#include <iostream>

int sum(int x, int y, int z = 0, int w = 0)
{
    return (x + y + z + w);
}

int sum(int x, int y, float z = 0, float w = 0)
{
    return (x + y + z + w);
}

int main()
{
    std::cout << sum(10, 15) << "\n";
    std::cout << sum(10, 15, 25) << "\n";
    std::cout << sum(10, 15, 25, 30) << "\n";

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ test_dp_overloading.cpp -o test && ./test
```

**OUTPUT:**  
```cpp
test_dp_overloading.cpp: In function 'int main()':
test_dp_overloading.cpp:15:28: error: call of overloaded 'sum(int, int)' is ambiguous
     std::cout << sum(10, 15) << "\n";
                            ^
test_dp_overloading.cpp:3:5: note: candidate: 'int sum(int, int, int, int)'
 int sum(int x, int y, int z = 0, int w = 0)
     ^~~
test_dp_overloading.cpp:8:5: note: candidate: 'int sum(int, int, float, float)'
 int sum(int x, int y, float z = 0, float w = 0)
     ^~~
```

**NOTE:**  
See that we have an "ambiguous" problem. The compiler doesn't know which function uses... How both the functions need the two first arguments this is "ambiguous" to the compiler.

---

**REFERENCES:**  
[Aula 02 - Introdução à Linguagem C++ | função main | biblioteca iostream | cout | Curso de C++](https://www.youtube.com/watch?v=HrikceiLvDI&list=PLX6Nyaq0ebfgWfHqVHVAEPCDG54RLArJh&index=5)  
[Aula 04 - Modularidade e Funções | Protótipo | Definição | Função | Curso de C++](https://www.youtube.com/watch?v=HSX6HT_k8n4&list=PLX6Nyaq0ebfgWfHqVHVAEPCDG54RLArJh&index=6)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
