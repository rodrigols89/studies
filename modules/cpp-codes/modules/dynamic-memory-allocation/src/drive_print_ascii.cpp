#include <iostream>
#include "print_ascii.h"

int main()
{
    char ch;

    std::cout << "Enter a character: ";
    std::cin >> ch;

    printASCII(ch);

    return 0;
}
