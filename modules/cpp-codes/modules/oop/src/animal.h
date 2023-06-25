#ifndef ANIMAL_CPP
#define ANIMAL_CPP

#include <iostream>

class Animal
{
private:
    std::string type;

public:
    // Constructor to initialize type
    Animal();

    // Declare virtual function
    virtual std::string getType();
};

#endif
