#include <iostream>
#include "publicCircle.h"

int main()
{
    Circle obj;

    // Accessing public dat amember outside the class.
    obj.radius = 5.5;

    std::cout << "Radius is: " << obj.radius << "\n";
    std::cout << "Area is: " << obj.compute_area();
    return 0;
}
