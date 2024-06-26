# Compilation

## Contents

 - **Compilation Process:**
   - [Pre-processing (-E)](#intro-to-preprocessing)
   - [Compiling (-S)](#intro-to-compiling)
   - [Assembling (-c)](#intro-to-assembling)
   - [Linking (-o)](#intro-to-linking)
     - [Static Library (Compile Time)](#intro-to-static-libraries)
     - [Dynamic Library (Runtime)](#intro-to-dynamic-libraries)
 - **Tools:**
   - **GNU Make:**
      - [Makefile (targets:prerequisites/command(s), variables, and wildcard functions)](#intro-to-makefile)
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
![img](images/linker-02.png)  


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

---

<div id="intro-to-static-libraries"></div>

## Static Library (Compile Time)

A **"Static Library"** or **"statically-linked library"** or **"archives"** is a collection of object files that are `linked into the program during the linking phase` of compilation *(4th and last phase compilation process)*.

For example, see the image below to understand more easily:

![img](images/static-library-01.png)  

**NOTE:**  
See that a Static Library has **".a"** extension.

> **Ok, but how to create a Static Library and how to use them?**

First, we need to specify to the compiler that we want to compile all files `(*.c/cpp)` into object files `(*.o)` **without linking** with the command below:

```bash
g++ -Wall -pedantic -Werror -Wextra -std=c++20 -c *.cpp
```

Flag description:

 - `g++`
   - The compiler used.
 - `-Wall -pedantic -Werror -Wextra`
   - Generate better code.
 - `-std=c++20`
   - Determine the language standard.
 - `-c`
   - *Compile* and *Assemble* **without link**.
 - `*.cpp`
   - Select all the files with `.cpp` extension in the same folder.

For example, imagine we have the following codes:

[sum_library.h](src/static-library-ex01/sum_library.h)
```cpp
#ifndef SUM_LIBRARY_H
#define SUM_LIBRARY_H

class SumLibrary
{
public:
    static int sum(int a, int b);
};

#endif
```

[sum_library.cpp](src/static-library-ex01/sum_library.cpp)
```cpp
#include "sum_library.h"

int SumLibrary::sum(int a, int b)
{
    return a + b;
}
```

Ok, we have a static library to work with, now let's translate it to object code:

```bash
g++ -Wall -pedantic -Werror -Wextra -std=c++20 -c *.cpp
```

Now, let's check:

**INTPUT:**
```bash
ls
```

**OUTPUT:**
```bash
sum_library.cpp  sum_library.h  sum_library.o
```

Now, let's create the **Static Library (".a")** using the **"ar (archive program)"** command:

```bash
ar -rc libsum.a *.o
```

Flag description:

 - `ar`
   - Archive program.
 - `-rc`
   - “r” insert the files into archive but if any file previously existing are deleted before and then added;
   - “c” create the archive if it did not already exist.
 - `libsum`
   - “lib” + name of the library.
 - `.a`
   - Extension of a library.
 - `*.o`
   - Puts copies of the object files in the library.

To check how many *object files (.o)* the Static Library has, we can use the following command:

**INPUT:**
```bash
ar -t libsum.a
```

**OUTPUT:**
```bash
sum_library.o
```

Now, we need to *index the library*. This index is later used by the compiler to speed up symbol_lookup inside the library:

```bash
ranlib libsum.a
```

**ranlib:**  
The command *"ranlib"* that generate an index to an archive.

**NOTE:**  
Ok, now the library is created and to use it in a program we need only add the library in the *link stage.*

For example, imagine we have the following **main.cpp** that use our Static Library:

[main.cpp](src/static-library-ex01/main.cpp)
```cpp
#include <iostream>
#include "sum_library.h"

int main()
{
    int result = MyLibrary::sum(3, 4);
    std::cout << "The sum is: " << result << std::endl;

    return 0;
}
```

Now, let's create an executable that use our Static Library:

```bash
g++ main.cpp -L. -lsum -o sumProgram.out
```

Flag description:

 - `gcc`
   - The compiler.
 - `main.c`
   - Source code whose the function *sum()* is used.
 - `-L.`
   - Tells the linker to use the library in the given directory, the **“.”** means the current directory.
 - `-l`
   - Specify the library.
 - `sum`
   - The name of the library omitted the **“lib”** prefix and the **“.a”** extension.
 - `-o`
   - Rename the program.
 - `sumProgram.out`
   - Name of the executable.

Now, let's run the program (executable):

**INPUT:**
```bash
./sumProgram.out 
```

**OUTPUT:**
```bash
The sum is: 7
```

### Advantages & Disadvantages

 - **Advantage:**
   - **Speed:** Static libraries are linked into the executable file at *compile time*, which can improve performance by eliminating the need to load and unload the library at runtime.
   - **Security:** Static libraries are more secure than dynamic libraries, as they cannot be modified without recompiling the application.
   - **Stability:** Static libraries are more stable than dynamic libraries, as they are not affected by changes to the library itself or to other applications that use the library.
   - **Static Dependency Resolution:** All dependencies are resolved during *compile-time*, avoiding potential conflicts or errors during runtime.
   - **Deployment Ease:** Application deployment is straightforward since the executable contains all necessary dependencies, eliminating the need for additional libraries on the target system.
   - **Precise Version Control:** Developers have precise control over the version of the library used, reducing the risk of incompatibilities.
 - **Disadvantage:**
   - **Complexity:** Static libraries can make it more difficult to debug and troubleshoot applications, as the library code is embedded in the executable file.
   - **Size:** Static libraries can increase the size of the executable file, which can make it more difficult to distribute and deploy the application.
   - **Portability:** Static libraries can reduce the portability of applications, as they are not portable across different platforms.
   - **More Challenging Updates:** Updating the library requires recompilation and redistribution of the entire application, which can be more time-consuming and complex.
   - **Longer Compilation Times:** Compilation times can be longer, especially in large projects, due to the inclusion of library code directly into the executable.
   - **Higher Memory Usage:** If multiple applications use the same static library, memory overhead may be higher as each application has its copy of the library.

---

<div id="intro-to-dynamic-libraries"></div>

## Dynamic Library (Runtime)

> A **Dynamic Library** or **Shared Library** is a collection of `object file` witch are launched only `during program execution (Runtime)`.

 - A link is created between shared library and executable file. It means that a shared library can be used by any program that needs it.
 - If the library code is updated, it’s not necessary to recompile. It’s location doesn’t move. This method permit to make a green code using less memory.

For example, see the image below to understand more easily:

![img](images/static-x-dynamic.png)  

> **Ok, but how to create a Dynamic Library (Shared Library) and how to use them?**

First, we need to specify to the compiler that we want to compile all files `(*.c/cpp)` into object files `(*.o)` **without linking** with the command below:

```bash
g++ -Wall -pedantic -Werror -Wextra -std=c++20 -fPIC -c *.cpp
```

Flag description:

 - `g++`
   - The compiler used.
 - `-Wall -pedantic -Werror -Wextra`
   - Generate better code.
 - `-std=c++20`
   - Determine the language standard.
 - `fPIC`
   - Position Independent Code, makes addresses in machine code.
 - `-c`
   - *Compile* and *Assemble* **without link**.
 - `*.cpp`
   - Select all the files with `.cpp` extension in the same folder.

For example, imagine we have the following codes:

[sum_library.h](src/static-library-ex01/sum_library.h)
```cpp
#ifndef SUM_LIBRARY_H
#define SUM_LIBRARY_H

class SumLibrary
{
public:
    static int sum(int a, int b);
};

#endif
```

[sum_library.cpp](src/static-library-ex01/sum_library.cpp)
```cpp
#include "sum_library.h"

int SumLibrary::sum(int a, int b)
{
    return a + b;
}
```

Ok, we have a **Dynamic Library (Shared Library)** to work with, now let's translate it to object code:

```bash
g++ -Wall -pedantic -Werror -Wextra -std=c++20 -fPIC -c *.cpp
```

Now, let's check:

**INTPUT:**
```bash
ls
```

**OUTPUT:**
```bash
sum_library.cpp  sum_library.h  sum_library.o
```

Now, let's create the **Dynamic Library (Shared Library)** using the **"g++"** with the **"-shared"** flag:

```bash
g++ -shared -o libsum.so *.o
```

Flag description:

 - `g++`
   - The compiler.
 - `-shared`
   - Produce a shared object which can then be linked with other objects to form an executable.
 - `-o`
   - Rename the program.
 - `libsum`
   - “lib” + name of the library.
 - `.so`
   - Extension of a Dynamic Library.
 - `*.o`
   - Puts copies of the object files in the library.

To check how many *object files (.so)* the **Dynamic Library (Shared Library)** has, we can use the following command:

**INPUT:**
```bash
nm -D libsum.so
```

**OUTPUT:**
```bash
                 w __cxa_finalize@GLIBC_2.2.5
                 w __gmon_start__
                 w _ITM_deregisterTMCloneTable
                 w _ITM_registerTMCloneTable
00000000000010fa T _ZN10SumLibrary3sumEii
```

**NOTE:**  
Ok, now the library is created and to use it in a program we need only add the library in the *link stage.*

For example, imagine we have the following **main.cpp** that use our **Dynamic Library (Shared Library)**:

[main.cpp](src/static-library-ex01/main.cpp)
```cpp
#include <iostream>
#include "sum_library.h"

int main()
{
    int result = MyLibrary::sum(3, 4);
    std::cout << "The sum is: " << result << std::endl;

    return 0;
}
```

Different of the *Static Library*, the **Dynamic Library (Shared Library)** first, need to add the location of the Dynamic Library into the environment variable:

```bash
export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
```

 - `export`
   - Set export attribute for sheel variables.
 - `LD_LIBRARY_PATH`
   - The name of environment variable.
 - `.:`
   - The current directory.
 - `::`
   - The separator
 - `$LD_LIBRARY_PATH`
   - The exit status of the command.

Finally, let's compile the **main.cpp** file with the **Dynamic Library (Shared Library)**:

```bash
g++ main.cpp -L. -lsum -o sumProgram.out
```

Flag description:

 - `gcc`
   - The compiler.
 - `main.c`
   - Source code whose the function *sum()* is used.
 - `-L.`
   - Tells the linker to use the library in the given directory, the **“.”** means the current directory.
 - `-l`
   - Specify the library.
 - `sum`
   - The name of the library omitted the **“lib”** prefix and the **“.a”** extension.
 - `-o`
   - Rename the program.
 - `sumProgram.out`
   - Name of the executable.

Now, let's use the **"ldd"** command to check the dependencies of the **Dynamic Library (Shared Library)**:

> **NOTE:**  
> **ldd (List Dynamic Dependencies)** is a Unix utility that prints the shared libraries required by each program or shared library specified on the command line. 

**INPUT:**
```bash
ldd sumProgram.out
```

**OUTPUT:**
```bash
linux-vdso.so.1 (0x00007ffd52cc1000)
libsum.so => ./libsum.so (0x00007fdc0bc68000)
libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007fdc0ba00000)
libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fdc0b919000)
libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fdc0bc35000)
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fdc0b600000)
/lib64/ld-linux-x86-64.so.2 (0x00007fdc0bc6f000)
```

Now, let's run the program (executable):

**INPUT:**
```bash
./sumProgram.out 
```

**OUTPUT:**
```bash
The sum is: 7
```

### Advantages & Disadvantages

 - **Advantage:**
   - **Smaller Executable Size:** Dynamic libraries are separate from the executable, resulting in smaller executable sizes, especially when multiple applications share the same library.
   - **Portability:** Dynamic libraries are portable across different platforms, as they are not embedded in the executable file.
   - **Complexity:** Dynamic libraries can make it easier to debug and troubleshoot applications, as the library code is not embedded in the executable file.
   - **Easier Updates:** Updating the library is simpler as it can be replaced *without recompiling* the entire application. This facilitates patching and version upgrades.
   - **Memory Efficiency:** Dynamic libraries can be shared among multiple processes, reducing memory usage as the library is loaded into memory only once.
   - **Run-Time Linking:** *Dynamic linking* allows resolving library dependencies at *runtime*, providing flexibility and the ability to load libraries on demand.
   - **Dynamic Loading and Unloading:** Dynamic libraries can be loaded and unloaded at runtime, enabling features like plugin systems and dynamic extensions.
 - **Disadvantage:**
   - **Dependency Management:** Dependency on external libraries introduces the need to manage and distribute additional library files along with the application.
   - **Deployment Complexity:** Deploying applications using dynamic libraries can be more complex as users need to ensure that the required libraries are available on their systems.
   - **Potential Version Conflicts:** Version conflicts may arise if multiple applications require different versions of the same dynamic library, leading to compatibility issues.
   - **Stability:** Dynamic libraries can be less stable than static libraries, as they are affected by changes to the library itself or to other applications that use the library.




























































































































































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

 - **Compilation Process:**
   - [The compilation process in C](https://medium.com/@elodieriou/the-compilation-process-in-c-b4325a4dd953)
   - [The Static libraries in C](https://medium.com/@elodieriou/the-static-libraries-in-c-d310dd7086d3)
   - [The Dynamic libraries in C](https://medium.com/@elodieriou/the-dynamic-libraries-in-c-d5cd1a78b937)
 - **GNU Make:**
   - [Introdução ao Makefile](https://embarcados.com.br/introducao-ao-makefile/)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
