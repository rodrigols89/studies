#include <iostream>

void printASCII(char ch)
{
    int *p = new int{ch};
    std::cout << "The ASCII number is: " << *p << "\n";
}
