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
