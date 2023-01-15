#include <iostream>
#include "player.h"

using namespace std;

int main()
{
    player messi{"Messi", 100000.00f, 600};
    player *pptr = &messi;

    cout << "Data taken ('.') directly of a struct:" << endl;
    cout << "Player: " << messi.name << endl;
    cout << "Salary: " << messi.salary << endl;
    cout << "Goals: " << messi.goals << endl;

    cout << "\nData taken ('->') of a struct from a pointer:" << endl;
    cout << "Player: " << pptr->name << endl;
    cout << "Salary: " << pptr->salary << endl;
    cout << "Goals: " << pptr->goals << endl;

    return 0;
}
