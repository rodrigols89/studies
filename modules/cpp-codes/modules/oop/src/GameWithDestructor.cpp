#include <iostream>
#include "GameWithDestructor.h"

// Class (Game) constructor definition (implementation)
Game::Game(const std::string &name, float cost)
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
