#include <iostream>
#include "show_number_pointer.h"

int main()
{
    int number;
    int *iptr = &number;

    std::cout << "Enter a number: ";
    std::cin >> number;

    showNumber(iptr);

    return 0;
}
