#include <iostream>
#include "player.h"

int main()
{
    player *messi = new player{"Messi", 100000.00f, 600};

    std::cout << "Player name: " << messi->name << "\n";
    std::cout << "Player salary: " << messi->salary << "\n";
    std::cout << "Player goals: " << messi->goals << "\n";

    delete messi;
    return 0;
}
