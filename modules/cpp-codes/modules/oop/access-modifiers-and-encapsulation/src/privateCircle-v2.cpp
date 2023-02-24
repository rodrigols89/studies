#include <iostream>
#include "privateCircle-v2.h"

void Circle::compute_area(double r)
{
    radius = r;
    double area = 3.14 * radius * radius;

    std::cout << "Radius is: " << radius << "\n";
    std::cout << "Area is: " << area;
}
