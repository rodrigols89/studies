#include <iostream>
#include "show_number_by_ref.h"

int main()
{
    int number;

    std::cout << "Enter a number: ";
    std::cin >> number;

    showNumber(number);

    return 0;
}
