#include <iostream>

int main()
{
    int *iptr = new int; // Allocate memory for an Integer.
    *iptr = 1001;        // Save a value (using "*" operator | Indirection Operator)
    std::cout << "Integer value: " << *iptr << "\n";
    std::cout << "Location: " << iptr << "\n";
    std::cout << "Size of 'iptr': " << sizeof(iptr) << "\n";
    std::cout << "Size of '*iptr': " << sizeof(*iptr) << "\n";

    double *dprt = new double; // Allocate memory for a double
    *dprt = 500.35;            // Save a value (using "*" operator | Indirection Operator)
    std::cout << "\nFloating-point value: " << *dprt << "\n";
    std::cout << "Location: " << dprt << "\n";
    std::cout << "Size of 'dprt': " << sizeof(dprt) << "\n";
    std::cout << "Size of '*dprt': " << sizeof(*dprt) << "\n";

    return 0;
}
