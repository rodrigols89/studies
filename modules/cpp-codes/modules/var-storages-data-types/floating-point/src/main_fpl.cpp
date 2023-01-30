#include <iostream>
#include <typeinfo>

int main()
{
    int x{5};      // 5 means integer.
    double y{5};   // 5.0 is a floating point literal (no suffix means double type by default).
    double z{5.0}; // 5.0 is a floating point literal (no suffix means double type by default).
    float w{5.0f}; // 5.0 is a floating point literal, f suffix means float type.

    std::cout << "'x' value is " << x << ", Primitive data type is: " << typeid(x).name() << "\n";
    std::cout << "'y' value is " << x << ", Primitive data type is: " << typeid(y).name() << "\n";
    std::cout << "'z' value is " << x << ", Primitive data type is: " << typeid(z).name() << "\n";
    std::cout << "'w' value is " << x << ", Primitive data type is: " << typeid(w).name() << "\n";

    return 0;
}
