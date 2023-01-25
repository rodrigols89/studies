#include <iostream>
#include "show_number.h"

int main()
{
    int number;

    std::cout << "Enter a number: ";
    std::cin >> number;

    showNumber(number);

    return 0;
}
