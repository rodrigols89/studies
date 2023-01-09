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
