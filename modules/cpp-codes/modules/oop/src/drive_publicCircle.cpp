#include <iostream>
#include "publicCircle.h"

int main()
{
    Circle obj;

    // Accessing public data member outside the class.
    obj.radius = 5.5;

    std::cout << "Radius is: " << obj.radius << "\n";
    std::cout << "Area is: " << obj.compute_area() << "\n";
    return 0;
}
