<<<<<<< HEAD:modules/cpp-codes/modules/structured/src/driver_number_pointer.cpp
#include <iostream>
#include "show_number_pointer.h"

using namespace std;

int main()
{
    int number;
    int *iptr = &number;

    cout << "Enter a number: ";
    cin >> number;

    showNumber(iptr);

    return 0;
}
=======
#include <iostream>
#include "show_number_pointer.h"

int main()
{
    int number;
    int *iptr = &number;

    std::cout << "Enter a number: ";
    std::cin >> number;

    showNumber(iptr);

    return 0;
}
>>>>>>> cpp-codes:modules/cpp-codes/modules/structured/pointers-references/src/main_number_pointer.cpp
