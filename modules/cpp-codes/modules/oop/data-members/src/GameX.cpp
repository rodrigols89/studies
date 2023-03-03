#include "Game.h"

inline void Game::calculate()
{
    if (hours > 0)
        cost = price / hours;
}
