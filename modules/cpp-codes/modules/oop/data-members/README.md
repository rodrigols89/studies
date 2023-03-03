# Data Members

## Contents

 - [Static data members](#static-data-members)
 - [Intro to Member functions](#intro-to-member-functions)
 - [Inline Methods](#inline-methods)

---

<div id="static-data-members"></div>

## Static data members

> Static data members are class members that are declared using **static** keywords.

A static member has certain special characteristics. These are:

 - Only one copy of that member is created for the entire class and is shared by all the objects of that class, no matter how many objects are created.
 - It is initialized before any object of this class is being created, even before main starts.
 - It is visible only within the class, but its lifetime is the entire program

---

<div id="intro-to-member-functions"></div>

## Intro to Member functions

**Member Functions** or **Methods** are normal functions, however, they differ only by two special characteristics:

 - Access to private class members.
 - Using (uso) of the *scope resolution operator* **"::"**.

> **NOTE:**  
> The **scope resolution operator "::"** is used to indicate what class the method belongs to.

For example in the [Game.h](src/Game.h) and [Game.cpp](src/Game.cpp):

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
    void calculate() { if (hours > 0) cost = price / hours; }

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

 - **NOTE:**  
   - See that in the [Game.h](src/Game.h) we have the method prototypes.
   - And in [Game.cpp](src/Game.cpp) we indicate what class the method belongs to:
     - Using **scope resolution operator "::"**

---

<div id="inline-methods"></div>

## Inline Methods

> Methods defined in the class declaration, are a*utomatically inline*.

For example, the **calculate() method** below is inline because is defined in the class declaration:

```cpp
#include <string>

class Game
{
private:
    // Encapsulation.
    ...

    // Calculate the cost to played hours (Inline function/Method).
    void calculate() { if (hours > 0) cost = price / hours; }

public:
    // Interfaces.
    ...
};
```

**NOTE:**  
However, these methods can also be defined outside the class declaration, But for that we need to use the **"inline"** keyword:

```cpp
#include "Game.h"

inline void calculate() { if (hours > 0) cost = price / hours; }
```

**NOTE:**  
See now we use the keyword **"inline"** to say that the method is *inline*.

> However, C++ language rules force inline methods to be defined in each **.cpp** file that uses them​.

For example, if we have [GameX.cpp](src/GameX.cpp) and [GameY.cpp](src/GameY.cpp) that use [Game.h](src/Game.h) we needed defined *calculate() method* in both **.cpp**:

[GameX.cpp](src/GameX.cpp)  
```cpp
#include "Game.h"

inline void Game::calculate()
{
    if (hours > 0)
        cost = price / hours;
}
```

[GameY.cpp](src/GameY.cpp)  
```cpp
#include "Game.h"

inline void Game::calculate()
{
    if (hours > 0)
        cost = price / hours;
}
```

> **NOTE:**  
> However, now we have a problem... Duplicate codes to do the same thing.

To solve that we can define the inline method outside the class declaration, however, in the same **.h** file:

[Game-v2.h](src/Game-v2.h)
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

    inline void calculate(); // Prototype.

public:
    // Interfaces.
    void purchase(const std::string &title, float value); // Fill the information.
    void update(float value);                             // Update game price.
    void play(int time);                                  // Record (save) the hours played.
    void showInformation();                               // show information.
};

// Calculate the cost to played hours (Inline function/Method).
void Game::calculate() { if (hours > 0) cost = price / hours; }
```

**NOTE:**  
Now who include this **.h** file can use calculate() method.

> **NOTE:**  
> However, now we have lost the separation of **interface** and **class implementation**.

---

**REFERENCES:**  
[Aula 04 - Funções Membros / Métodos / Curso de C++](https://www.youtube.com/watch?v=_KEVmlFyAFI&list=PLX6Nyaq0ebfhlKSTKlADladUNBHNBXxHg&index=9)  
[Static data members in C++](https://www.geeksforgeeks.org/static-data-members-c/)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**

