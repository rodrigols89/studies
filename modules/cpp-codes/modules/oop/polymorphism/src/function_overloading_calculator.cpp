#include "function_overloading_calculator.h"

int Calculator::add(int x, int y)
{
    return x + y;
}

int Calculator::add(int x, int y, int z)
{
    return x + y + z;
}

int Calculator::add(int x, int y, int z, int w)
{
    return x + y + z + w;
}
