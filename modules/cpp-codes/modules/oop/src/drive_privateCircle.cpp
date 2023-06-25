#include <iostream>
#include "privateCircle.h"

int main()
{
    // Creating object of the class
    Circle obj;

    // Trying to access private data member
    // directly outside the class
    obj.radius = 1.5;

    std::cout << "Area is:" << obj.compute_area();
    return 0;
}
