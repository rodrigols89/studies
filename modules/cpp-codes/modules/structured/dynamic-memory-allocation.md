# Dynamic Memory Allocation

## Contents

 - [Memory Allocation: Auto Allocation vs. Dynamic Allocation](#aa-da)
 - [Intro to Dynamic Memory Allocation](#intro-to-dma)
 - [Deleting allocated memory (+delete operator)](#delete-operator)
 - [Memory Leak (+Some solutions)](#memory-leak)
 - [Dynamic Vectors (+Static Vectors vs. Dynamic Vectors)](#dynamic-va)
 - [Assign values to a Dynamic Vector (+The vector name (pointer) points to the first element of a vector)](#assign-values)
 - [Dynamic Records/Structs (+Vector of Records/Structs)](#dynamic-structs)
 - **Tips & Tricks:**
   - [When use Dynamic Memory Allocation?](#when-use-dma)

---

<div id="aa-da"></div>

## Memory Allocation: Auto Allocation vs. Dynamic Allocation

There are two approach to Memory Allocation:

 - **Auto Allocation:**
   - declare variables: *int total = 100;*
 - **Dynamic Allocation:**
   - Allocate memory with the **"new"** operator;
   - Save the memory address in a pointer;
   - Use the pointer to access and modify the data;
   - Free the memory with **"delete"** operator.

![img](images/memory-allocation-01.png)  

---

<div id="intro-to-dma"></div>

## Intro to Dynamic Memory Allocation

To allocate memory (dynamically) with the **"new"** operator to an *unlabeled memory* in C++, we use the follow definition:

![img](images/memory-allocation-02.png)  

For example, see the code below how allocate memory with the **"new"** operator:

[memory_allocation-01.cpp](src/memory_allocation-01.cpp)
```cpp
#include <iostream>
using namespace std;

int main()
{
    int *iptr = new int; // Allocate memory for an Integer.
    *iptr = 1001;        // Save a value (using "*" operator | Indirection Operator)
    cout << "Integer value: " << *iptr << endl;
    cout << "Location: " << iptr << endl;
    cout << "Size of 'iptr': " << sizeof(iptr) << endl;
    cout << "Size of '*iptr': " << sizeof(*iptr) << endl;

    double *dprt = new double;     // Allocate memory for a double
    *dprt = 500.35;                // Save a value (using "*" operator | Indirection Operator)
    cout << "\nFloating-point value: " << *dprt << endl;
    cout << "Location: " << dprt << endl;
    cout << "Size of 'dprt': " << sizeof(dprt) << endl;
    cout << "Size of '*dprt': " << sizeof(*dprt) << endl;

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ memory_allocation-01.cpp -o testNew

./testNew
```

**OUTPUT:**  
```cpp
Integer value: 1001
Location: 0x6b25a0
Size of 'iptr': 8
Size of '*iptr': 4

Floating-point value: 500.35
Location: 0x6b25c0
Size of 'dprt': 8
Size of '*dprt': 8
```

See the abstraction of the code above:

![img](images/memory-allocation-03.png)  

Ok, now let's review the code output:

**OUTPUT:**  
```cpp
Integer value: 1001
Location: 0x6b25a0
Size of 'iptr': 8
Size of '*iptr': 4

Floating-point value: 500.35
Location: 0x6b25c0
Size of 'dprt': 8
Size of '*dprt': 8
```

**What?**  
Why my **pointers have 8 Bytes (both)**?

> **NOTE:**  
> The size of your *pointer (in Bytes)* depends your computer architecture:  
> - 32 bits commonly use 4 Bytes.
> - 64 bits commonly use 8 Bytes.

---

<div id="delete-operator"></div>

## Deleting allocated memory (+delete operator)

> When using **Dynamic Memory Allocation** principles, the programmer always cares about one thing - **Freeing the allocated memory**.

To freeing the allocated memory the programer need to use **"delete"** operator. For example, see the code below how delete allocated memory by the programer:

[](src/)
```cpp
#include <iostream>
using namespace std;

int main()
{
    int *iptr = new int; // Allocate memory for an Integer.
    *iptr = 30;          // Save a value (using "*" operator | Indirection Operator)

    cout << "Memory Address save in 'iptr' pointer: " << iptr << endl;
    cout << "Value save in the Memory Address save in 'iptr' pointer: " << *iptr << endl;
    cout << "Memory Address of 'iptr' pointer: " << &iptr << endl << endl;
    delete iptr;
    cout << "After use 'delete' operator in 'iptr' pointer: " << endl;
    cout << "Memory Address save in 'iptr' pointer: " << iptr << endl;
    cout << "Value save in the Memory Address save in 'iptr' pointer: " << *iptr << endl;
    cout << "Memory Address of 'iptr' pointer: " << &iptr << endl;

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ delete_operator.cpp -o deleteProgram
./deleteProgram 
```

**OUTPUT:**  
```cpp
Memory Address save in 'iptr' pointer: 0x5c0eb0
Value save in the Memory Address save in 'iptr' pointer: 30
Memory Address of 'iptr' pointer: 0x7fffea7d70b8

After use 'delete' operator in 'iptr' pointer: 
Memory Address save in 'iptr' pointer: 0x5c0eb0
Value save in the Memory Address save in 'iptr' pointer: 0
Memory Address of 'iptr' pointer: 0x7fffea7d70b8
```

Seeing for the above program output we can see some observations:

 - **Our 'iptr' pointer still exists (ainda existe) and has the same memory address (0x7fffea7d70b8):**
   - Yes, our **'iptr'** *pointer* still exists(ainda existe), the memory allocated was freed, however, the pointer still exists (ainda existe).
   - Knowing this, we also can save another memory address in the **'iptr'** *pointer*.
 - **Even after freeing the memory our pointer still points to the same memory space (0x5c0eb0):**
   - Yes, our pointer still has the same memory address saved.
   - Knowing this, we need to take care to don't use this pointer to work because this pointer points to memory we don't allocate any more.

---

<div id="memory-leak"></div>

## Memory Leak (+Some solutions)

> The **"new"** operator must (deve) always be balanced with the use of the **"delete"** operator. Otherwise (caso contrário), there is a **memory leak**.

For example, imagine we allocate the following memory:

```cpp
int *p = new int;
*p = 30;
```

![img](images/memory-allocation-04.png)  

See that:

 - First, we allocated memory:
   - `int *p = new int`
 - Next, we put a value in allocated memory:
   - `*p = 30`

Now, imagine we allocate memory to the same pointer without use **"delete"** *operator*:

```cpp
p = new int;
*p = 50;
```

![img](images/memory-allocation-05.png)  

Now, we have a problem:

 - **We don't have any more the old memory address saved in "p":**
   - That's, don't have how to use **"delete"** *operator* in the old allocated memory.
   - We lost the memory address of old allocated memory.

> This is what we know as a ***memory leak***.

For example, see a function that print the ASCII number of a character typed, however, we don't use **"delete"** *operator*:

[print_ascii.h](src/print_ascii.h)
```cpp
#pragma once

void printASCII(char ch);
```

[print_ascii.cpp](src/print_ascii.cpp)
```cpp
#include <iostream>

using namespace std;

void printASCII(char ch)
{
    int *p = new int{ch};
    cout << "The ASCII number is: " << *p << endl;
}
```

[drive_print_ascii.cpp](src/drive_print_ascii.cpp)
```cpp
#include <iostream>
#include "print_ascii.h"

using namespace std;

int main()
{
    char ch;

    cout << "Enter a character: ";
    cin >> ch;

    printASCII(ch);

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ print_ascii.cpp drive_print_ascii.cpp -o printASCII
./printASCII
```

**OUTPUT:**  
```cpp
Enter a character: A
The ASCII number is: 65
```

![img](images/memory-allocation-06.png)  

**NOTE:**  
See that we have a problem... the pointer **"p"** stop existing when the function ends. That's, we don't have any more access to allocated memory in the function.

 - Imagine that our program call the function printASCII() many times?
 - Many times we allocated memory, however, don't freeing the memory.
 - That's, we have a **memory leak** problem.

> **Ok, but how solve that?**

An approach to solve that is using a function that returns a **pointer (memory address)** to our *allocated memory*:

[get_ascii.h](src/get_ascii.h)
```cpp
#pragma once

int *getASCII(char ch);
```

[get_ascii.cpp](src/get_ascii.cpp)
```cpp
int *getASCII(char ch)
{
    int *p = new int{ch};
    return p;
}
```

[drive_get_ascii.cpp](src/drive_get_ascii.cpp)
```cpp
#include <iostream>
#include "get_ascii.h"

using namespace std;

int main()
{
    char ch;

    cout << "Enter a character: ";
    cin >> ch;

    // Pointer (*pnum) var to save memory address returned by getASCII() function.
    int *pnum = getASCII(ch);

    cout << "Value saved in '*pnum' pointer allocated inside getASCII() function: " << *pnum << endl;
    delete pnum; // delete allocated memory inside getASCII() function.
    cout << "Value saved in '*pnum' pointer after delete allocated memory: " << *pnum << endl;

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ get_ascii.cpp drive_get_ascii.cpp -o getASCII
./getASCII 
```

**OUTPUT:**  
```cpp
Enter a character: A
Value saved in '*pnum' pointer allocated inside getASCII() function: 65
Value saved in '*pnum' pointer after delete allocated memory: 0
```

![img](images/memory-allocation-07.png)

 - **See that first we allocated memory inside the function getASCII():**
   - `int *p = new int{ch}`
 - **Next, we returns the memory address (pointer) to allocated memory:**
   - `return p`
   - That's, even (mesmo) if the pointer that pointed to the allocated memory ceases (deixar) to exist (when the function ends) we still (ainda) have the memory address of allocated, passed as return.
 - **Finally, we apply "delete" operator to freeing allocated memory:**
   - `delete pnum`

---

<div id="dynamic-va"></div>

## Dynamic Vectors (+Static Vectors vs. Dynamic Vectors)

Now, let's see the difference between **Static Vectors vs. Dynamic Vectors**:

 - **Static Vectors:**
   - It is necessary to define the size of the array in the declaration​
(size needs to be an integer constant).
 - **Dynamic Vectors:**
   - With the **"new"** *operator* it is possible to create a dynamic vector.
   - Its size can be set at any time​ (size can be read from the user)​

For example, see the **Static Vectors** below:

```cpp
int vet[10];
```

![img](images/memory-allocation-08.png)  

 - See that we create a **static vector** to store 10 integer values:
   - How the vector is **static** we can't *increase* the size.
   - Another observation is that we need to define the size of the vector in the vector definition:
     - `int vet[10]`.
     - That value need be constant *(e.g. 10)* and don't get by the user *(e.g. cin)*.

> **Ok, but how create a Dynamic Vector?**

See the definition below how define a **Dynamic Vector**:

![img](images/dynamic-vector-01.png)  

For example, let's see how creates a **Dynamic Vector** with the size passed by user:

[drive_dynamic_vector.cpp](src/drive_dynamic_vector.cpp)
```cpp
#include <iostream>

using namespace std;

int main()
{
    int vSize;

    cout << "Enter the Vector size: ";
    cin >> vSize;

    int *vec = new int[vSize];
    delete vec;

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ drive_dynamic_vector.cpp -o dynamicVector.out && ./dynamicVector.out
```

**OUTPUT:**  
```cpp
Enter the Vector size: 10
```

**NOTE:**  
However, the **Dynamic Vector** can't be increased after created. Yes, he is created dynamically, but don't be increase after created.

For example:

```
vSize += 10;
```

> **Don't works!**

---

<div id="assign-values"></div>

## Assign values to a Dynamic Vector (+The vector name (pointer) points to the first element of a vector)

Before learn how assign values to dynamic vectors you need to know that:

> **The vector name (pointer) points to the first element of a vector.**

For example, let's see how assign values in a dynamic vector and show the first element of a vector from a pointer:

[drive_assign.cpp](src/drive_assign.cpp)
```cpp
#include <iostream>

using namespace std;

int main()
{
    int vSize = 5;

    int *vec = new int[vSize];
    vec[0] = 10;
    vec[1] = 20;
    vec[2] = 30;
    vec[3] = 40;
    vec[4] = 50;

    cout << "The first value get by 'vec[0]': " << vec[0] << endl;
    cout << "The first value get by '*vec': " << *vec << endl;

    for (int i = 0; i < vSize; i++)
        cout << "Value in index " << i << " is " << vec[i] << endl;

    delete []vec;
    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ drive_assign.cpp -o assignEX.out && ./assignEX.out
```

**OUTPUT:**  
```cpp
The first value get by 'vec[0]': 15
The first value get by '*vec': 15
Value in index 0 is 15
Value in index 1 is 5
Value in index 2 is 30
Value in index 3 is 28
Value in index 4 is 40
```

See that:

 - **The name of a vector (pointer):**
   - Has the memory address to the first element of a vector.
   - That's, we can access that value by `*vec`.
 - **Finally, see we use another approach to freeing the allocated memory:**
   - `delete []vec`

For example, see the image below to understand more easily:

![img](images/dynamic-vector-02.png)  

---

<div id="dynamic-structs"></div>

## Dynamic Records/Structs (+Vector of Records/Structs)

> Ok, but I can create Dynamic Records (structs)? Yes, of course!

For example, see the code below how create a Dynamic Records (structs):

[player.h](src/player.h)
```cpp
#pragma once

struct player
{
    char name[20];
    float salary;
    unsigned goals;
};
```

[drive_dynamic_struct.cpp](src/drive_dynamic_struct.cpp)
```cpp
#include <iostream>
#include "player.h"

using namespace std;

int main()
{
    player *messi = new player{"Messi", 100000.00f, 600};

    cout << "Player name: " << messi->name << endl;
    cout << "Player salary: " << messi->salary << endl;
    cout << "Player goals: " << messi->goals << endl;

    delete messi;
    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ drive_dynamic_struct.cpp -o dynamicStruct.out && ./dynamicStruct.out
```

**OUTPUT:**  
```cpp
Player name: Messi
Player salary: 100000
Player goals: 600
```

> **Nice! But how create a Vector of Records (structs)?**

[player.h](src/player.h)
```cpp
#pragma once

struct player
{
    char name[20];
    float salary;
    unsigned goals;
};
```

[drive_vector_to_struct.cpp](src/drive_vector_to_struct.cpp)
```cpp
#include <iostream>
#include "player.h"

using namespace std;

int main()
{
    int playersSize;

    cout << "Enter the number of players: ";
    cin >> playersSize;

    player *vecToPlayers = new player[playersSize];

    for (int i = 0; i < playersSize; i++)
    {
        cout << "\nEnter the name of player " << i << ": ";
        cin >> vecToPlayers[i].name;
        cout << "Enter the salary of player " << i << ": ";
        cin >> vecToPlayers[i].salary;
        cout << "Enter the number of goals of player " << i << ": ";
        cin >> vecToPlayers[i].goals;
    }

    for (int i = 0; i < playersSize; i++)
    {
        cout << "\nThe name of player " << i << ": " << vecToPlayers[i].name << endl;
        cout << "The salary of player " << i << ": " << vecToPlayers[i].salary << endl;
        cout << "The number of goals of player " << i << ": " << vecToPlayers[i].goals << endl;
    }

    delete []vecToPlayers;
    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ drive_vector_to_struct.cpp -o vectorToStruct.out && ./vectorToStruct.out
```

**INPUT:**  
```cpp
Enter the number of player: 3

Enter the name of player 0: Messi
Enter the salary of player 0: 10000000
Enter the number of goals of player 0: 1000

Enter the name of player 1: Neymar
Enter the salary of player 1: 80000
Enter the number of goals of player 1: 700

Enter the name of player 2: Mbappe
Enter the salary of player 2: 10000
Enter the number of goals of player 2: 300
```

**OUTPUT:**  
```cpp
The name of player 0: Messi
The salary of player 0: 1e+07
The number of goals of player 0: 1000

The name of player 1: Neymar
The salary of player 1: 80000
The number of goals of player 1: 700

The name of player 2: Mbappe
The salary of player 2: 10000
The number of goals of player 2: 300
```

---

<div id="when-use-dma"></div>

## When use Dynamic Memory Allocation?

 - **When you create a variable inside a function (scope), however, want to use outside the function (scope):**
   - If you create the variable (memory space) dynamically it will remain there even if the function (scope) ends.
   - This variable (memory space) will only cease to exist when the program ends or you delete (freed) it with the "delete" operator.

---

**REFERENCES:**  
[Aula 15 - Alocação Dinâmica de Memória | Operadores new e delete | Vetores Dinâmicos | Curso de C++](https://www.youtube.com/watch?v=qYUiBzxdf-U&t)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
