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
