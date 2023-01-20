#include <iostream>
#include "player.h"

using namespace std;

int main()
{
    int playersSize;

    cout << "Enter the number of players: ";
    cin >> playersSize;

    player *vecToPlayers = new player[playersSize];

    for (int i = 0; i < playersSize; i++)
    {
        cout << "\nEnter the name of player " << i << ": ";
        cin >> vecToPlayers[i].name;
        cout << "Enter the salary of player " << i << ": ";
        cin >> vecToPlayers[i].salary;
        cout << "Enter the number of goals of player " << i << ": ";
        cin >> vecToPlayers[i].goals;
    }

    for (int i = 0; i < playersSize; i++)
    {
        cout << "\nThe name of player " << i << ": " << vecToPlayers[i].name << endl;
        cout << "The salary of player " << i << ": " << vecToPlayers[i].salary << endl;
        cout << "The number of goals of player " << i << ": " << vecToPlayers[i].goals << endl;
    }

    delete []vecToPlayers;
    return 0;
}
