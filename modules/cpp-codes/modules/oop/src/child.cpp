#include <iostream>
#include "child.h"

void Child::setId(int id)
{
    id_protected = id;
}

void Child::displayId()
{
    std::cout << "id_protected is: " << id_protected << "\n";
}
