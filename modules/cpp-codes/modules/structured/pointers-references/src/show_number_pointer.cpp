<<<<<<< HEAD:modules/cpp-codes/modules/structured/src/show_number_pointer.cpp
#include <iostream>
#include "show_number_pointer.h"

using namespace std;

void showNumber(int *number)
{
    cout << "The number passe was: " << *number;
}
=======
#include <iostream>
#include "show_number_pointer.h"

void showNumber(int *number)
{
    std::cout << "The number passed was: " << *number;
}
>>>>>>> cpp-codes:modules/cpp-codes/modules/structured/pointers-references/src/show_number_pointer.cpp
