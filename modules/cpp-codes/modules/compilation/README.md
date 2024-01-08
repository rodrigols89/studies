# Compilation

## Contents

 - **Compilation Process:**
   - [Pre-processing (-E)](#intro-to-preprocessing)
   - [Compiling (-S)](#intro-to-compiling)
   - [Assembling (-c)](#intro-to-assembling)
   - [Linking (-o)](#intro-to-linking)
 - **Tools:**
   - **GNU Compiler Collection (GCC/G++):**
   - **GNU Make:**
      - [Makefile (targets:prerequisites/command(s), variables, and wildcard functions)](#intro-to-makefile)
   - **CMake:**
     - [Intro to CMake](#intro-to-cmake)
     - **CMakeLists.txt:**
       - [cmake_minimum_required()](#cmake-minimum-required)
       - [project()](#project)
       - [add_executable()](#add-executable)
 - [**References**](#ref)




































































































<!--- ( Compilation Process ) --->

---

<div id="intro-to-preprocessing"></div>

## Pre-processing (-E)

In the **Pre-processing** stage of compiling a C++ program, several tasks are performed. For example:

 - **Header inclusion:**
   - The contents of header files (specified using `#include` directives) are copied into the source code.
 - **Macro expansion:**
   - Macros defined using `#define` are replaced with their corresponding code.
 - **Conditional compilation:**
   - Directives like `#ifdef`, `#ifndef`, `#else`, `#elif`, and `#endif` are processed to *include* or *exclude* code based on certain conditions.
 - **File inclusion:**
   - Files specified with `#include` are processed, including nested includes.
 - **Comments removal:**
   - Comments (both single-line `//` and multi-line `/* */`) are removed from the code.
 - **Whitespace removal:**
   - Extra *whitespaces* and *tabs* are condensed to a single space.
 - **Line continuation:**
   - The backslash `\` at the end of a line is used for line continuation, and it is processed by combining the current line with the next one.
 - **Character set conversion:**
   - Characters are converted to the appropriate character set if needed.
 - **Pragma processing:**
   - Directives like `#pragma` are processed, which provide compiler-specific instructions.
 - **Assertion handling:**
   - `#assert` statements are checked, and if the specified condition is false, an error message is generated.

![img](images/preprocessor-01.png)  

Now, let's see how to apply preprocessor stage manually using **g++**. For example, imagine we have the following codes:

[preprocessing.cpp](src/preprocessing.cpp)
```cpp
#include <iostream>        // Header inclusion
#include "external_code.h" // File inclusion

// Macro definition
#define SQUARE(x) ((x) * (x))

// Conditional compilation
#ifdef DEBUG
#define LOG(message) std::cout << "Debug: " << message << std::endl;
#else
#define LOG(message)
#endif

// Assertion
#define CHECK_CONDITION(condition)                                 \
    if (!(condition))                                              \
    {                                                              \
        std::cerr << "Assertion failed: " #condition << std::endl; \
        exit(EXIT_FAILURE);                                        \
    }

int main()
{
    // Macro expansion
    int result = SQUARE(5);

    // Conditional compilation
    LOG("This is a debug message.");

    // Tokenization
    int i = 10;
    int j = i + 20;

    // Line continuation
    int sum = i +
              j;

    // Character set conversion
    char specialChar = '\x41';

    // Assertion handling
    CHECK_CONDITION(i < 100);

    std::cout << "Result: " << result << std::endl;

    return 0;
}
```

[external_code.h](src/external_code.h)
```cpp
#ifndef EXTERNAL_CODE_H
#define EXTERNAL_CODE_H

#include <iostream>

void externalFunction();

#endif // EXTERNAL_CODE_H
```

[external_code.cpp](src/external_code.cpp)
```cpp
#include "external_code.h"

void externalFunction()
{
    std::cout << "This is a function from external_code.h" << std::endl;
}
```

To preprocess the code above, we can use the **"g++"** with the **"-E"** flag:

```bash
g++ -E main.cpp -o processed.i
```

**NOTE:**  
We can also use the **"-o"** flag to save the preprocessed code in a file.

---

<div id="intro-to-compiling"></div>

## Compiling (-S)

> The second stage of *compilation* is the **"compilation"** too. The code created by **"the preprocessor is translated to assembly instructions specific."** It is an intermediate human readable language.

![img](images/compiler-01.png)  

To translate the preprocessed code to assembly instructions, we can use the **"g++"** with the **"-S"** flag:

```bash
g++ -S processed.i -o assembly.s
```

**NOTE:**  
Here, we can also use the **"-o"** flag to save the assembly code in a file.

---

<div id="intro-to-assembling"></div>

## Assembling (-c)

For this third stage, **the assembly code (that we have make in the previous steps) is translated to object code**.

> **NOTE:**  
> An object code, it’s only composed **"0"** and **"1"**.

![img](images/assembler-01.png)  

To translate the assembly code to object code, we can use the **"g++"** with the **"-c"** flag:

```bash
g++ -c assembly.s -o objectcode.o
```

**NOTE:**  
Here, we can also use the **"-o"** flag to save the assembly code in a file.

---

<div id="intro-to-linking"></div>

## Linking (-o)

> Finally, the linking stage produce an executable program.

To do an executable:

 - The existing pieces have to be rearranged.
 - And the missing ones filled in (as que faltam, preenchidas).

The linker will arrange the piece of object code. For example, he add pieces containing the instructions for library functions.

![img](images/linker-01.png)  

To translate the object code to executable, we can use the **"g++"** with the **"-o"** flag:

For example:

**Translate the assembly code to object code:**
```bash
g++ -c assembly-01.s -o objectcode-01.o
g++ -c assembly-02.s -o objectcode-02.o
```

**Linking all the object codes (in the same folder):**
```bash
g++ *.o -o exe.out

or

g++ objectcode-01.o objectcode-02.o -o exe.out
```

**NOTE:**  
Before the **"-o"** *flag* was used to generate files to specific outputs. Here is used to generate an executable.

As our program has only one file to link we'll generate an executable with only him:

```bash
g++ objectcode.o -o printy.out
```

**Run the executable:**
```bash
./printy.out
```

**OUTPUT:**
```bash
Result: 25
```




















[](src/)
```cpp

```





































































---

<div id="install-dependencies"></div>

## Install project dependencies in a specific project vs. Operational system

There, two common approaches to install dependencies for a project:

 - Install on the project.
 - Install on the Operating System.

For example, imagine we need the install *SDL library* on our project:

 - **Installing SDL in the Specific Project:**
   - In this approach, you include SDL header files and libraries directly in your project.
   - This means that SDL dependencies are controlled by your project and do not affect other projects or systems.
   - This approach is common in smaller projects and when you want to ensure that your code is portable across different systems without relying on global system settings.
   - **Pros:**
     - Avoids conflicts with different versions of the SDL in different projects.
     - Facilitates code portability between different systems.
     - Allows you to use a specific version of SDL for the project.
   - **Cons:**
     - Can increase the project's size as library files and headers are included directly.
     - May require more effort to set up libraries and paths correctly for the project.
 - **Installing SDL on the Operating System:**
   - In this approach, you install SDL globally on the operating system.
   - This means that other projects can also leverage the same SDL installation without the need to replicate library files and headers in each individual project.
   - This approach is often used in larger projects or when you want to take advantage of optimization and updates provided by the operating system.
   - **Pros:**
     - Avoids duplication of library files and headers across different projects.
     - Can leverage optimizations and updates from the operating system.
     - Configuration can be simpler for projects as you don't need to point to specific include and library paths.
   - **Cons:**
     - Can create dependencies between projects and the global SDL of the system.
     - Can cause issues if there are version conflicts of SDL between projects.
     - May not be as portable, as projects need to rely on the global SDL installation.

---
































<div id="static-library"></div>

## Static library

 - The library code is directly copied into the executable during the compilation process.
 - Makes the executable larger as the library code is included in it.
 - Doesn't require external libraries during execution, as all the necessary code is embedded in the executable.
 - Changes in the library require recompilation of the entire program.

For example, let's make a **Static Library** that uses an *external library (SDL)*. But, first, let's consider some things:





[]()



---

<div id="dynamic-library"></div>

## Dynamic library

 - The library code is kept separately in dynamic files (DLLs in Windows or shared objects in Linux).
 - The executable contains references to functions and resources in the library.
 - Makes the executable smaller since it doesn't embed the library code.
 - Requires the presence of external libraries during execution, which can be slightly more complicated.
 - Changes in the library usually don't require recompilation of the program unless the library's interface changes.
























































<!--- ( Compilation/Tools/GNU Make ) --->

---

<div id="intro-to-makefile"></div>

## Makefile (targets:prerequisites/command(s), variables, and wildcard functions)

A makefile consist:

 - **targets:prerequisites**
   - command<sub>1</sub>
   - command<sub>2</sub>
   - ...
   - command<sub>n</sub>
 - **variables.**
 - **wildcard functions.**

Let's get started with **targets:prerequisites/command(s)**:

 - **target:**
   - **target** is the name of the ***action*** you want to execute.
   - Or usually the name of the file you want to produce.
 - **prerequisites:**
   - Are files that are used as input to create the *target*.
 - **command(s)**:
   - Are operations run to generate or help the **"prerequisites"**.

For example, imagine we have the following files (program):

**helloWorld.h**
```cpp
#ifndef _H_TESTE
#define _H_TESTE

void helloWorld();
```

**helloWorld.c**
```cpp
#include <stdio.h>
#include <stdlib.h>

void helloWorld(void){
    printf("Hello World!\n");
}
```

**main.c**
```cpp
#include <stdlib.h>
#include "helloWorld.h"

int main(){
    helloWorld();
    return (0);
}
```

Now, imagine we need to compile these files. We can use a makefile to do it:

**makefile**
```makefile
printy: main.o helloWorld.o
    gcc -o printy main.o helloWorld.o

main.o: main.c helloWorld.h
    gcc -o main.o main.c -c -W -Wall -ansi -pedantic

helloWorld.o: helloWorld.c helloWorld.h
    gcc -o helloWorld.o helloWorld.c -c -W -Wall -ansi -pedantic

clean:
    rm -rf *.o *~ printy
```

See that:

 - **printy** depends on → **main.o** and **helloWorld.o**:
   - And run the command **"gcc -o printy main.o helloWorld.o"** to help.
 - **main.o** depends on → **main.c** and **helloWorld.h**:
   - And run the command **"gcc -o main.o main.c -c -W -Wall -ansi -pedantic"** to help.
 - **helloWorld.o** depends on → **helloWorld.c** and **helloWorld.h**:
   - And run the command **"gcc -o helloWorld.o helloWorld.c -c -W -Wall -ansi -pedantic"** to help.
 - Finally, we have a command (target) **"clean"**:
   - How this command (target) has no prerequisites we just run this command (target) with: **"make clean"**.
   - This command is useful to remove unnecessary files.

**NOTE:**  
If you pay attention you can see that we have repeat many times the command **"gcc"**. To solve that, we can create a variable to represent this value.

 - **Variable syntax:**
   - VAR_NAME=value
 - **To use:**
   - $(VAR_NAME)

For example:

**makefile**
```makefile
# Variables
COMPILER=gcc

printy: main.o helloWorld.o
    $(COMPILER) -o printy main.o helloWorld.o

main.o: main.c helloWorld.h
    $(COMPILER) -o main.o main.c -c -W -Wall -ansi -pedantic

helloWorld.o: helloWorld.c helloWorld.h
    $(COMPILER) -o helloWorld.o helloWorld.c -c -W -Wall -ansi -pedantic

clean:
    rm -rf *.o *~ printy
```

Now, if we change the compiler we need just  modify the value in the **"COMPILER"** variable.

**NOTE:**  
See also we have the argument **"-o"** and **"-c -W -Wall -ansi -pedantic"** used in many cases. That's, we can create variables for them:

**makefile**
```makefile
# Variables
COMPILER=gcc
ARGS=-o

# Flags for compiler
CC_FLAGS=-c         \
         -W         \
         -Wall      \
         -ansi      \
         -pedantic

printy: main.o helloWorld.o
    $(COMPILER) $(ARGS) printy main.o helloWorld.o

main.o: main.c helloWorld.h
    $(COMPILER) $(ARGS) main.o main.c $(CC_FLAGS)

helloWorld.o: helloWorld.c helloWorld.h
    $(COMPILER) $(ARGS) helloWorld.o helloWorld.c $(CC_FLAGS)

clean:
    rm -rf *.o *~ printy
```

**NOTE:**  
We can also call these *targets (printy, main.o, helloWorld.o, clean)* separated, for example:

```bash
make printy
make main.o
make helloWorld.o
make clean
```

> **NOTE:**  
> However, if we call **"make printy"** he will call your prerequisites, that will call your prerequisites, and so on (e assim por diante/sucessivamente).

Knowing that, is common to create a *main target (e.g. "all")* e call just him. For example:


```makefile
# Variables
COMPILER=gcc
ARGS=-o

# Flags for compiler
CC_FLAGS=-c         \
         -W         \
         -Wall      \
         -ansi      \
         -pedantic

all:printy

printy: main.o helloWorld.o
    $(COMPILER) $(ARGS) printy main.o helloWorld.o

main.o: main.c helloWorld.h
    $(COMPILER) $(ARGS) main.o main.c $(CC_FLAGS)

helloWorld.o: helloWorld.c helloWorld.h
    $(COMPILER) $(ARGS) helloWorld.o helloWorld.c $(CC_FLAGS)

clean:
    rm -rf *.o *~ printy
```

```bash
make all
```

**NOTE:**
Another problem is that we have many files **"o."**, **".c"**, and **".h"**. How we can call all at once (de uma vez)?

**Using "wildcard functions":**  
To solve that we can use the **wildcard "*"**, for example see the code below:

**NOTE: Esse exemplo não está completo, pois não usa wildcard "%", mas em breve retornare aqui para arrumar, quando eu aprender como utiliza-lo:**
```makefile
# Variables
PROJ_NAME=printy
COMPILER=gcc
ARGS=-o

# .c files.
C_SOURCE=$(wildcard *.c)

# .h files.
H_SOURCE=$(wildcard *.h)

# Object files.
OBJ=$(C_SOURCE:.c=.o)

all:$(PROJ_NAME)

printy: main.o helloWorld.o
    $(COMPILER) $(ARGS) printy main.o helloWorld.o

main.o: main.c helloWorld.h
    $(COMPILER) $(ARGS) main.o main.c $(CC_FLAGS)

helloWorld.o: helloWorld.c helloWorld.h
    $(COMPILER) $(ARGS) helloWorld.o helloWorld.c $(CC_FLAGS)

clean:
    rm -rf *.o $(PROJ_NAME) *~
```

See that, we are grouping by file:

 - **NOTE:** In this example we create a variable (PROJ_NAME) to store the project name.
 - **All ".c":**
   - `C_SOURCE=$(wildcard *.c)`
 - **All ".h":**
   - `H_SOURCE=$(wildcard *.h)`
 - **All ".o":**
   - `OBJ=$(C_SOURCE:.c=.o)`
   - See that here depend on all `".c"=C_SOURCE`.








































<!--- ( Compilation/Tools/CMake ) --->

---

<div id="intro-to-cmake"></div>

# Intro to CMake

> **CMake is a compiler generator system.**

**What?**  
For example, CMake can be used to generate a makefile for your project automatically.

 - In truth, the CMake tool generates a makefile and many auxiliary files.
 - We need a file called *CMakeLists.txt* to set up our project in the same folder as our program files. For example:
   - MyProject:
     - calc.h
     - calc.cpp
     - main.cpp
     - CMakeLists.txt
 - As many files are generated by CMake is recommended to create a folder to put these files. For example:
   - MyProject:
     - **Debug/** For debug compilation.
     - **Release/** For release compilation.
     - calc.h
     - calc.cpp
     - main.cpp
     - CMakeLists.txt

To generate these files we need go to the **"Debug/"** or **"Release"** folder and run the following commands:

**Debug:**
```bash
cd Debug/

cmake -DCMAKE_BUILD_TYPE=Debug ../
```

**Release:**
```bash
cd Release/

cmake -DCMAKE_BUILD_TYPE=Release ../
```

---

<div id="cmake-minimum-required"></div>

## cmake_minimum_required()

Any project's top most **CMakeLists.txt** must start by specifying a minimum CMake version using the **cmake_minimum_required()** command.

```c
cmake_minimum_required(VERSION <min>[...<policy_max>] [FATAL_ERROR])
```

**NOTE:**  
> - **ENG -** This establishes policy settings and ensures that the following CMake functions are run with a compatible version of CMake.
> - **PT -** Isso estabelece configurações de política e garante que as seguintes funções do CMake sejam executadas com uma versão compatível do CMake.

**Useful Links:**  
[cmake_minimum_required](https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html#command:cmake_minimum_required)

**Real example:**
```c
cmake_minimum_required(VERSION 3.27.0)
```

---

<div id="project"></div>

## project()

> To start a project, we use the **project()** command to set the project name.

 - This call is required with every project and should be called soon after *cmake_minimum_required()*.
 - As we will see later, this command can also be used to specify other project level information such as the language or version number.

```c
project(<PROJECT-NAME> [<language-name>...])
project(<PROJECT-NAME>
        [VERSION <major>[.<minor>[.<patch>[.<tweak>]]]]
        [DESCRIPTION <project-description-string>]
        [HOMEPAGE_URL <url-string>]
        [LANGUAGES <language-name>...])
```

**Useful Links:**  
[project](https://cmake.org/cmake/help/latest/command/project.html#command:project)

**Real example:**
```c
cmake_minimum_required(VERSION 3.27.0)
project(studies)
```

---

<div id="add-executable"></div>

## add_executable()

> The **add_executable()** command tells CMake to create an *executable* using the specified source code files.

**Normal Executables:**
```c
add_executable(<name> [WIN32] [MACOSX_BUNDLE]
               [EXCLUDE_FROM_ALL]
               [source1] [source2 ...])
```

**Imported Executables:**
```c
add_executable(<name> IMPORTED [GLOBAL])
```

**Alias Executables:**
```c
add_executable(<name> ALIAS <target>)
```

**Useful Links:**  
[add_executable](https://cmake.org/cmake/help/latest/command/add_executable.html#normal-executables)

**Real example:**
```c
cmake_minimum_required(VERSION 3.27.0)
project(studies)
add_executable(studies tutorial.cxx)
```









































































<!--- ( References ) --->

---

<div id="ref"></div>

## References

 - [Aula 01 - Ambiente Linux | Histórico | Terminal | Shell | g++ | gdb | make | cmake | Compiladores](https://www.youtube.com/watch?v=JJmf1wlNGeQ&t=1s)
 - [Advanced C and C++ Compiling](https://www.oreilly.com/library/view/advanced-c-and/9781430266679/)
 - [Introdução ao Makefile](https://embarcados.com.br/introducao-ao-makefile/)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
