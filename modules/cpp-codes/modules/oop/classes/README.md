<<<<<<< HEAD:modules/cpp-codes/modules/oop/classes.md
# Classes

## Contents

 - [Classes in C++ (+Game example)](#classes-in-cpp)
 - [Objects (instances) in C++](#objects-instances)
 - **Tips & Tricks:**
   - [Classes vs. Records (struct)](#class-vs-struct)

---

<div id="classes-in-cpp"></div>

## Classes in C++ (+Game example)

> A **class** in *C++* can represent many **objects**.

A class in C++ is defined in two parts:

 - **Declaration:**
   - Describe the attributes.
   - Describe the methods
 - **Definition:**
   - Methods implementations.

> **NOTE:**  
> Like a *record*, a *class* defines a new type.


For example, the code below represent a **Car class**:

[Car.h](src/Car.h)
```cpp
#include <string>
using std::string;

class Car
{
private:
    // Encapsulation.
    int color;
    string type;
    float velocity;

public:
    // Interfaces.
    void turnOn();
    void turnOff();
    void speed();
    void brake();
};
```

Now, with this class (Car) we can create many objects (abstractions):

![img](images/class-01.png)  

> **NOTE:**  
> Another observation is that usually we declared a **class** in **".h"** file.

**Ok, I know that class are declared in ".h" file, but and the implementations?**  
Implementations or definitions of a class are written another file, reference to your class **(same name your ".h", however using .cpp)**.

For example, imagine we have the **Game class**:

[Game.h](src/Game.h)
```cpp
#pragma once
#include <string>
using std::string;

class Game
{
private:
	// Encapsulation.
	string name;                                        // Game name.
	float price;                                        // Game price.
	int hours;                                          // Hours played.
	float cost;                                         // Cost per hour player.

	// Calculate the cost to played hours (Inline function/Method).
	void calculate() { if (hours > 0) cost = price / hours; }

public:
	// Interfaces.
	void purchase(const string& title, float value);    // Fill the information.
	void update(float value);                           // Update game price.
	void play(int time);                                // Record (save) the hours played.
	void showInformation();                             // show information.
};
```

[Game.cpp](src/Game.cpp)
```cpp
#include <iostream>
#include "Game.h"

void Game::purchase(const string& title, float value)
{
    name = title;
    price = value;
    hours = 0;
    cost = price;
}

void Game::update(float value)
{
    price = value;
    calculate();
}

void Game::play(int time)
{
    hours = hours + time;
    calculate();
}

void Game::showInformation()
{
    std::cout << name << " R$"
        << price << " "
        << hours << "h = R$"
        << cost << "/h\n";
}
```

[driver_game.cpp](src/driver_game.cpp)
```cpp
#include "Game.h"

int main()
{
	Game gow; // Variable of type "Game".

	// Call methods of Game (gow) object.
	gow.purchase("Gow", 160.0f);
	gow.showInformation();

	// Call methods of Game (gow) object.
	gow.play(5);
	gow.showInformation();

	// Call methods of Game (gow) object.
	gow.play(3);
	gow.showInformation();
}
```

**COMPILATION AND RUN:**  
```cpp
g++ Game.cpp driver_game.cpp -o game

./game.exe
```

**OUTPUT:**  
```cpp
Gow R$160 0h = R$160/h
Gow R$160 5h = R$32/h
Gow R$160 8h = R$20/h
```

---

<div id="objects-instances"></div>

## Objects (instances) in C++

> Once (uma vez) you have declared a class, we can create objects (instances)

For example, see how to create two objects (instances) from **Game class** below:

```cpp
int main()
{
   Game gears;​
   Game doom;​
}
```

> An **instance** is the **creation of a type**, reference to our class (Game for our example).

For example, see the image below how objects are created in the memory:

![img](images/instance-01.png)  

 - See we have two **objects (instances)** of the **type Game**.
 - When we create an object (instance) automatically is reserved memory for your attributes *(Game was name, price, ours, cost)*.
 - The **name of the object ("gears" and "doom" for our example)** is a **reference to the memory reserved for the object (instance)**.

---

<div id="class-vs-struct"></div>

## Classes vs. Records (struct)

> What if (e se) the **public** and **private** are omitted?​

 - **Class members** are **private** by *default*.
 - **Record (struct) members** are **public** by *default*. 

For example:

![img](images/classes-vs-records.png)  

**NOTE:**  
See we can *access* and *modify* **record (struct) members** directly, however, **class members** are *private* by *default*, then we can't *access* and *modify* directly, we needed and interface (method) for it.

---

**REFERENCES:**  
[Aula 02 - Classes / Encapsulamento / Curso de C++](https://www.youtube.com/watch?v=pONnilIFY64&list=PLX6Nyaq0ebfhlKSTKlADladUNBHNBXxHg&index=5)  
[Lab02 - Exercícios de Classes / Encapsulamento / Curso de C++](https://www.youtube.com/watch?v=XP91FuJjicM&list=PLX6Nyaq0ebfhlKSTKlADladUNBHNBXxHg&index=6)  
[Aula 03 - Objetos / Instâncias / Curso de C++](https://www.youtube.com/watch?v=wO9IKAjZYyg&list=PLX6Nyaq0ebfhlKSTKlADladUNBHNBXxHg&index=8)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
=======
# Classes

## Contents

 - [Classes in C++ (+Game example)](#classes-in-cpp)
 - [Objects (instances) in C++](#objects-instances)
 - **Tips & Tricks:**
   - [Class members are private by default vs. Record (struct) members are public by default](#class-vs-struct)

---

<div id="classes-in-cpp"></div>

## Classes in C++ (+Game example)

> A **class** in *C++* can represent many **objects**.

A class in C++ is defined in two parts:

 - **Declaration:**
   - Describe the attributes.
   - Describe the methods
 - **Definition:**
   - Methods implementations.

> **NOTE:**  
> Like a *record (struct)*, a *class* defines a new type.


For example, the code below represent a **Car class**:

[Car.h](src/Car.h)
```cpp
#include <string>

class Car
{
private:
    // Encapsulation.
    int color;
    std::string type;
    float velocity;

public:
    // Interfaces.
    void turnOn();
    void turnOff();
    void speed();
    void brake();
};
```

Now, with this class (Car) we can create many objects (abstractions):

![img](images/class-01.png)  

> **NOTE:**  
> Another observation is that usually we declared a **class** in **".h"** file.

**Ok, I know that class are declared in ".h" file, but and the implementations?**  
Implementations or definitions of a class are written another file, reference to your class **(same name your ".h", however using .cpp)**.

For example, imagine we have the **Game class**:

[Game.h](src/Game.h)
```cpp
#include <string>

class Game
{
private:
    // Encapsulation.
    std::string name; // Game name.
    float price;      // Game price.
    int hours;        // Hours played.
    float cost;       // Cost per hour player.

    // Calculate the cost to played hours (Inline function/Method).
    void calculate()
    {
        if (hours > 0)
            cost = price / hours;
    }

public:
    // Interfaces.
    void purchase(const std::string &title, float value); // Fill the information.
    void update(float value);                             // Update game price.
    void play(int time);                                  // Record (save) the hours played.
    void showInformation();                               // show information.
};
```

[Game.cpp](src/Game.cpp)
```cpp
#include <iostream>
#include "Game.h"

void Game::purchase(const std::string &title, float value)
{
    name = title;
    price = value;
    hours = 0;
    cost = price;
}

void Game::update(float value)
{
    price = value;
    calculate();
}

void Game::play(int time)
{
    hours = hours + time;
    calculate();
}

void Game::showInformation()
{
    std::cout << name << " R$"
              << price << " "
              << hours << "h = R$"
              << cost << "/h\n";
}
```

[driver_game.cpp](src/driver_game.cpp)
```cpp
#include "Game.h"

int main()
{
    Game gow; // Variable of type "Game".

    // Call methods of Game (gow) object.
    gow.purchase("Gow", 160.0f);
    gow.showInformation();

    // Call methods of Game (gow) object.
    gow.play(5);
    gow.showInformation();

    // Call methods of Game (gow) object.
    gow.play(3);
    gow.showInformation();
}
```

**COMPILATION AND RUN:**  
```cpp
g++ Game.cpp driver_game.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
Gow R$160 0h = R$160/h
Gow R$160 5h = R$32/h
Gow R$160 8h = R$20/h
```

---

<div id="objects-instances"></div>

## Objects (instances) in C++

> Once (uma vez) you have declared a class, we can create objects (instances)

For example, see how to create two objects (instances) from **Game class** below:

```cpp
int main()
{
   Game gears;​
   Game doom;​
}
```

> An **instance** is the **creation of a type**, reference to our class (Game for our example).

For example, see the image below how objects are created in the memory:

![img](images/instance-01.png)  

 - See we have two **objects (instances)** of the **type Game**.
 - When we create an object (instance) automatically is reserved memory for your attributes *(Game was name, price, ours, cost)*.
 - The **name of the object ("gears" and "doom" for our example)** is a **reference to the memory reserved for the object (instance)**.

---

<div id="class-vs-struct"></div>

## Class members are private by default vs. Record (struct) members are public by default

> What if (e se) the **public** and **private** are omitted?​

 - **Class members** are **private** by *default*.
 - **Record (struct) members** are **public** by *default*. 

For example:

![img](images/classes-vs-records.png)  

**NOTE:**  
See we can *access* and *modify* **record (struct) members** directly, however, **class members** are *private* by *default*, then we can't *access* and *modify* directly, we needed and interface (method) for it.

---

**REFERENCES:**  
[Aula 02 - Classes / Encapsulamento / Curso de C++](https://www.youtube.com/watch?v=pONnilIFY64&list=PLX6Nyaq0ebfhlKSTKlADladUNBHNBXxHg&index=5)  
[Lab02 - Exercícios de Classes / Encapsulamento / Curso de C++](https://www.youtube.com/watch?v=XP91FuJjicM&list=PLX6Nyaq0ebfhlKSTKlADladUNBHNBXxHg&index=6)  
[Aula 03 - Objetos / Instâncias / Curso de C++](https://www.youtube.com/watch?v=wO9IKAjZYyg&list=PLX6Nyaq0ebfhlKSTKlADladUNBHNBXxHg&index=8)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
>>>>>>> cpp-codes:modules/cpp-codes/modules/oop/classes/README.md
