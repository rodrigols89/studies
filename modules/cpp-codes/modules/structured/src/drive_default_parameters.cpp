#include <iostream>
#include "default_parameters.h"

int main()
{
    std::cout << "Function return passing 2 arguments (10, 15): " << sum(10, 15) << "\n";
    std::cout << "Function return passing 3 arguments (10, 15, 25): " << sum(10, 15, 25) << "\n";
    std::cout << "Function return passing 4 arguments (10, 15, 25, 30): " << sum(10, 15, 25, 30) << "\n";

    return 0;
}
