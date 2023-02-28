#include "animal.h"

// Constructor implementation.
Animal::Animal()
{
    type = "Animal";
}

std::string Animal::getType()
{
    return this->type;
}
