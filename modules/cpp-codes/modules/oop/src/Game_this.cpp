#include <iostream>
#include "Game_this.h"

// Class (Game) constructor definition (implementation)
Game::Game(const string &name, float cost)
{
    this->name = name;
    this->price = cost;
    this->hours = 0;
    this->cost = cost;
}

void Game::update(float cost)
{
    this->price = cost;
    calculate();
}

void Game::play(int hours)
{
    this->hours += hours;
    calculate();
}

void Game::showInformation()
{
    std::cout << this->name << " R$"
              << this->price << " "
              << this->hours << "h = R$"
              << this->cost << "/h\n";
}
