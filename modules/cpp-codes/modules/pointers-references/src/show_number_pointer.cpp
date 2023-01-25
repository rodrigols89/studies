#include <iostream>
#include "show_number_pointer.h"

void showNumber(int *number)
{
    std::cout << "The number passed was: " << *number;
}
