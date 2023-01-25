#include <iostream>

int main()
{
    int number = 100;
    int *iptr = &number;

    std::cout << "Value stored in 'number' variable: " << number << "\n";
    std::cout << "Memory Address of 'number' variable: " << &number << "\n";
    std::cout << "Memory Addres saved in 'iptr' pointer: " << iptr << "\n";
    std::cout << "Value stored at 'number' variable referenced by a 'iptr' pointer: " << *iptr;

    return 0;
}
