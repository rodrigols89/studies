#include <iostream>
#include "player.h"

int main()
{
    player messi{"Messi", 100000.00f, 600};
    player *pptr = &messi;

    std::cout << "Data taken ('.') directly of a struct:"
              << "\n";
    std::cout << "Player: " << messi.name << "\n";
    std::cout << "Salary: " << messi.salary << "\n";
    std::cout << "Goals: " << messi.goals << "\n";

    std::cout << "\nData taken ('->') of a struct from a pointer (memory address):"
              << "\n";
    std::cout << "Player: " << pptr->name << "\n";
    std::cout << "Salary: " << pptr->salary << "\n";
    std::cout << "Goals: " << pptr->goals << "\n";

    return 0;
}
