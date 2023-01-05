# 'this' pointer in C++

## Contents

 - [How methods access object attributes?](#how-methods-acces-attributes)
 - [When use "this" pointer?](#when-use)
 - **Tips & Tricks:**
   - [const methods](#const-methods)
   - [`"*this"`](#asterisk-this)
   - ["-> (arrow)" vs. ". (dot)"](#arrow-vs-dot)

---

<div id="how-methods-acces-attributes"></div>

## How methods access object attributes?

In the old days (antigamente), *C++* converted methods to functions to access object attributes. For example, see the **showInformation()** method below and how was converted:

**C++ METHOD:**  
```cpp
void Game::showInformation()
{
    cout << name << " R$"
         << price << " "
         << hours << "h = R$"
         << cost << "/h\n";
}

// Driver's example.
Game gears; // Object reference.
gears.showInformation(); // Call object showInformation() method.
```

**C FUNCTION SIMILAR TO "Game::showInformation()" method:**  
```cpp
void :showInformation(Game * this)
{
    cout << this->name << " R$"
         << this->price << " "
         << this->hours << "h = R$"
         << this->cost << "/h\n";
}

// Driver's example.
Game gears; // Object reference.
showInformation(&gears);​ // Pass gears object address (&).
```

 - See that in the function approach we have a pointer this as parameter (Game * this).
 - And when call the function we pass the object address (&).

**NOTE:**  
Currently, the compilers don't translate C++ methods to C functions, but the **"this pointer"** still (ainda) exists​:

 - It is passed implicitly to methods.
 - Points (aponta) to the object used in the call

However, you can access the object attributes explicitly using this in the members of the object *(but this is optional)*:

**C++ METHOD USING "this pointer" (EXPLICITLY APPROACH):**  
```cpp
void Game::showInformation()
{
    cout << this->name << " R$"
         << this->price << " "
         << this->hours << "h = R$"
         << this->cost << "/h\n";
}
```

**NOTE:**  
Another observation is when you call methods in C++ automatically we pass to compilers the object address (&). For example, see the method calls below:

```cpp
Game Gears { "Gears", 90.0f };


gears.update(100.0f);
gears.play(2);
​gears.showInformation();
```

Above, when we call the methods we pass implicitly the compiler:

 - The argument values.
 - And "gears" object address (&):
   - implicitly

---

<div id="when-use"></div>

## When use "this" pointer?

> A common use of "this" pointer is to reference object attributes.

For example, imagine we have the following Game class:

[Game_this.h](src/Game_this.h)
```cpp
#pragma once
#include <string>
using std::string;

class Game
{
private:
    // Encapsulation.
    string name; // Game name.
    float price; // Game price.
    int hours;   // Hours played.
    float cost;  // Cost per hour player.

    // Calculate the cost to played hours (Inline function/Method).
    void calculate()
    {
        if (this->hours > 0)
            this->cost = this->price / this->hours;
    }

public:
    // Interfaces.
    Game(const string &name, float cost = 0); // Constructor prototype.
    void update(float cost);                  // Update game price.
    void play(int hours);                     // Record (save) the hours played.
    void showInformation();                   // show information.
};
```

[Game.cpp](src/Game.cpp)
```cpp
#include <iostream>
#include "Game.h"

void Game::purchase(const string &title, float value)
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

[driver_this-v1.cpp](src/driver_this-v1.cpp)
```cpp
#include "Game_this.h"

int main()
{
	Game gears = { "Gears", 50.0f };

    // Call methods of Game (gow) object.
	gears.showInformation();

	// Call methods of Game (gow) object.
	gears.play(5);
	gears.showInformation();

	// Call methods of Game (gow) object.
	gears.play(3);
	gears.showInformation();
}
```

**COMPILATION AND RUN:**  
```cpp
g++ Game_this.cpp driver_this-v1.cpp -o this

./this
```

**OUTPUT:**  
```
Gears R$50 0h = R$50/h
Gears R$50 5h = R$10/h
Gears R$50 8h = R$6.25/h
```

> **NOTE:**  
> - See that now we can use **this->attribute** to reference object attributes.
> - Now, we also can have the same name to object attributes and constructor of object.

---

<div id="const-methods"></div>

## const methods

> A *const* method can't modify attributes because is translated to constant pointer.

For example the method below is **const**:

**CONST METHOD:**
```cpp
void game::showInformation() const
{
    cout << name << " R$"
         << price << " "
         << hours << "h = R$"
         << cost << "/h\n";
}

Game gears;
gears.showInformation();
```

**TRANSLATED TO FUNCTION:**
```cpp
void showInformation(const Game * this)
{
    cout << this->name << " R$"
         << this->price << " "
         << this->hours << "h = R$"
         << this->cost << "/h\n";
}


Game gears;
gears.showInformation(&gears);
```

---

<div id="asterisk-this"></div>

## `"*this"`

> When we need reference the current object we use `"*this"`

For example, imagine we need return an object in a function:

```cpp
Game & Game::compare(Game & game)
{
    if (game.hours > hours)
        return game;
    else
        return *this;
}​
```

**NOTE:**  
See that in the else block we return the `object (*this)` not the object address (&).

---

<div id="arrow-vs-dot"></div>

## "-> (arrow)" vs. ". (dot)"

> When use **"-> (arrow)"** vs. **". (dot)"** to work with objects?

 - **"-> (arrow)":**
   - Used when you have a pointer.
 - **". (dot)":**
   - Used when you have an object.

---

**REFERENCES:**  
[Aula 07 - Ponteiro this / Vetores de Objetos / Curso de C++](https://www.youtube.com/watch?v=SoX7r_Sq_Rc)  

---
