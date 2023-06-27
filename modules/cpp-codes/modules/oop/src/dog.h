#include "animal.h"

class Dog : public Animal
{
private:
    std::string type;

public:
    // Constructor to initialize type
    Dog();

    // Override getType() method.
    std::string getType() override;
};
