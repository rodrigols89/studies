# Debugging

## Contents

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




































































































<!--- ( gdb (GNU Debugger) ) --->

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

 - [](#)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
