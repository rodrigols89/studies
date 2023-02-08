#include <iostream>
#include "player.h"

int main()
{
    int playersSize;

    std::cout << "Enter the number of players: ";
    std::cin >> playersSize;

    player *vecToPlayers = new player[playersSize];

    for (int i = 0; i < playersSize; i++)
    {
        std::cout << "\nEnter the name of player " << i << ": ";
        std::cin >> vecToPlayers[i].name;
        std::cout << "Enter the salary of player " << i << ": ";
        std::cin >> vecToPlayers[i].salary;
        std::cout << "Enter the number of goals of player " << i << ": ";
        std::cin >> vecToPlayers[i].goals;
    }

    for (int i = 0; i < playersSize; i++)
    {
        std::cout << "\nThe name of player " << i << ": " << vecToPlayers[i].name << "\n";
        std::cout << "The salary of player " << i << ": " << vecToPlayers[i].salary << "\n";
        std::cout << "The number of goals of player " << i << ": " << vecToPlayers[i].goals << "\n";
    }

    delete []vecToPlayers;
    return 0;
}
