# Modularization in C++

## Contents

 - [Intro to Modularization in C++](#modularization)
 - **Examples:**
   - **Function cases:**
     - [swap() function](#swap-function)
   - **Class cases:**
     - [Game class](#game-class)

---

<div id="modularization"></div>

## Modularization in C++

A C++ program can be divided into different files, where:

 - **file.h**
   - The prototypes of the functions stay here.
   - Class declaration:
     - Attributes.
     - Methods prototypes.
 - **file.cpp**
   - Function definitions stay here.
   - Implementations or definitions of a class are written here.
 - **main_file.cpp**
   - Includes *( headers / .h )* from the functions.
   - Functions calls

---

<div id="swap-function"></div>

## swap() function

Here, let's create a modularized **swap()** function:

[swap.h](src/swap.h)  
```cpp
void swap(int& first, int& second); // Function prototype.
```

[swap.cpp](src/swap.cpp)  
```cpp
#include "swap.h"


void swap(int& first, int& second)
{
    int temp = first;
    first = second;
    second = temp;
}
```

[swap_main.cpp](src/swap_main.cpp)  
```cpp
#include <iostream>
#include "swap.h"
using namespace std;


int main()
{
    int x, y;

    cout << "Enter the first value: ";
    cin >> x;

    cout << "Enter the second value: ";
    cin >> y;

    cout << "Initial values:\n" <<
    "First value: " << x << 
    "\nSecond value: " << y << endl;

    // Call the swap() function.
    swap(x, y);

    cout << "\nAfter swapping:\n" <<
    "First value: " << x << 
    "\nSecond value: " << y << endl;


    return 0;
}
```

**COMPILATION AND RUN:**  
```cpp
g++ swap_main.cpp swap.cpp -o swap

./swap.exe

Enter the first value: 10
Enter the second value: 20
```

**OUTPUT:**
```cpp
Initial values:
First value: 10
Second value: 20

After swapping:
First value: 20
Second value: 10
```

---

<div id="game-class"></div>

## Game class

Here, let's see how modularized a simple **Game class**:

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

**REFERENCES:**  
[Aula 03 - Objetos / Instâncias / Curso de C++](https://www.youtube.com/watch?v=wO9IKAjZYyg&list=PLX6Nyaq0ebfhlKSTKlADladUNBHNBXxHg&index=9)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
