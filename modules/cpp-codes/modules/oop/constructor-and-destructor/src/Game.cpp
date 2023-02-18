#include <iostream>
#include "Game.h"

void Game::purchase(const std::string &title, float value)
{
    name = title;
    price = value;
    hours = 0;
    cost = price;
}
