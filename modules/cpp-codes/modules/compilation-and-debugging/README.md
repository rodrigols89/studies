# Compilation & Debugging

## Contents

 - **Compilation:**
   - **Concepts:**
     - [x](#)
   - **Tools:**
     - **GNU Compiler Collection (GCC/G++):**
       - **Options:**
         - [x](#)
     - **GNU Make:**
        - [Makefile (targets:prerequisites/command(s), variables, and wildcard functions)](#intro-to-makefile)
     - **CMake:**
       - [Intro to CMake](#intro-to-cmake)
       - **CMakeLists.txt:**
         - [cmake_minimum_required()](#cmake-minimum-required)
         - [project()](#project)
         - [add_executable()](#add-executable)
 - **Debugging:**
   - **gdb (GNU Debugger):**
     - [Intro to gdb (GNU Debugger)](#intro-to-gdb)
     - [Interactive Debug](#interactive-debug)
     - **GDB commands:**
       - [run](#run-r)
       - [list](#list-l)
       - [break](#break-b)
       - [next and print](#next-print)
       - [step](#step)
       - [frame (where I stopped debug?)](#frame)
       - [set](#set)
 - [**References**](#ref)

<!--- ( Compilation/Concepts ) --->

---

<div id=""></div>








































<!--- ( Compilation/Tools/GCC/G++ ) --->

---

<div id=""></div>








































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








































<!--- ( Debugging/gdb ) --->

---

<div id="intro-to-gdb"></div>

## Intro to gdb (GNU Debugger)

> The first thing you need to know is that before debugging a C++ program you'll need to compile the program (e.g. using "g++ -g" option).

For example, see the code below:

[showName.cpp](src/showName.cpp)
```cpp
#include <iostream>
#include <string>
#include <sstream>

std::string showName(const int &age, const std::string &name)
{
    std::ostringstream ss;
    ss << "Name: " << name << ", Age: " << age;
    return ss.str();
}

int main()
{
    int age = 30;
    std::string name = "Rodrigo";

    std::string result = showName(age, name);
    std::cout << result << "\n";
    return 0;
}
```

Now, let's compiler this code as debug:

**COMPILATION:**
```bash
g++ showName.cpp -o test.out -g
```

Finally, to start the debug:


**DEBUG:**
```bash
gdb ./test.out
```

---

<div id="interactive-debug"></div>

## Interactive Debug

There are two common approaches to interactively debugging a program:

 - First, passing the argument **"-tui"** to the GDB:
   - `gdb exec-file -tui`
 - Second, enter **"+"** on GDB to show you the code visually.

---

<div id="run-r"></div>

## run

> **"run"** or **"r"** executes the program from **start** to **end**.

For example:

[showName.cpp](src/showName.cpp)
```cpp
#include <iostream>
#include <string>
#include <sstream>

std::string showName(const int &age, const std::string &name)
{
    std::ostringstream ss;
    ss << "Name: " << name << ", Age: " << age;
    return ss.str();
}

int main()
{
    int age = 30;
    std::string name = "Rodrigo";

    std::string result = showName(age, name);
    std::cout << result << "\n";
    return 0;
}
```

**COMPILATION:**
```bash
g++ showName.cpp -o test.out -g
```

**DEBUG:**
```bash
gdb ./test.out
```

**GDB:**
```bash
run
```

**OUTPUT:**
```bash
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Name: Rodrigo Leite
[Inferior 1 (process 9268) exited normally]
(gdb) 
```

**NOTE:**  
You can also pass arguments if the program needs some command-line arguments to be passed to it:

**GDB:**
```bash
run arg1 arg2
```

---

<div id="list-l"></div>

## list

> **"list"** or **"l"** displays the code.

The "list" command in GDB (GNU Debugger) is used to display the source code of the program being debugged. It shows a portion of the source code around the current execution line or a specific location specified as an argument.

Here is the basic syntax of the "list" command:

```bash
(gdb) list [START_LINE [, END_LINE]]
```

Arguments of the **"list"** command:

 - **START_LINE (optional):**
   - Specifies the starting line from which the source code will be displayed. *If no value is provided, the display will start at the current execution line*.
 - **END_LINE (optional):**
   - Specifies the ending line up to which the source code will be displayed. *If no value is provided, the display will continue until the default ending line, which is typically 10 lines after the starting line*.

Additionally, you can also use additional options with the **"list"** command to modify its behavior. Some examples of these options are:

 - **list -**
   - Use the hyphen to display the source code preceding the current execution line.
   - This command is useful for gdb to show 10 lines of code *above* the current line. Just continue with **"list -"** until you get where you want it (até chegar onde você quer).
 - **list +**
   - Use the plus sign to display the source code following the current execution line.
   - This command is useful for gdb to show 10 lines of code *below* the current line. Just continue with **"list +"** until you get where you want (até chegar onde você quer).
 - **You can also specify how many lines you show above or below:**
   - list -5
   - list +5
 - **FILE**
   - Specifies the source file in which you want to display the code.
   - For example, **"list main.c"** will display the source code from the **"main.c"** file.

Let's see an example now:

[showName.cpp](src/showName.cpp)
```cpp
#include <iostream>
#include <string>
#include <sstream>

std::string showName(const int &age, const std::string &name)
{
    std::ostringstream ss;
    ss << "Name: " << name << ", Age: " << age;
    return ss.str();
}

int main()
{
    int age = 30;
    std::string name = "Rodrigo";

    std::string result = showName(age, name);
    std::cout << result << "\n";
    return 0;
}
```

**COMPILATION:**
```bash
g++ showName.cpp -o test.out -g
```

**DEBUG:**
```bash
gdb ./test.out
```

**GDB:**
```bash
list 1, 20
```

**OUTPUT:**
```bash
(gdb) list 1, 20
1       #include <iostream>
2       #include <string>
3       #include <sstream>
4
5       std::string showName(const std::string &name, const std::string &lastName)
6       {
7           std::string msg = "Name: " + name + " " + lastName;
8           return msg;
9       }
10
11      int main()
12      {
13          std::string name = "Rodrigo";
14          std::string lastName = "Leite";
15
16          std::string result = showName(name, lastName);
17          std::cout << result << "\n";
18          return 0;
19      }
(gdb) 
```

---

<div id="break-b"></div>

## break

> **"break"** or **"b"** sets a *breakpoint on a particular line or function*.

 - We can set a breakpoint on a particular line, just pass the line number.
 - Or we can sets breakpoint on a function, just pass the function name.

The following example sets a breakpoint at the start of the main function:

**GDB:**
```bash
break main
```

The next example sets a breakpoint at a specific line (17):

**GDB:**
```bash
break 17
```

The next example lists all of the breakpoints:

**GDB:**
```bash
info break
```

**OUTPUT:**
```bash
(gdb) info break
Num     Type           Disp Enb Address            What
1       breakpoint     keep y   0x00000000004023b7 in main() at showName.cpp:13
2       breakpoint     keep y   0x0000000000402428 in main() at showName.cpp:17
(gdb) 
```

The next example deletes the first breakpoint:

**GDB:**
```bash
delete 1
```

**NOTE:**  
Here, we delete a break breakpoint by your number not your line.

```bash
(gdb) info break
Num     Type           Disp Enb Address            What
 1       breakpoint     keep y   0x00000000004023b7 in main() at showName.cpp:13
 2       breakpoint     keep y   0x0000000000402428 in main() at showName.cpp:17
 |
 |
 ------ (breakpoint number).
(gdb) 
```

---

<div id="next-print"></div>

## next and print

> The "next" statement execute the next statement.

> **NOTE:**  
> If the next statement is a function call, execute the entire function and return to the next line of code.

For example, imagine we have the following code:

[debug.cpp](src/debug.cpp)
```cpp
#include <iostream>
#include <string>

int add(const int &x, const int &y);
int sub(const int &x, const int &y);
int mult(const int &x, const int &y);
float divFunc(const int &x, const int &y);

int main(int argc, char *argv[])
{
    int x = 5;
    int y = 10;
    int add_result = add(x, y);
    std::cout << "The sum between " << x << " and " << y << " is: " << add_result << "\n";

    int w = 5;
    int z = 10;
    int sub_result = sub(w, z);
    std::cout << "The subtraction between " << w << " and " << z << " is: " << sub_result << "\n";

    int r = 5;
    int s = 10;
    int mult_result = mult(r, s);
    std::cout << "The multiplication between " << r << " and " << s << " is: " << mult_result << "\n";

    float g = 5;
    float h = 10;
    float div_result = divFunc(g, h);
    std::cout << "The division between " << g << " and " << h << " is: " << div_result << "\n";

    return 0;
}

int add(const int &x, const int &y)
{
    int result;
    result = x + y;
    return result;
}

int sub(const int &x, const int &y)
{
    int result;
    result = x - y;
    return result;
}

int mult(const int &x, const int &y)
{
    int result;
    result = x * y;
    return result;
}

float divFunc(const int &x, const int &y)
{
    float div;
    div = static_cast<float>(x) / y;
    return div;
}
```

**COMPILATION:**
```bash
g++ debug.cpp -o test.out -g
```

**DEBUG:**
```bash
gdb ./test.out
```

To start let's run the code:

**GDB:**
```bash
run
```

**OUTPUT:**
```bash
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
The sum between 5 and 10 is: 15
The subtraction between 5 and 10 is: -5
The multiplication between 5 and 10 is: 50
The division between 5 and 10 is: 0.5
[Inferior 1 (process 8152) exited normally]
(gdb)
```

Now, let's print the code:

**GDB:**
```bash
(gdb) list 1
1       #include <iostream>
2       #include <string>
3
4       int add(const int &x, const int &y);
5       int sub(const int &x, const int &y);
6       int mult(const int &x, const int &y);
7       float divFunc(const int &x, const int &y);
8
9       int main(int argc, char *argv[])
10      {
(gdb) list
11          int x = 5;
12          int y = 10;
13          int add_result = add(x, y);
14          std::cout << "The sum between " << x << " and " << y << " is: " << add_result << "\n";
15
16          int w = 5;
17          int z = 10;
18          int sub_result = sub(w, z);
19          std::cout << "The subtraction between " << w << " and " << z << " is: " << sub_result << "\n";
20
(gdb) list
21          int r = 5;
22          int s = 10;
23          int mult_result = mult(r, s);
24          std::cout << "The multiplication between " << r << " and " << s << " is: " << mult_result << "\n";
25
26          float g = 5;
27          float h = 10;
28          float div_result = divFunc(g, h);
29          std::cout << "The division between " << g << " and " << h << " is: " << div_result << "\n";
30
(gdb) list
31          return 0;
32      }
33
34      int add(const int &x, const int &y)
35      {
36          int result;
37          result = x + y;
38          return result;
39      }
40
(gdb) list
41      int sub(const int &x, const int &y)
42      {
43          int result;
44          result = x - y;
45          return result;
46      }
47
48      int mult(const int &x, const int &y)
49      {
50          int result;
(gdb) list
51          result = x * y;
52          return result;
53      }
54
55      float divFunc(const int &x, const int &y)
56      {
57          float div;
58          div = static_cast<float>(x) / y;
59          return div;
60      }
(gdb) list
Line number 61 out of range; debug.cpp has 60 lines.
```

Ok, now let's add a breakpoints starting from the main() function:

**GDB:**
```bash
break main
```

**OUTPUT:**
```bash
Breakpoint 1 at 0x401185: file debug.cpp, line 11.
```

Now, let's *run* the program again:

**GDB:**
```bash
run
```

**OUTPUT:**
```bash
Breakpoint 1, main (argc=1, argv=0x7fffffffdc48) at debug.cpp:11
11          int x = 5;
```

> **NOTE:**  
> See that now we are on line 11, however, this line (instruction) has not yet been executed (ainda não foi executada).

For example, we can use the **GDB "print" statement** to show the value in the **"x" variable**:

**GDB:**
```bash
(gdb) print x
$1 = 0
(gdb) print y
$2 = 0
```

> **What?**  
> Then, the problem here is that we are on line 11, however, this line (instruction) has not yet been executed (ainda não foi executada).

A possible GDB command to execute this line is the command "next", for example:

**GDB:**
```bash
(gdb) next
12          int y = 10;
(gdb) print x
$3 = 5
(gdb) next
13          int add_result = add(x, y);
(gdb) print y
$4 = 10
```

> **NOTE:**  
> See that, we run the **GDB "next"** command to run the current line instruction.

Ok now, let's run some instructions:

**GDB:**
```bash
Breakpoint 1, main (argc=1, argv=0x7fffffffdc48) at debug.cpp:11
11          int x = 5;
(gdb) next
12          int y = 10;
(gdb) next
13          int add_result = add(x, y);
(gdb) next
14          std::cout << "The sum between " << x << " and " << y << " is: " << add_result << "\n";
(gdb) 
```

See that:

 - If you pay attention in line (instruction) 13, the **GDB "next"** command runs the *add()* function and gets your return, however, does not come in to debug (não entra para depurar) the function's internal instructions.
 - This is because, if the next statement is a function, execute the entire function and get your return without coming into the function to debug internal instructions.

> **Ok, but how to solve that?**
> Using **GDB "step"** command.

---

<div id="step"></div>

## step

> The **"step"** statement execute the next statement.

> **NOTE:**  
> If the next statement is a function call, step into the function *(i.e. start debugging inside the function itself)*.

Let's debug the **add()** function step by step using **GDB "step" command**:

**GDB:**
```bash
(gdb) break main
Breakpoint 1 at 0x4013ee: file debug.cpp, line 37.
```

Now, let's run:

**GDB:**
```bash
run
```

**OUTPUT:**
```bash
Breakpoint 1, main (argc=1, argv=0x7fffffffdc48) at debug.cpp:11
11          int x = 5;
```

Now, let's run the **"step"** command until inside the add() function:

**GDB:**
```bash
(gdb) step
12          int y = 10;
(gdb) step
13          int add_result = add(x, y);
(gdb) step
add (x=@0x7fffffffdb0c: 5, y=@0x7fffffffdb08: 10) at debug.cpp:37
37          result = x + y;
```

Ok, here we can see the **"x"** and **"y"** value passed as argument to the add() function:

**GDB:**
```bash
(gdb) print x
$1 = (const int &) @0x7fffffffdb0c: 5
(gdb) print y
$2 = (const int &) @0x7fffffffdb08: 10
(gdb) print result
$3 = 0
```

> **What? Why "result" variable is zero?**  
> That's because we haven't yet executed the statement **"result = x + y;"** yet (ainda). That is, we are still standing on that line.

Now, let's run the **"step"** command and check the value in **"result" variable**:

**GDB:**
```bash
(gdb) step
38          return result;
(gdb) print result
$4 = 15
```

Nice, now we can follow the debug process back to the main function running the **"step"** command:

**GDB:**
```bash
(gdb) step
38          return result;
(gdb) step
39      }
(gdb) step
main (argc=1, argv=0x7fffffffdc48) at debug.cpp:14
14          std::cout << "The sum between " << x << " and " << y << " is: " << add_result << "\n";
(gdb) 
```

> **NOTE:**  
> See that now we are on below instruction below the add() function call.

```cpp
   int add_result = add(x, y);
-> std::cout << "The sum between " << x << " and " << y << " is: " << add_result << "\n";
```

---

<div id="frame"></div>

## frame (where I stopped debug?)

Now imagine you are out to lunch and when back don't remember where you stopped debug.

> **How check it?**  
> Using the **frame** command.

**GDB:**
```bash
                                                        ||
                                                        ||
                                                        ||
    (gdb) frame                                         \/
    #0  main (argc=1, argv=0x7fffffffdc48) at debug.cpp:14
--> 14          std::cout << "The sum between " << x << " and " << y << " is: " << add_result << "\n";
```

See that you stopped on the 14 line.

> **NOTE:**  
> You can also see the lines below from where you stopped using **"list +10"** command. For example:

**OUTPUT:**
```bash
(gdb) frame
#0  main (argc=1, argv=0x7fffffffdc48) at debug.cpp:14
14          std::cout << "The sum between " << x << " and " << y << " is: " << add_result << "\n";
(gdb) list +10
19          std::cout << "The subtraction between " << w << " and " << z << " is: " << sub_result << "\n";
20
21          int r = 5;
22          int s = 10;
23          int mult_result = mult(r, s);
24          std::cout << "The multiplication between " << r << " and " << s << " is: " << mult_result << "\n";
25
26          float g = 5;
27          float h = 10;
28          float div_result = divFunc(g, h);
(gdb) 
```

---

<div id="set"></div>

## set

The **"set"** command is used to:

 - Modify variables values.
 - Or settings during program debugging.
 - It allows you to assign a new value to a variable or configure specific options of GDB.

Here is the basic syntax of the **"set"** command:

```bash
set <variable> <value>
```

 - Here, `<variable>` represents the name of the variable you want to modify.
 - And `<value>` is the new value you want to assign to that variable.








































<!--- ( References ) --->

---

<div id="ref"></div>

## References

 - [Aula 01 - Ambiente Linux | Histórico | Terminal | Shell | g++ | gdb | make | cmake | Compiladores](https://www.youtube.com/watch?v=JJmf1wlNGeQ&t=1s)
 - [Advanced C and C++ Compiling](https://www.oreilly.com/library/view/advanced-c-and/9781430266679/)
 - [Introdução ao Makefile](https://embarcados.com.br/introducao-ao-makefile/)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
