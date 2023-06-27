#include "cat.h"

// Constructor implementation.
Cat::Cat()
{
    type = "Cat";
}

// Override getType() method.
std::string Cat::getType()
{
    return type;
}
