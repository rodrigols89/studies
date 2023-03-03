<<<<<<< HEAD:modules/cpp-codes/modules/oop/src/Game.cpp
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
=======
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
>>>>>>> cpp-codes:modules/cpp-codes/modules/oop/member-functions/src/Game.cpp
