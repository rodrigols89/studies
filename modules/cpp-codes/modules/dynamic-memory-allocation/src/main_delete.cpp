#include <iostream>

int main()
{
    int *iptr = new int; // Allocate memory for an Integer.
    *iptr = 30;          // Save a value (using "*" operator | Indirection Operator)

    std::cout << "Memory Address save in 'iptr' pointer: " << iptr << "\n";
    std::cout << "Value save in the Memory Address save in 'iptr' pointer: " << *iptr << "\n";
    std::cout << "Memory Address of 'iptr' pointer: " << &iptr << "\n"
              << "\n";

    delete iptr;

    std::cout << "After use 'delete' operator in 'iptr' pointer: "
              << "\n";
    std::cout << "Memory Address save in 'iptr' pointer: " << iptr << "\n";
    std::cout << "Value save in the Memory Address save in 'iptr' pointer: " << *iptr << "\n";
    std::cout << "Memory Address of 'iptr' pointer: " << &iptr << "\n";

    return 0;
}
