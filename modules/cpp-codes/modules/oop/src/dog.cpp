#include "dog.h"

// Constructor implementation.
Dog::Dog()
{
    type = "Dog";
}

// Override getType() method.
std::string Dog::getType()
{
    return type;
}
