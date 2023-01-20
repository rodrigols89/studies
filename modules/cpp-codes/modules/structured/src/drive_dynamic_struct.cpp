#include <iostream>
#include "player.h"

using namespace std;

int main()
{
    player *messi = new player{"Messi", 100000.00f, 600};

    cout << "Player name: " << messi->name << endl;
    cout << "Player salary: " << messi->salary << endl;
    cout << "Player goals: " << messi->goals << endl;

    delete messi;
    return 0;
}
