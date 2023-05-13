#include <iostream>
#include "vectors.h"

int main()
{
    std::cout << "================ ( 2D Vector example ) ================\n";

    vec2 v1_2d = {5.0f, 4.0f};
    vec2 v2_2d = {10.0f, 8.0f};
    float dot_product_2d;

    dot_product_2d = Dot(v1_2d, v1_2d);
    std::cout << "Dot Product: " << dot_product_2d << "\n";

    std::cout << "================ ( 3D Vector example ) ================\n";

    vec3 v1_3d = {5.0f, 4.0f, 6.0f};
    vec3 v2_3d = {10.0f, 8.0f, 3.0f};
    float dot_product_3d;

    dot_product_3d = Dot(v1_3d, v2_3d);
    std::cout << "Dot Product: " << dot_product_3d;

    return 0;
}
