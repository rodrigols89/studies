#include <iostream>
#include "function_overloading_calculator.h"

int main()
{
    int x = 10;
    int y = 20;
    int z = 30;
    int w = 40;

    Calculator calc;

    std::cout << "x + y: " << calc.add(x, y);
    std::cout << "\nx + y + z: " << calc.add(x, y, z);
    std::cout << "\nx + y + z + w: " << calc.add(x, y, z, w);

    return 0;
}
