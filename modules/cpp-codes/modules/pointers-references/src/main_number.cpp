<<<<<<< HEAD:modules/cpp-codes/modules/structured/src/driver_number.cpp
#include <iostream>
#include "show_number.h"

using namespace std;

int main()
{
    int number;

    cout << "Enter a number: ";
    cin >> number;

    showNumber(number);

    return 0;
}
=======
#include <iostream>
#include "show_number.h"

int main()
{
    int number;

    std::cout << "Enter a number: ";
    std::cin >> number;

    showNumber(number);

    return 0;
}
>>>>>>> cpp-codes:modules/cpp-codes/modules/structured/pointers-references/src/main_number.cpp
