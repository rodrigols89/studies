# NamespacesNamespace in C++

## Contents

 - [Intro to Namespace](#intro-to-namespace)
 - [The "using" directive](#using-directive)
 - [Nested Namespaces (+Scope Resolution Operator `"::"`)](#nested-namespaces)
 - [Accessing specific namespaces (+Scope Resolution Operator `"::"`)](#accessing-specific-namespaces)
 - [Classes and Methods in Namespace](#classes-methods-namespace)
 - [Extending namespaces (Using same name twice)](#extending-namespaces)
 - [Using namespace in header (.h) files](#namespace-header)
 - [Namespace alias](#namespace-alias)
 - **Tips & Tricks:**
   - [Advantage of Namespace to avoid name collision](#advantage-avoid-collision)

---

<div id="intro-to-namespace"></div>

## Intro to Namespace

**Namespace** provide the *space* where we can define or declare:

 - Variable.
 - Functions.
 - Classes:
   - Methods
 - etc...

> **NOTE:**  
> Using namespace, you can define the **space** or **context** in which identifiers are defined i.e. variable, method, classes. In essence, a namespace defines a **scope**.

---

<div id="using-directive"></div>

## The "using" directive

> You can also avoid prepending of namespaces with the **"using"** namespace directive. This directive tells the compiler that the subsequent code is making use of names in the specified namespace.

For example, see the code and output below:

[namespaces-01.cpp](src/namespaces-01.cpp)
```cpp
#include <iostream>
using namespace std;

// First name space.
namespace first_space
{
    void func()
    {
        cout << "Inside first_space" << endl;
    }
}

// Second name space
namespace second_space
{
    void func()
    {
        cout << "Inside second_space" << endl;
    }
}

using namespace first_space;

int main()
{
    // This calls function from first name space.
    func();
    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ namespaces-01.cpp -o test && ./test
```

**OUTPUT:**  
```cpp
Inside first_space
```

 - **First, we use *C++ standard library (std)* with *"using"* directive:**
   - `using namespace std;`
   - For now, our program (all file) is using "std" namespace.
 - **Now, we define two namespaces for us:**
   - `namespace first_space`.
   - `namespace second_space`.
   - *"first_space"* and *"second_space"* namespaces are using *"std"* namespace.
 - **Finally, we set our program to use "first_space" namespace:**
   - `using namespace first_space;`
   - Thenm call the function **func()**.
 - **Why the function in the "first_space" was called and not the function in the "second_space"?**
   - Because we define our programa to use "first_space" namespace no "second_space":
     - `using namespace first_space;`

---

<div id="nested-namespaces"></div>

## Nested Namespaces (+Scope Resolution Operator `"::"`)

Namespaces can be nested where you can define one namespace inside another name space as follows:

```cpp
namespace namespace_name1
{
    // code declarations.
    namespace namespace_name2 
    {
        // code declarations.
    }
}
```

You can access members of nested namespace by using **Scope Resolution Operator "::"** as follows:

```cpp
// To access members of namespace_name2.
using namespace namespace_name1::namespace_name2;
```

For example, see the nested namespaces code below:

[nested_namespaces.cpp](src/nested_namespaces.cpp)
```cpp
// C++ program to demonstrate nesting of namespaces
#include <iostream>
using namespace std;

// Nested namespace
namespace out
{
    int val = 5;
    namespace in
    {
        int val2 = val;
    }
}

// Driver code
int main()
{
    cout << out::in::val2; // prints 5
    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ nested_namespaces.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
5
```

---

<div id="accessing-specific-namespaces"></div>

## Accessing specific namespaces (+Scope Resolution Operator `"::"`)

Imagine we have a function **greetings()** that say:

 - **Good Morning!**
   - In the morning.
 - **Good Afternoon!**
   - In the afternoon.
 - **Good night!**
   - At Night.

Ok, we can create 3 namespaces represents 3 times of day; Create 3 functions **greetings()** 1 for each time of day and finally, use **Scope Resolution Operator `"::"`** to access the specific namespace:

[greetings_namespaces.cpp](src/greetings_namespaces.cpp)
```cpp
#include <iostream>
using namespace std;

namespace morning
{
    void greetings()
    {
        cout << "Good Morning!"
             << "\n";
    }
}

namespace afternoon
{
    void greetings()
    {
        cout << "Good Afternoon!"
             << "\n";
    }
}

namespace night
{
    void greetings()
    {
        cout << "Good night!"
             << "\n";
    }
}

int main()
{
    morning::greetings();
    afternoon::greetings();
    night::greetings();

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ greetings_namespaces.cpp -o test && ./test
```

**OUTPUT:**  
```cpp
Good Morning!
Good Afternoon!
Good night!
```

---

<div id="classes-methods-namespace"></div>

## Classes and Methods in Namespace

We can also be create classes inside namespaces, for example, the following is a simple way to create classes in a namespace:

[namespace_class.cpp](src/namespace_class.cpp)
```cpp
#include <iostream>
using namespace std;

namespace ns
{
    // A Class in a namespace
    class geek
    {
    public:
        void display()
        {
            cout << "ns::geek::display()" << endl;
            ;
        }
    };
}

int main()
{
    // Creating Object of geek Class
    ns::geek obj;
    obj.display();

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ namespace_class.cpp -o test && ./test
```

**OUTPUT:**  
```cpp
ns::geek::display()
```

**NOTE:**  
A class can also be:

 - Declared inside namespace.
 - And defined outside namespace.

Using the following syntax: 

[namespace_class-v2.cpp](src/namespace_class-v2.cpp)
```cpp
#include <iostream>
using namespace std;

namespace ns
{
    // Only declaring class here
    class geek;
} // namespace ns

// Defining class outside
class ns::geek
{
public:
    void display() { cout << "ns::geek::display()\n"; }
};

int main()
{
    // Creating Object of geek Class
    ns::geek obj;
    obj.display();

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ namespace_class-v2.cpp -o test && ./test
```

**OUTPUT:**  
```cpp
ns::geek::display()
```

**NOTE:**  
We can **define** methods as well outside the namespace. The following is an example code below: 

[namespace_method.cpp](src/namespace_method.cpp)
```cpp
#include <iostream>
using namespace std;

// Creating a namespace
namespace ns
{
    void display();
    class geek
    {
    public:
        void display();
    };
} // namespace ns


// Defining methods of namespace
void ns::geek::display()
{
    cout << "ns::geek::display()\n";
}

void ns::display() { cout << "ns::display()\n"; }

// Driver code
int main()
{
    ns::geek obj;
    ns::display();
    obj.display();

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ namespace_method.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
ns::display()
ns::geek::display()
```

---

<div id="extending-namespaces"></div>

## Extending namespaces (Using same name twice)

 - It is also possible to create two namespace blocks having the same name.
 - The second namespace block is nothing but actually the continuation of the first namespace.

> **NOTE:** 
> In simpler words, we can say that both the namespaces are not different but actually the same, which are being defined in parts.

For example, see the code below:

[extending_namespaces.cpp](src/extending_namespaces.cpp)
```cpp
#include <iostream>
using namespace std;

// first name space
namespace first
{
    int val1 = 500;
}

// rest part of the first namespace
namespace first
{
    int val2 = 501;
}

int main()
{
    cout << first::val1 << "\n";
    cout << first::val2 << "\n";

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ extending_namespaces.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
500
501
```

 - We have two namespaces with the same name.
 - The second namespace is continuation of the first namespace.
 - We can access both from the same name "first".

---

<div id="namespace-header"></div>

## Using namespace in header (.h) files

> We can create **namespace** in one file and access contents using another program.

This is done in the following manner:

 - We need to create two files. One containing the namespace and all the data members and member functions we want to use later.
 - And the other program can directly call the first program to use all the data members and member functions in it.

For example, see the codes below:

[file1.h](src/file1.h)
```cpp
#pragma once

namespace foo
{
    int value()
    {
        return 5;
    }
}
```

[file2.cpp](src/file2.cpp)
```cpp
#include <iostream>
#include "file1.h" // Including file1

using namespace std;

int main()
{
    cout << foo::value();
    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ file2.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
5
```

**NOTE:**  
Here we can see that the **namespace** is created in **file1.h** and the **value()** of that **namespace** is getting called in **file2.cpp**.

---

<div id="namespace-alias"></div>

## Namespace alias

In *C++*, you can use an **alias** name for your *namespace* name, for ease of use. Existing namespaces can be aliased with new names, with the following syntax:

```cpp
namespace new_name = current_name;
```

For example, see the code below how **alias** a namespace:

[alias_namespace.cpp](src/alias_namespace.cpp)
```cpp
#include <iostream>

namespace name1
{
    namespace name2
    {
        namespace name3
        {
            int var = 42;
        }
    }
}

// Apply aliasing to "name3" namespace.
namespace alias = name1::name2::name3;

int main()
{
    std::cout << alias::var << '\n';
}
```

**COMPILATION AND RUN:**
```cpp
g++ alias_namespace.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
42
```

---

<div id="advantage-avoid-collision"></div>

## Advantage of Namespace to avoid name collision

 - Example, you might be writing some code that has a function called **xyz()** and there is another library available which is also having same function **xyz()**:
   - Now the compiler has no way of knowing which version of **xyz()** function you are referring to within your code.
 - A namespace is designed to overcome this difficulty and is used as additional information to differentiate similar functions, classes, variables etc. with the same name available in different libraries.
 - The best example of namespace **scope** is the *C++ standard library (std)* where all the classes, methods and templates are declared. Hence while writing a C++ program we usually include the directive **"using namespace std;"**.

---

**REFERENCES:**  
[Namespace in C++ | Set 1 (Introduction)](https://www.geeksforgeeks.org/namespace-in-c/)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
