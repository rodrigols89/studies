# Constants

## Contents

 - [Symbolic Constants](#symbolic-constants)

---

<div id="symbolic-constants"></div>

## Symbolic Constants

> **Symbolic constant** is a way to *define* a value that will be constant throughout our program.

For example, imagine we create a program that converts **hours** in **minutes**:

[hours_to_minutes.cpp](src/hours_to_minutes.cpp)
```cpp
#include <iostream>
using namespace std;

#define SECONDS_PER_HOUR 3600

int main()
{
    int seconds, hours;

    cout << "Enter hours amount: ";
    cin >> hours;

    seconds = hours * SECONDS_PER_HOUR;
    cout << hours << " hours have " << seconds << " seconds.\n";

    return 0;
}
```

**COMPILATION AND RUN:**
```
g++ hours_to_minutes.cpp -o converter

./converter.exe
```

**OUTPUT:**  
```
Enter hours amount: 10
10 hours have 36000 seconds.
```

**NOTE:**  
See that we used the **#define** preprocessing directive and defined the symbolic constant **"SECONDS_PER_HOUR"** which is a value that will be constant throughout our program.

> But why don't we use a *global variable* to store that value?

 - First, because a *symbolic constant* created with the *#define* directive is not stored in memory:
   - That is, we will save (economizar) computational memory.
 - What happens is that at compilation time the compiler will take the value in **"SECONDS_PER_HOUR"** and every time the name **"SECONDS_PER_HOUR"** appears in your code it will replace it with **"3600"**:
   - This is done before compilation and at compile time there will be no **"SECONDS_PER_HOUR"**, just **"3600"** in your code.

---

**REFERENCES:**  
[Aula 06 - Tipos Inteiros | Variáveis | Constantes | Overflow | Underflow | Curso de C++](https://www.youtube.com/watch?v=N2xfTZuLrFI&list=PLX6Nyaq0ebfgWfHqVHVAEPCDG54RLArJh&index=8&t=1604s)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
