<<<<<<< HEAD:modules/cpp-codes/modules/oop/constructor-and-destructor.md
# Constructor & Destructor (+Object Lifecycle)

## Contents

 - **Constructor:**
   - [Problem and intro to Constructors](#problem-intro)
   - [Initializing constructors](#initializing-constructors)
   - [Default parameters (Good example)](#default-parameters)
 - **Destructor:**
   - [Intro to C++ Destructor](#intro-to-des)
 - **Tips & Tricks:**
   - [Object Lifecycle in C++](#object-lifecycle)
   - [Attributes (members) & Constructor parameters conventions](#attributes-constructor-conventions)

---

<div id="problem-intro"></div>

## Problem and intro to Constructors

Imagine we have the follow Game class:

[Game.h](src/Game.h)
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
        if (hours > 0)
            cost = price / hours;
    }

public:
    // Interfaces.
    void purchase(const string &title, float value); // Fill the information.
    void update(float value);                        // Update game price.
    void play(int time);                             // Record (save) the hours played.
    void showInformation();                          // show information.
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
```

Here we have the method **purchase()** to init the attributes. However, imagine we make a Game object and use **play()** and **showInformation()** methods without use **purchase()**:

[testing_game_wt_purchase.cpp](src/testing_game_wt_purchase.cpp)
```cpp
#include "Game.h"

int main()
{
	Game gow; // Variable of type "Game".

	// Call methods of Game (gow) object.
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
g++ Game.cpp testing_game_wt_purchase.cpp -o game

./game.exe
```

**OUTPUT:**  
```
R$1.12104e-44 0h = R$8.26766e-44/h
R$1.12104e-44 5h = R$2.8026e-45/h
R$1.12104e-44 8h = R$1.4013e-45/h
```

**What?**  
Well, the problem is that we don't initialize the attribute before play the game. That's, **we have trash in the memory**:

![img](images/game-trashinthememory.png)  

> **Ok, how solve that?**  
> Using *constructor*.

 - The constructor is declared in the class declaration (.h file).
 - The constructor have the same class name:
   - However, has no return.

For example, let's see a constructor for the class Game:

[GameWithConstructor.h](src/GameWithConstructor.h)
```cpp
#pragma once
#include <string>
using std::string;

class Game
{
private:
    // Encapsulation.
    string m_name; // Game name.
    float m_price; // Game price.
    int m_hours;   // Hours played.
    float m_cost;  // Cost per hour player.

    // Calculate the cost to played hours (Inline function/Method).
    void calculate()
    {
        if (m_hours > 0)
            m_cost = m_price / m_hours;
    }

public:
    // Interfaces.
    Game(const string &name, float cost = 0); // Constructor prototype.
    void update(float cost);                  // Update game price.
    void play(int hours);                     // Record (save) the hours played.
    void showInformation();                   // show information.
};
```

[GameWithConstructor.cpp](src/GameWithConstructor.cpp)
```cpp
#include <iostream>
#include "GameWithConstructor.h"

// Class (Game) constructor definition (implementation)
Game::Game(const string &name, float cost)
{
    m_name = name;
    m_price = cost;
    m_hours = 0;
    m_cost = cost;
}

void Game::update(float cost)
{
    m_price = cost;
    calculate();
}

void Game::play(int hours)
{
    m_hours += hours;
    calculate();
}

void Game::showInformation()
{
    std::cout << m_name << " R$"
              << m_price << " "
              << m_hours << "h = R$"
              << m_cost << "/h\n";
}
```

[testing_constructor.cpp](src/testing_constructor.cpp)
```cpp
#include "GameWithConstructor.h"

int main()
{
	Game gow = Game("Gears", 50.0f);

	// Call methods of Game (gow) object.
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
g++ GameWithConstructor.cpp testing_constructor.cpp -o gamewc

./gamewc.exe 
```

**OUTPUT:**  
```cpp
Gears R$50 0h = R$50/h
Gears R$50 5h = R$10/h
Gears R$50 8h = R$6.25/h
```

> **NOTE:**  
> Another advantage of creating a constructor is forcing anyone who instantiates an object to always start its attributes (members).

---

<div id="initializing-constructors"></div>

## Initializing constructors

There are three common approaches to initialize a constructor:

**Explicitly approach:**  
```cpp
Game gow = Game("Gears", 50.0f);
```

**Implicitly approach:**
```cpp
Game gow("Gears", 50.0f);
```

**List approach:**
```cpp
Game gow { "Gears", 50.0f };

or

Game gow = { "Gears", 50.0f };
```

---

<div id="default-parameters"></div>

## Default parameters

> **Default parameters** in a constructor are **defined in the "constructor prototype"** *not in the constructor definition (implementation)*.

For example, see default parameters for Game class below:

[default_parameters.h](src/default_parameters.h)
```cpp
#pragma once
#include <string>
using std::string;

class Game
{
private:
    string m_name;
    float m_price;
    int m_hours;
    float m_cost;

    // Inline function.
    void calculate() { if (m_hours > 0) m_cost = m_price / m_hours; }

public:
    // Constructor prototype (with default parameters).
    Game(const string &name = "Gears", float price = 100, int hours = 0, float cost = 0);

    void update(float cost);
    void play(int hours);
    void showInformation();
};
```

[default_parameters.cpp](src/default_parameters.cpp)
```cpp
#include <iostream>
#include "default_parameters.h"

// Class (Game) constructor definition (implementation)
Game::Game(const string &name, float price, int hours, float cost)
{
    m_name = name;
    m_price = price;
    m_hours = hours;
    m_cost = cost;
}

void Game::update(float cost)
{
    m_price = cost;
    calculate();
}

void Game::play(int hours)
{
    m_hours += hours;
    calculate();
}

void Game::showInformation()
{
    std::cout << "Game name: "       << m_name <<
                 ", Price: R$"       << m_price <<
                 ", Hours played:  " << m_hours <<
                 ", Game Cost: R$"   << m_cost << "/h\n";
}
```

[testing_default_parameters.cpp](src/testing_default_parameters.cpp)
```cpp
#include "default_parameters.h"

int main()
{
	Game gow;

	// Call methods of Game (gow) object.
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
g++ default_parameters.cpp testing_default_parameters.cpp -o game

./game.exe
```

**OUTPUT:**  
```
Game name: Gears, Price: R$100, Hours played:  0, Game Cost: R$0/h
Game name: Gears, Price: R$100, Hours played:  5, Game Cost: R$20/h
Game name: Gears, Price: R$100, Hours played:  8, Game Cost: R$12.5/h
```

**NOTE:**  
See that now we have default parameters for our constructor.

---

<div id="intro-to-des"></div>

## Intro to C++ Destructor

 - **Destructor** is a **special member function (method)** that has the same class name, however, preceded by **"~"**.

For example, see below the **Destructor** for the Game class:

[GameWithDestructor.h](src/GameWithDestructor.h)
```cpp
#pragma once
#include <string>
using std::string;

class Game
{
private:
    // Encapsulation.
    string m_name; // Game name.
    float m_price; // Game price.
    int m_hours;   // Hours played.
    float m_cost;  // Cost per hour player.

    // Calculate the cost to played hours (Inline function/Method).
    void calculate()
    {
        if (m_hours > 0)
            m_cost = m_price / m_hours;
    }

public:
    // Interfaces.
    Game(const string &name, float cost = 0); // Constructor prototype.
    ~Game(); // Destructor prototype.

    void update(float cost);                  // Update game price.
    void play(int hours);                     // Record (save) the hours played.
    void showInformation();                   // show information.
};
```

[GameWithDestructor.cpp](src/GameWithDestructor.cpp)
```cpp
#include <iostream>
#include "GameWithDestructor.h"

// Class (Game) constructor definition (implementation)
Game::Game(const string &name, float cost)
{
    m_name = name;
    m_price = cost;
    m_hours = 0;
    m_cost = cost;
}

// Class (Game) destructor definition (implementation)
Game::~Game()
{
    // Empty
}

// Other codes...
```

**NOTE:**  
An observation is that a **Destructor** doesn't have parameters.

> **Ok, but what is a destructor for?**

 - The **destructor** is called automatically when the *object's life comes to an end*.
 - Or when you call him before the object's life runs out.

For example, imagine we have the function **process()** that create an object Game:

```cpp
void process()
{
    Game gears; // The Constructor is called here.

} // The Destructor is called here, in the end of the block.
```

**NOTE:**  
See that, the Destructor is called automatically **in the end of the block** (If you don't call him first).

> **Okay, but if destructors are called at the end of each block automatically, why do I need to create mine? (o meu)**

 - The function of the destructor is to **terminate/destroy** things​:
   - Important for working with resources​:
     - Dynamic Memory Allocation.​
     - File reading​.
     - Opening of connections.

For example, imagine we have a **constructor** to create a **set (yes, math set)**:

```cpp
Set::Set(int n)
{
    // Memory alocation.
    vet = new int[n];
}
```

The **destructor** to our example is:

```cpp
Sets::~Sets()
{
    delete [] vet;
}​
```

 - Now, we just need call the destructor to destroy the object **Set** before our destructor is automatically called.
 - The advantage is that we are saving (economizando) memory.

---

<div id="object-lifecycle"></div>

## Object Lifecycle in C++

Let's, getting started with the following question:

> [EN] - When does an object's life come to an end?
> [PT] - Quando a vida de um objeto chega ao fim?

 - **Depends where your object was created:**
   - Variable static or global?
   - Variable local ou parameter?
   - Dynamic allocation?
   - Temporary?

**GLOBAL OBJECTS:**  
If you object is global him is destroyed in the end of the program. For example:

```cpp
Game gears { "gears" }; // The Constructor is called here.

int main()
{
    ...
}
// The Destructor is called here, in the end of the program.​
```

**STATIC OBJECTS:**  
Static objects are created in the object instance and destroyed in the end of the program. For example:

```cpp
void process()
{
    // Static object.
    static Game doom { "Doom" }; // The Constructor is called here.
    ...
}

int main()
{
    process();
    ...
}
// The Destructor is called here, in the end of the program.​​
```

**LOCAL OBJECTS:**  
Local objects are created in the object instance and destroyed in the end of the block where was created. For example:

```cpp
void process(Game j) // The Constructor is called here.
{
    ...
} // The Destructor is called here, in the end of the block.

int main()
{
    Game gta ( "GTA" ); // The Constructor is called here.

    process(gta);
    ...
} // The Destructor is called here, in the end of the block.​
```

**OBJECTS CREATED DYNAMICALLY:**  
Objects created dynamically are controlled by the programmer. Created when the programer use keyword *"new"* and destroyed when the programmer use keyword *"delete"*. For example:

```cpp
int main()
{
    Game * rdr = new Game { "RDR" }; // The Constructor is called here.

    process(rdr);
    ...
}

void process(Game * pJ)
{
    delete pJ;  // The Destructor is called here.
}​
```

---

<div id="attributes-constructor-conventions"></div>

## Attributes (members) & Constructor parameters conventions

> The **constructor parameters** can't have the same name of the attributes (members) of the class.

There are two common conventions to solve that:

 - **Prefix:**
   - The first is using the prefix **"m_"** before your attribute (member).
     - **"m_"** is abbreviation to **"member"**.
 - **suffix:**
   - The second is using the suffix **"_"** after your attribute (member).

For example, to our Game class we used **prefix "m_"**:

[GameWithConstructor.h](src/GameWithConstructor.h)
```cpp
#pragma once
#include <string>
using std::string;

class Game
{
private:
    // Encapsulation.
    string m_name; // Game name.
    float m_price; // Game price.
    int m_hours;   // Hours played.
    float m_cost;  // Cost per hour player.

    // Calculate the cost to played hours (Inline function/Method).
    void calculate()
    {
        if (m_hours > 0)
            m_cost = m_price / m_hours;
    }

public:
    // Interfaces.
    Game(const string &name, float cost = 0); // Constructor prototype.
    void update(float cost);                  // Update game price.
    void play(int hours);                     // Record (save) the hours played.
    void showInformation();                   // show information.
};
```

 - See we have the **prefix "m_"** in the **attributes (members)**.
 - And **not having the "m_"** prefix in the **constructor parameters**.

---

**REFERENCES:**  
[Aula 05 - Construtores / Construtor Padrão / Curso de C++](https://www.youtube.com/watch?v=ziFZul0HCyU&list=PLX6Nyaq0ebfhlKSTKlADladUNBHNBXxHg&index=12)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
=======
# Constructor & Destructor (+Object Lifecycle)

## Contents

 - **Constructor:**
   - [Problem and intro to Constructors](#problem-intro)
   - [Initializing constructors](#initializing-constructors)
   - [Default parameters (Good example)](#default-parameters)
 - **Destructor:**
   - [Intro to C++ Destructor](#intro-to-des)
 - **Tips & Tricks:**
   - [Object Lifecycle in C++](#object-lifecycle)
   - [Attributes (members) & Constructor parameters conventions](#attributes-constructor-conventions)

---

<div id="problem-intro"></div>

## Problem and intro to Constructors

Imagine we have the follow Game class:

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

void Game::purchase(const string& title, float value)
{
    name = title;
    price = value;
    hours = 0;
    cost = price;
}
```

Here we have the method **purchase()** to init the attributes. However, imagine we make a Game object and use **play()** and **showInformation()** methods without use **purchase()**:

[testing_game_wt_purchase.cpp](src/testing_game_wt_purchase.cpp)
```cpp
#include "Game.h"

int main()
{
    Game gow; // Variable of type "Game".

    // Call methods of Game (gow) object.
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
g++ Game.cpp testing_game_wt_purchase.cpp -o game

./game.exe
```

**OUTPUT:**  
```
R$1.12104e-44 0h = R$8.26766e-44/h
R$1.12104e-44 5h = R$2.8026e-45/h
R$1.12104e-44 8h = R$1.4013e-45/h
```

**What?**  
Well, the problem is that we don't initialize the attribute before play the game. That's, **we have trash in the memory**:

![img](images/game-trashinthememory.png)  

> **Ok, how solve that?**  
> Using *constructor*.

 - The constructor is declared in the class declaration (.h file).
 - The constructor have the same class name:
   - However, has no return.

For example, let's see a constructor for the class Game:

[GameWithConstructor.h](src/GameWithConstructor.h)
```cpp
#pragma once
#include <string>
using std::string;

class Game
{
private:
    // Encapsulation.
    string m_name; // Game name.
    float m_price; // Game price.
    int m_hours;   // Hours played.
    float m_cost;  // Cost per hour player.

    // Calculate the cost to played hours (Inline function/Method).
    void calculate()
    {
        if (m_hours > 0)
            m_cost = m_price / m_hours;
    }

public:
    // Interfaces.
    Game(const string &name, float cost = 0); // Constructor prototype.
    void update(float cost);                  // Update game price.
    void play(int hours);                     // Record (save) the hours played.
    void showInformation();                   // show information.
};
```

[GameWithConstructor.cpp](src/GameWithConstructor.cpp)
```cpp
#include <iostream>
#include "GameWithConstructor.h"

// Class (Game) constructor definition (implementation)
Game::Game(const string &name, float cost)
{
    m_name = name;
    m_price = cost;
    m_hours = 0;
    m_cost = cost;
}

void Game::update(float cost)
{
    m_price = cost;
    calculate();
}

void Game::play(int hours)
{
    m_hours += hours;
    calculate();
}

void Game::showInformation()
{
    std::cout << m_name << " R$"
              << m_price << " "
              << m_hours << "h = R$"
              << m_cost << "/h\n";
}
```

[testing_constructor.cpp](src/testing_constructor.cpp)
```cpp
#include "GameWithConstructor.h"

int main()
{
	Game gow = Game("Gears", 50.0f);

	// Call methods of Game (gow) object.
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
g++ GameWithConstructor.cpp testing_constructor.cpp -o gamewc

./gamewc.exe 
```

**OUTPUT:**  
```cpp
Gears R$50 0h = R$50/h
Gears R$50 5h = R$10/h
Gears R$50 8h = R$6.25/h
```

> **NOTE:**  
> Another advantage of creating a constructor is forcing anyone who instantiates an object to always start its attributes (members).

---

<div id="initializing-constructors"></div>

## Initializing constructors

There are three common approaches to initialize a constructor:

**Explicitly approach:**  
```cpp
Game gow = Game("Gears", 50.0f);
```

**Implicitly approach:**
```cpp
Game gow("Gears", 50.0f);
```

**List approach:**
```cpp
Game gow { "Gears", 50.0f };

or

Game gow = { "Gears", 50.0f };
```

---

<div id="default-parameters"></div>

## Default parameters

> **Default parameters** in a constructor are **defined in the "constructor prototype"** *not in the constructor definition (implementation)*.

For example, see default parameters for Game class below:

[default_parameters.h](src/default_parameters.h)
```cpp
#pragma once
#include <string>
using std::string;

class Game
{
private:
    string m_name;
    float m_price;
    int m_hours;
    float m_cost;

    // Inline function.
    void calculate() { if (m_hours > 0) m_cost = m_price / m_hours; }

public:
    // Constructor prototype (with default parameters).
    Game(const string &name = "Gears", float price = 100, int hours = 0, float cost = 0);

    void update(float cost);
    void play(int hours);
    void showInformation();
};
```

[default_parameters.cpp](src/default_parameters.cpp)
```cpp
#include <iostream>
#include "default_parameters.h"

// Class (Game) constructor definition (implementation)
Game::Game(const string &name, float price, int hours, float cost)
{
    m_name = name;
    m_price = price;
    m_hours = hours;
    m_cost = cost;
}

void Game::update(float cost)
{
    m_price = cost;
    calculate();
}

void Game::play(int hours)
{
    m_hours += hours;
    calculate();
}

void Game::showInformation()
{
    std::cout << "Game name: "       << m_name <<
                 ", Price: R$"       << m_price <<
                 ", Hours played:  " << m_hours <<
                 ", Game Cost: R$"   << m_cost << "/h\n";
}
```

[testing_default_parameters.cpp](src/testing_default_parameters.cpp)
```cpp
#include "default_parameters.h"

int main()
{
	Game gow;

	// Call methods of Game (gow) object.
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
g++ default_parameters.cpp testing_default_parameters.cpp -o game

./game.exe
```

**OUTPUT:**  
```
Game name: Gears, Price: R$100, Hours played:  0, Game Cost: R$0/h
Game name: Gears, Price: R$100, Hours played:  5, Game Cost: R$20/h
Game name: Gears, Price: R$100, Hours played:  8, Game Cost: R$12.5/h
```

**NOTE:**  
See that now we have default parameters for our constructor.

---

<div id="intro-to-des"></div>

## Intro to C++ Destructor

 - **Destructor** is a **special member function (method)** that has the same class name, however, preceded by **"~"**.

For example, see below the **Destructor** for the Game class:

[GameWithDestructor.h](src/GameWithDestructor.h)
```cpp
#pragma once
#include <string>
using std::string;

class Game
{
private:
    // Encapsulation.
    string m_name; // Game name.
    float m_price; // Game price.
    int m_hours;   // Hours played.
    float m_cost;  // Cost per hour player.

    // Calculate the cost to played hours (Inline function/Method).
    void calculate()
    {
        if (m_hours > 0)
            m_cost = m_price / m_hours;
    }

public:
    // Interfaces.
    Game(const string &name, float cost = 0); // Constructor prototype.
    ~Game(); // Destructor prototype.

    void update(float cost);                  // Update game price.
    void play(int hours);                     // Record (save) the hours played.
    void showInformation();                   // show information.
};
```

[GameWithDestructor.cpp](src/GameWithDestructor.cpp)
```cpp
#include <iostream>
#include "GameWithDestructor.h"

// Class (Game) constructor definition (implementation)
Game::Game(const string &name, float cost)
{
    m_name = name;
    m_price = cost;
    m_hours = 0;
    m_cost = cost;
}

// Class (Game) destructor definition (implementation)
Game::~Game()
{
    // Empty
}

// Other codes...
```

**NOTE:**  
An observation is that a **Destructor** doesn't have parameters.

> **Ok, but what is a destructor for?**

 - The **destructor** is called automatically when the *object's life comes to an end*.
 - Or when you call him before the object's life runs out.

For example, imagine we have the function **process()** that create an object Game:

```cpp
void process()
{
    Game gears; // The Constructor is called here.

} // The Destructor is called here, in the end of the block.
```

**NOTE:**  
See that, the Destructor is called automatically **in the end of the block** (If you don't call him first).

> **Okay, but if destructors are called at the end of each block automatically, why do I need to create mine? (o meu)**

 - The function of the destructor is to **terminate/destroy** things​:
   - Important for working with resources​:
     - Dynamic Memory Allocation.​
     - File reading​.
     - Opening of connections.

For example, imagine we have a **constructor** to create a **set (yes, math set)**:

```cpp
Set::Set(int n)
{
    // Memory alocation.
    vet = new int[n];
}
```

The **destructor** to our example is:

```cpp
Sets::~Sets()
{
    delete [] vet;
}​
```

 - Now, we just need call the destructor to destroy the object **Set** before our destructor is automatically called.
 - The advantage is that we are saving (economizando) memory.

---

<div id="object-lifecycle"></div>

## Object Lifecycle in C++

Let's, getting started with the following question:

> [EN] - When does an object's life come to an end?
> [PT] - Quando a vida de um objeto chega ao fim?

 - **Depends where your object was created:**
   - Variable static or global?
   - Variable local ou parameter?
   - Dynamic allocation?
   - Temporary?

**GLOBAL OBJECTS:**  
If you object is global him is destroyed in the end of the program. For example:

```cpp
Game gears { "gears" }; // The Constructor is called here.

int main()
{
    ...
}
// The Destructor is called here, in the end of the program.​
```

**STATIC OBJECTS:**  
Static objects are created in the object instance and destroyed in the end of the program. For example:

```cpp
void process()
{
    // Static object.
    static Game doom { "Doom" }; // The Constructor is called here.
    ...
}

int main()
{
    process();
    ...
}
// The Destructor is called here, in the end of the program.​​
```

**LOCAL OBJECTS:**  
Local objects are created in the object instance and destroyed in the end of the block where was created. For example:

```cpp
void process(Game j) // The Constructor is called here.
{
    ...
} // The Destructor is called here, in the end of the block.

int main()
{
    Game gta ( "GTA" ); // The Constructor is called here.

    process(gta);
    ...
} // The Destructor is called here, in the end of the block.​
```

**OBJECTS CREATED DYNAMICALLY:**  
Objects created dynamically are controlled by the programmer. Created when the programer use keyword *"new"* and destroyed when the programmer use keyword *"delete"*. For example:

```cpp
int main()
{
    Game * rdr = new Game { "RDR" }; // The Constructor is called here.

    process(rdr);
    ...
}

void process(Game * pJ)
{
    delete pJ;  // The Destructor is called here.
}​
```

---

<div id="attributes-constructor-conventions"></div>

## Attributes (members) & Constructor parameters conventions

> The **constructor parameters** can't have the same name of the attributes (members) of the class.

There are two common conventions to solve that:

 - **Prefix:**
   - The first is using the prefix **"m_"** before your attribute (member).
     - **"m_"** is abbreviation to **"member"**.
 - **suffix:**
   - The second is using the suffix **"_"** after your attribute (member).

For example, to our Game class we used **prefix "m_"**:

[GameWithConstructor.h](src/GameWithConstructor.h)
```cpp
#pragma once
#include <string>
using std::string;

class Game
{
private:
    // Encapsulation.
    string m_name; // Game name.
    float m_price; // Game price.
    int m_hours;   // Hours played.
    float m_cost;  // Cost per hour player.

    // Calculate the cost to played hours (Inline function/Method).
    void calculate()
    {
        if (m_hours > 0)
            m_cost = m_price / m_hours;
    }

public:
    // Interfaces.
    Game(const string &name, float cost = 0); // Constructor prototype.
    void update(float cost);                  // Update game price.
    void play(int hours);                     // Record (save) the hours played.
    void showInformation();                   // show information.
};
```

 - See we have the **prefix "m_"** in the **attributes (members)**.
 - And **not having the "m_"** prefix in the **constructor parameters**.

---

**REFERENCES:**  
[Aula 05 - Construtores / Construtor Padrão / Curso de C++](https://www.youtube.com/watch?v=ziFZul0HCyU&list=PLX6Nyaq0ebfhlKSTKlADladUNBHNBXxHg&index=12)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
>>>>>>> cpp-codes:modules/cpp-codes/modules/oop/constructor-and-destructor/README.md
