# Access Modifiers & Encapsulation

## Contents

 - **Public:**
   - [Intro to "public" modifier](#intro-public-modifier)
 - **Private:**
   - [Intro to "private" modifier](#intro-private-modifier)
 - **Protected:**
   - [Intro to "protected" modifier](#intro-protected-modifier)
 - **Encapsulation:**
   - [Intro to Encapsulation](#intro-to-encapsulation)
   - [Getters & Setters: Employee](#get-set-employee)
   - [Getters & Setters: Person](#get-set-person)

---

<div id="intro-public-modifier"></div>

## Intro to "public" modifier

> **All the class members declared under the public specifier will be available to everyone.**

 - The data members and member functions declared as public can be accessed by other classes and functions too.
 - The public members of a class can be accessed from anywhere in the program using the direct member **access operator (.)** with the object of that class.

For example, see the code below:

[publicCircle.h](src/publicCircle.h)
```cpp
class Circle
{
public:
    double radius;

    double compute_area();
};
```

[publicCircle.cpp](src/publicCircle.cpp)
```cpp
#include "publicCircle.h"

double Circle::compute_area()
{
    return 3.14 * radius * radius;
}
```

[drive_publicCircle.cpp](src/drive_publicCircle.cpp)
```cpp
#include <iostream>
#include "publicCircle.h"

int main()
{
    Circle obj;

    // Accessing public dat amember outside the class.
    obj.radius = 5.5;

    std::cout << "Radius is: " << obj.radius << "\n";
    std::cout << "Area is: " << obj.compute_area();
    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ publicCircle.cpp drive_publicCircle.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
Radius is: 5.5
Area is: 94.985
```

**NOTE:**  
In the above program, the data **member radius** is declared as public so it could be accessed outside the class and thus was allowed access from inside **main()**.

---

<div id="intro-private-modifier"></div>

## Intro to "private" modifier

> **The class members declared as private can be accessed only by the member functions inside the class.**

 - They are not allowed to be accessed directly by any object or function outside the class.
 - Only the member functions or the friend functions are allowed to access the private data members of the class. 

For example, see the code below:

[privateCircle.h](src/privateCircle.h)
```cpp
class Circle
{
private:
    double radius;

public:
    double compute_area();
};
```

[privateCircle.cpp](src/privateCircle.cpp)
```cpp
#include "privateCircle.h"

double Circle::compute_area()
{
    return 3.14 * radius * radius;
}
```

[drive_privateCircle.cpp](src/drive_privateCircle.cpp)
```cpp
#include <iostream>
#include "privateCircle.h"

int main()
{
    // Creating object of the class
    Circle obj;

    // Trying to access private data member
    // directly outside the class
    obj.radius = 1.5;

    std::cout << "Area is:" << obj.compute_area();
    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ privateCircle.cpp drive_privateCircle.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
drive_privateCircle.cpp: In function 'int main()':
drive_privateCircle.cpp:11:9: error: 'double Circle::radius' is private within this context
     obj.radius = 1.5;
         ^~~~~~
In file included from drive_privateCircle.cpp:2:
privateCircle.h:4:12: note: declared private here
     double radius;
            ^~~~~~
```

> **NOTE:**  
> - The output of the above program is a compile time error because we are not allowed to access the private data members of a class directly from outside the class. Yet an access to obj.radius is attempted, but radius being a private data member, we obtained the above compilation error.
> - **However, we can access the private data members of a class indirectly using the public member functions of the class.**

For example, see the code below:

[privateCircle-v2.h](src/privateCircle-v2.h)
```cpp
class Circle
{
private:
    double radius;

public:
    void compute_area(double r);
};
```

[privateCircle-v2.cpp](src/privateCircle-v2.cpp)
```cpp
#include <iostream>
#include "privateCircle-v2.h"

void Circle::compute_area(double r)
{
    radius = r;
    double area = 3.14 * radius * radius;

    std::cout << "Radius is: " << radius << "\n";
    std::cout << "Area is: " << area;
}
```

[drive_privateCircle-v2.cpp](src/drive_privateCircle-v2.cpp)
```cpp
#include <iostream>
#include "privateCircle-v2.h"

int main()
{
    Circle obj;

    obj.compute_area(1.5);
    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ privateCircle-v2.cpp drive_privateCircle-v2.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
Radius is: 1.5
Area is: 7.065
```

---

<div id="intro-protected-modifier"></div>

## Intro to "protected" modifier

The **protected access modifier is similar to the private access modifier** in the sense that it can’t be accessed outside of its class unless with the help of a friend class.

> **The difference is that the class members declared as Protected can be accessed by any subclass (derived class) of that class as well.**

**NOTE:**
This access through inheritance can alter the access modifier of the elements of base class in derived class ***depending on the mode of Inheritance***.

For example, see the code below:

[parent.h](src/parent.h)
```cpp
class Parent
{
protected:
    int id_protected;
};
```

[child.h](src/child.h)
```cpp
#include "parent.h"

class Child : public Parent
{
public:
    void setId(int id);
    void displayId();
};
```

[child.cpp](src/child.cpp)
```cpp
#include <iostream>
#include "child.h"

void Child::setId(int id)
{
    id_protected = id;
}

void Child::displayId()
{
    std::cout << "id_protected is: " << id_protected << "\n";
}
```

[drive_protected.cpp](src/drive_protected.cpp)
```cpp
#include "child.h"

int main()
{
    Child obj1;

    obj1.setId(81);
    obj1.displayId();

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ child.cpp  drive_protected.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
id_protected is: 81
```

---

<div id="intro-to-encapsulation"></div>

## Intro to Encapsulation

> **The meaning of Encapsulation, is to make sure that *"sensitive"* data is hidden from users.**

 - To achieve (conseguir) this, you must declare class variables/attributes as private:
   - Cannot be accessed from outside the class
 - If you want others to read or modify the value of a private member, you can provide public **get** and **set** methods.

![img](images/encapsulation-in-cpp.png)  

---

<div id="get-set-employee"></div>

## Getters & Setters: Employee

[employee.h](src/employee.h)
```cpp
class Employee
{
private:
    int salary;

public:
    void setSalary(int s);
    int getSalary();
};
```

[employee.cpp](src/employee.cpp)
```cpp
#include "employee.h"

void Employee::setSalary(int s)
{
    salary = s;
}

int Employee::getSalary()
{
    return salary;
}
```

[drive_employee.cpp](src/drive_employee.cpp)
```cpp
#include <iostream>
#include "employee.h"

int main()
{
    Employee myObj;
    myObj.setSalary(50000);

    std::cout << "The Employee salary is: " << myObj.getSalary();

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ employee.cpp drive_employee.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
The Employee salary is: 50000
```

 - **Example explained:**
   - The **salary** attribute is private, which have restricted access.
   - The public **setSalary()** method takes a parameter **(s)** and assigns it to the **salary** attribute
     - salary = s.
   - The public **getSalary()** method returns the value of the private **salary** attribute.
   - Inside **main()**, we create an object of the *Employee class*. Now we can use the **setSalary()** method to set the value of the private attribute to **50000**. Then we call the **getSalary()** method on the object to return the value.

---

<div id="get-set-person"></div>

## Getters & Setters: Person

[person.h](src/person.h)
```cpp
#include <string>

class Person
{
private:
    std::string name;
    int age;

public:
    Person(std::string name, int age); // Constructor prototype.

    // Setters
    void setName(std::string name);
    void setAge(int age);

    // Getters
    std::string getName();
    int getAge();
};
```

[person.cpp](src/person.cpp)
```cpp
#include "person.h"

// Constructor.
Person::Person(std::string name, int age)
{
    this->name = name;
    this->age = age;
}

// ------------------ ( Setters ) ------------------

void Person::setName(std::string name)
{
    this->name = name;
}

void Person::setAge(int age)
{
    this->age = age;
}

// ------------------ ( Getters ) ------------------

std::string Person::getName()
{
    return name;
}

int Person::getAge()
{
    return age;
}
```

[drive_person.cpp](src/drive_person.cpp)
```cpp
#include <iostream>
#include "person.h"

int main()
{

    Person person("Rodrigo Leite da Silva", 33);

    std::cout << "Name and Age of Person passed to construct was: "
              << "\n";
    std::cout << "Person name: " << person.getName() << "\n";
    std::cout << "Person age: " << person.getAge() << "\n";

    person.setName("Sir Isaac Newton");
    person.setAge(84);
    std::cout << "\nAfter set name and age:"
              << "\n";

    std::cout << "Name: " << person.getName() << "\n";
    std::cout << "Age: " << person.getAge() << "\n";

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ person.cpp drive_person.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
Name and Age of Person passed to construct was: 
Person name: Rodrigo Leite da Silva
Person age: 33

After set name and age:
Name: Sir Isaac Newton
Age: 84
```

---

**REFERENCES:**  
[Access Modifiers in C++](https://www.geeksforgeeks.org/access-modifiers-in-c/)  
[Encapsulation in C++](https://www.geeksforgeeks.org/encapsulation-in-cpp/)  
[C++ Encapsulation](https://www.w3schools.com/cpp/cpp_encapsulation.asp)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
