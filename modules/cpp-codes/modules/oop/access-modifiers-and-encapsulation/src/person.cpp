#include "person.h"

// Constructor.
Person::Person(std::string name, int age)
{
    this->name = name;
    this->age = age;
}

// ------------------ ( Setters ) ------------------

void Person::setName(std::string name)
{
    this->name = name;
}

void Person::setAge(int age)
{
    this->age = age;
}

// ------------------ ( Getters ) ------------------

std::string Person::getName()
{
    return name;
}

int Person::getAge()
{
    return age;
}
