#include "animal.h"

class Cat : public Animal
{
private:
    std::string type;

public:
    // Constructor to initialize type
    Cat();

    // Override getType() method.
    std::string getType() override;
};
